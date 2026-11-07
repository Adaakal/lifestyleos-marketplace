---
name: clip-cutter
description: "Cuts, reorders, and joins attached video into a finished MP4 from a content-reverse-engineer EDL (source in/out segments + overlays). Accepts one video or several smaller parts that make up one recording, stitches them into one source timeline, tightens cut points against the audio, verifies runtime, and returns the file plus a corrected overlay map. Triggers on: a video (or video parts) attached with a clip package or EDL, \"cut this\", \"trim the video\", \"build the cut\", \"render clip N\", \"make the MP4\", \"stitch these parts\", \"burn in the overlays\"."
license: MIT
---

<!--
  CUSTOMIZE THIS SKILL: 1 spot makes it yours.
  "Your Burn-In Style" (below) sets the overlay box color and font for burned-in text.
  Everything else is a general-purpose cutting engine.
-->

# Clip Cutter

You turn a content-reverse-engineer edit decision list into an actual video file. The user attaches the source recording, in one file or in several smaller parts (chat upload limits mean a long recording often arrives split), names the package or clip, and you hand back the rendered MP4 with the overlay map recomputed from the real cut. The EDL stays the source of truth: segments and overlays are written in SOURCE time, and output time is computed by the script, never typed by hand.

Requires `ffmpeg` and `ffprobe` (6.x tested) and Python 3.

## Inputs

1. One video file, or several parts of one recording (attached to the chat, staged from a connected folder, or already in the workspace). Parts are joined in the order the user gives them. When the order is not stated, sort by the number in the filename and confirm the order in the reply.
2. An EDL. Take it from the clip package file (the "Edit Decision List" section) or from the chat. If only a package exists, convert its EDL table and overlay map into the JSON below yourself. SOURCE timecodes refer to the full recording, the same timeline the caption editor showed, so parts must be stitched before any cutting.
3. Optional: which overlays to burn in, and a target platform. Default policy: TikTok, Reels and Shorts get NO burned-in text (creators add text natively in-app so it stays editable). LinkedIn and Substack uploads get overlays burned in, because those uploaders have no text tool.

## Workflow

```
1. PROBE     ffprobe every file: duration, resolution, fps, audio present. Flag anything off
             (silent track, landscape when vertical was expected, a part whose resolution
             differs from the others, total runtime shorter than the EDL's last out point).
2. STITCH    Several parts: run clipcut.py --stitch-only first. It prints each part's offset on
             the joined timeline. Compare the total against the caption editor's last cue.
             If the total comes up short, a part is missing or duplicated; ask before cutting.
             One file: skip this step.
3. EDL->JSON Write edl.json from the package. Segments in playback order, SOURCE in/out.
             Overlays with SOURCE anchors. Set "vertical": false only for landscape sources.
4. FIRST CUT Run clipcut.py with --pad 0.15 (caption-cue starts are upper bounds, so cut a
             beat wide on the first pass). Read the report.
5. TIGHTEN   For each cut point, run silencedetect on the stitched source around it (+/-1.5s)
             and move the in/out to the nearest silence edge: in = end of the silence before
             the first word, out = start of the silence after the last word. Rerun without
             --pad. If speech runs continuously through a cut point, keep the caption time
             and say so.
6. VERIFY    Compare planned vs actual runtime (the script warns above 0.5s). Pull 3-4
             frames at the seams with ffmpeg select+tile and read the image: confirm the
             order is right and no wrong-frame flash at a join. A listen check is not
             possible, so state that seams were checked visually and by silence edges only.
7. DELIVER   Send the MP4 to the user. Paste the script's final EDL + overlay table into the
             reply. If the real runtime differs from the package, update the package file's
             EDL and overlay map to the new numbers and resend it, so any content database
             synced from it gets the corrected version.
```

## Rules

- Never author an output timecode. The script computes them; you report them.
- Never stream-copy cuts. Stream copy snaps to keyframes and drifts by up to a second; the script re-encodes each part and each segment for frame-accurate joins.
- Part boundaries are not cut points. A segment may span two parts; the script handles it because it cuts the stitched file, not the parts.
- Keep the original files untouched. Outputs are named from the package: `NN_kebab-title.mp4`, and `NN_kebab-title_burned.mp4` when overlays are burned in.
- If a segment's out point is an assumption in the package ("end time assumed"), say which one and confirm it from ffprobe/silencedetect before the final render.
- If a part fails to upload, ask for that part again rather than cutting around the gap.
- Report one decided result, not a menu of renders. Follow the voice rules in content-reverse-engineer's "Your Voice" section for any copy in the reply.

## ⚙️ Your Burn-In Style — CUSTOMIZE THIS

Default: white text on a black box at 75% opacity (`--box 0x000000@0.75`), centered, lower third, DejaVu Sans if no brand font is on disk (`fc-list | grep -i dejavu`). Replace with your brand box color (`--box 0xRRGGBB@0.85`) and a font path (`--font /path/to/font.ttf`). Ask before installing any new font.

## The script

`scripts/clipcut.py` in this skill folder. Copy it into the working directory before the first run. Tested on ffmpeg 6.1: a 75s 1080x1920 source split into three uneven parts stitched back to within one frame of the original timeline, and a 58s reorder cut matched the single-file result. A one-minute cut renders in about a minute; stitching adds roughly real-time per part.

## Useful commands

Probe:
```
ffprobe -v error -show_entries format=duration:stream=width,height,r_frame_rate,codec_type -of default=nw=1 FILE.mp4
```

Stitch only (confirm part order and offsets before cutting):
```
python3 clipcut.py --stitch-only --out source_joined.mp4 part1.mp4 part2.mp4 part3.mp4
```

Cut and burn in:
```
python3 clipcut.py --edl edl.json --out 01_my-clip_burned.mp4 --burn --box 0x000000@0.75 source.mp4
```

Silence edges around a cut point on the stitched source (example: 1:05 = 65s):
```
ffmpeg -ss 63.5 -t 3 -i source_joined.mp4 -af silencedetect=n=-35dB:d=0.25 -f null - 2>&1 | grep silence_
```
Add 63.5 to every reported time to get source time.

Seam frames for a visual check (frame numbers = seconds x 30):
```
ffmpeg -y -i OUT.mp4 -vf "select='eq(n,0)+eq(n,240)+eq(n,900)',scale=270:-1,tile=3x1" -frames:v 1 seams.png
```

## edl.json format

```json
{
  "segments": [ {"in": "1:05", "out": "1:13"}, {"in": "0:15", "out": "1:05"} ],
  "overlays": [
    {"text": "TALK IT. DON'T TYPE IT.", "src": "1:05"},
    {"text": "1 · VOICE MODE ON", "src": "0:19"},
    {"text": "4 · IT WRITES THE DETAILED PROMPT", "src": "0:55", "hold": 9}
  ],
  "vertical": true
}
```
An overlay with no `hold` stays up until the next overlay starts. An overlay whose source anchor is not inside any segment is reported as NOT IN CUT rather than silently dropped.

## Handoff

End every run with: the MP4, the part offsets if the source was stitched, the final EDL and overlay table (real numbers), which cut points were snapped to silence and which kept the caption time, and whether the package file was updated. If the user is adding text natively in TikTok, restate the overlay start/end times as the numbers to type into the text tool.
