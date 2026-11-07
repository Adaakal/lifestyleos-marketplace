#!/usr/bin/env python3
"""
clipcut.py: turn a Content Reverse Engineer EDL into a finished MP4.

Usage:
  python3 clipcut.py --edl EDL.json --out OUT.mp4 [--burn] [--pad 0.15] [--font PATH] [--box 0xRRGGBB@ALPHA]
                     [--stitch-only] PART1.mp4 [PART2.mp4 PART3.mp4 ...]

Parts are joined IN THE ORDER GIVEN into one continuous source timeline, so
the EDL's SOURCE timecodes refer to the joined recording (the same timeline
the caption editor showed for the full video). One part = the old behaviour.

--stitch-only  writes the joined source to OUT.mp4 and prints each part's
               offset, without cutting. Use it to confirm part order first.
"""
import json, subprocess, sys, os, shlex, tempfile

def tc(v):
    if isinstance(v, (int, float)): return float(v)
    parts = [float(p) for p in str(v).strip().split(":")]
    while len(parts) < 3: parts.insert(0, 0.0)
    return parts[0]*3600 + parts[1]*60 + parts[2]

def fmt(s):
    m = int(s // 60); r = s - m*60
    return f"{m}:{r:04.1f}"

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.stderr.write(r.stderr); sys.exit(r.returncode)
    return r.stdout

def duration(path):
    return float(run(["ffprobe","-v","error","-show_entries","format=duration",
                      "-of","default=nw=1:nk=1", path]).strip())

def normalize(src, dst, vf):
    """Re-encode a part to one common format so parts concat cleanly."""
    run(["ffmpeg","-y","-i",src,"-vf",vf+",fps=30,format=yuv420p",
         "-c:v","libx264","-preset","fast","-crf","18",
         "-c:a","aac","-b:a","192k","-ar","48000","-ac","2","-movflags","+faststart", dst])

def concat(paths, dst):
    lst = dst + ".txt"
    open(lst,"w").write("".join(f"file {shlex.quote(p)}\n" for p in paths))
    run(["ffmpeg","-y","-f","concat","-safe","0","-i",lst,"-c","copy", dst])

BOX_DEFAULT = "0x000000@0.75"

def main():
    a = sys.argv[1:]
    def opt(name, default=None, flag=False):
        if name not in a: return default
        i = a.index(name)
        if flag: a.pop(i); return True
        v = a[i+1]; del a[i:i+2]; return v
    burn = opt("--burn", False, flag=True)
    stitch_only = opt("--stitch-only", False, flag=True)
    pad = float(opt("--pad", 0.0)); font = opt("--font")
    box = opt("--box", BOX_DEFAULT)
    edl_path = opt("--edl"); out = opt("--out")
    parts = [p for p in a if not p.startswith("--")]
    if not parts or not out or (not edl_path and not stitch_only):
        sys.exit(__doc__)
    edl = json.load(open(edl_path)) if edl_path else {}
    vertical = edl.get("vertical", True)
    vf_base = "scale=1080:-2" if vertical else "scale=-2:1080"
    tmp = tempfile.mkdtemp()

    # 0. Stitch parts into one source timeline
    offsets = []; t = 0.0
    for p in parts:
        d = duration(p); offsets.append((p, t, t + d)); t += d
    if len(parts) == 1:
        src = parts[0]
    else:
        norm = []
        for i, p in enumerate(parts):
            n = os.path.join(tmp, f"part{i:02d}.mp4"); normalize(p, n, vf_base); norm.append(n)
        src = os.path.join(tmp, "source_joined.mp4"); concat(norm, src)
    src_dur = duration(src)
    print(f"SOURCE timeline ({len(parts)} part{'s' if len(parts)>1 else ''}, {fmt(src_dur)} total):")
    for p, s, e in offsets:
        print(f"  {os.path.basename(p):40s} {fmt(s)} -> {fmt(e)}")
    if stitch_only:
        os.replace(src, out) if len(parts) > 1 else run(["cp", src, out])
        print(f"Stitched source written to {out}. Scrub it and confirm the parts are in order.")
        return

    # 1. Segments with output times
    segs = []; t = 0.0
    for s in edl["segments"]:
        a0 = max(0.0, tc(s["in"]) - pad); b0 = min(src_dur, tc(s["out"]) + pad)
        if b0 <= a0: sys.exit(f"bad segment {s} (source is only {fmt(src_dur)})")
        segs.append({"in": a0, "out": b0, "o_in": t, "o_out": t + (b0 - a0)}); t += (b0 - a0)
    total = t

    # 2. Overlays SOURCE -> OUTPUT
    ovs = []
    for o in edl.get("overlays", []):
        st = tc(o["src"]); hit = None
        for s in segs:
            if s["in"] <= st < s["out"]:
                hit = s["o_in"] + (st - s["in"]); break
        ovs.append({"text": o["text"], "src": st, "out": hit, "hold": o.get("hold")})
    ovs_sorted = sorted([o for o in ovs if o["out"] is not None], key=lambda o: o["out"])
    for i, o in enumerate(ovs_sorted):
        o["end"] = (ovs_sorted[i+1]["out"] if i+1 < len(ovs_sorted) else total) \
                   if o["hold"] is None else min(total, o["out"] + o["hold"])

    # 3. Cut (re-encode, frame-accurate) and join
    cut_parts = []
    for i, s in enumerate(segs):
        p = os.path.join(tmp, f"seg{i:02d}.mp4"); cut_parts.append(p)
        run(["ffmpeg","-y","-ss",f"{s['in']:.3f}","-to",f"{s['out']:.3f}","-i",src,
             "-vf", vf_base+",fps=30,format=yuv420p", "-c:v","libx264","-preset","fast","-crf","18",
             "-c:a","aac","-b:a","192k","-ar","48000","-ac","2", p])
    joined = os.path.join(tmp, "joined.mp4"); concat(cut_parts, joined)

    # 4. Optional burn-in
    if burn and ovs_sorted:
        fontarg = f":fontfile={font}" if font else ""
        filters = []
        for o in ovs_sorted:
            txt = o["text"].replace("\\","\\\\").replace("'", "’").replace(":", "\\:")
            filters.append(
                f"drawtext=text='{txt}'{fontarg}:fontsize=64:fontcolor=white:"
                f"box=1:boxcolor={box}:boxborderw=22:x=(w-text_w)/2:y=h*0.78:"
                f"enable='between(t,{o['out']:.2f},{o['end']:.2f})'")
        run(["ffmpeg","-y","-i",joined,"-vf",",".join(filters),
             "-c:v","libx264","-preset","fast","-crf","18","-c:a","copy","-movflags","+faststart", out])
    else:
        os.replace(joined, out)

    # 5. Report
    real = duration(out)
    print(f"\nOUTPUT {out}  planned {fmt(total)}  actual {fmt(real)}")
    print("\n| # | Source | Output | dur |")
    for i, s in enumerate(segs, 1):
        print(f"| {i} | {fmt(s['in'])} -> {fmt(s['out'])} | {fmt(s['o_in'])} -> {fmt(s['o_out'])} | {s['out']-s['in']:.1f}s |")
    if ovs:
        print("\n| Overlay | Source | Output | End |")
        for o in ovs:
            if o["out"] is None: print(f"| {o['text']} | {fmt(o['src'])} | NOT IN CUT | |")
            else: print(f"| {o['text']} | {fmt(o['src'])} | {fmt(o['out'])} | {fmt(o['end'])} |")
    if abs(real - total) > 0.5:
        print(f"\nWARNING: actual runtime differs from plan by {real-total:+.1f}s. Check the last segment's out point.")

if __name__ == "__main__":
    main()
