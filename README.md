# LifestyleOS Marketplace

Content and lifestyle-operations skills for Claude. They turn raw material into
research-validated, platform-ready output, and they ask you for what they need the first
time you use them.

## Install

### In the Claude app (claude.ai or desktop). Start here.

No code and no terminal.

1. In Claude, open **Plugins** in the left sidebar.
2. Click **Add**, then **Add marketplace**, then **Add from a repository**.
3. Type `Adaakal/lifestyleos-marketplace`, pick it from the list, and click **Sync**.
4. Open **Content Repurposer (Marketplace)** in the list and click **Add**.
5. Start a chat and hand it something: "reverse engineer this video into posts" with a
   link, a transcript or a file.

The first time it runs, the skill asks for the few details it needs (your content pillars,
and your voice if you want one). It then gives you a filled "My setup" block. Paste that
into a Project's instructions and it won't ask again.

Every plugin from this repo is listed with **(Marketplace)** in its name, so you can tell
it apart from anything of your own with a similar name.

Prefer single skills? The [`downloads/`](downloads/) folder has one ZIP per skill that you
can upload on its own.

### In Claude Code

```
/plugin marketplace add https://github.com/Adaakal/lifestyleos-marketplace
/plugin install content-repurposer@lifestyleos-marketplace
```

Enabling the plugin opens a short form for the same details. Change them later with
`/config`.

## Plugins

### content-repurposer

Turn one recording into a stack of **research-validated, platform-ready clip packages.**
Feed it a video, transcript, or a pasted URL and it finds the standalone moments worth
posting, then hands back fully-drafted, paste-ready copy native to each platform —
TikTok, Instagram Reels, YouTube Shorts, LinkedIn, Substack, and beehiiv — with SEO/AEO/GEO
optimization and recut-safe timecodes.

- **Clip extraction** — mines a long video/transcript for each standalone insight and packages each separately.
- **Native multi-platform copy** — real, paste-ready posts per platform, not a "should I post here?" table.
- **SEO / AEO / GEO** — every field is engineered to be found by search bars, answer engines, and generative engines.
- **Deep research validation** — fact-checks stats, studies, and product/tech claims before writing copy.
- **Recut-safe timecodes** — every timed clip ships an edit decision list (EDL) that separates *source* time from *output* time, so edit notes survive recuts. Includes an offline **Clip Re-Timer** calculator (`content-repurposer/skills/content-reverse-engineer/assets/clip-retimer.html`).

- **Clip Cutter** — renders the package's EDL into a finished MP4. Stitches a recording uploaded in parts, snaps cut points to silence edges, recomputes the overlay map from the real cut, and can burn overlays in for LinkedIn and Substack. Ships `clipcut.py` (needs ffmpeg).
- **Carousel Builder** — builds a 6-slide-max carousel in your Canva template where every slide stands alone, with the hook slide always built answer-first. Needs the Canva connector.

In the Claude app, just describe what you have ("reverse engineer this video into posts:
<url>", "cut clip 2", "make this a carousel") and the right skill picks it up. In Claude
Code you can also call each one by name:

```
/content-repurposer:content-reverse-engineer
/content-repurposer:clip-cutter
/content-repurposer:carousel-builder
/content-repurposer:setup
```

**It asks for what it needs.** Nothing in the skills is hard-coded to one creator, and you
never have to open a file to make it yours.

- **In the Claude app,** just start using a skill. If a required detail is missing it asks
  once, in plain words, then hands you a filled "My setup" block to paste into your
  Project instructions so it never asks again. Saying "set up content repurposer" runs the
  full walkthrough if you uploaded the setup skill.
- **In Claude Code,** enabling the plugin opens a short form: your name, your content
  pillars, your voice, and (only if you use them) a Canva carousel template, a burn-in box
  color and font, and a content database. Change any of them later with `/config`.

| Detail | Required? | Used by |
|---|---|---|
| Your name | Yes | Carousel byline |
| Content pillars | Yes | Choosing and tagging clips |
| Voice | No, a default voice ships | Every caption and post |
| Canva carousel template | Only for carousels | Carousel Builder |
| Burn-in box color and font | No, a neutral default ships | Clip Cutter |
| Content database | No | Optional sync |

## Using it without Claude

The skills are plain-English instructions, and the Clip Re-Timer is a standalone HTML file
that needs no AI tool at all.

**Any other LLM.** Paste the body of `SKILL.md` — everything below the YAML
frontmatter — into a system prompt, a project's custom knowledge, or an uploaded file. The
frontmatter is a Claude-specific trigger mechanism and can be dropped. The
`## Universal Access Contexts` section is also Claude-specific and safe to delete.

**The Clip Re-Timer alone.** Open
`content-repurposer/skills/content-reverse-engineer/assets/clip-retimer.html` in any
browser. It is fully offline and makes no network requests. If all you want is edit notes
that survive a recut, you never have to touch an AI tool.

### Two honest caveats

**Research validation needs web search.** Fact-checking claims before writing copy is one
of the seven core capabilities, and it's the one separating this from a caption generator.
On a model without search, that step can't run — the skill is written to say so and
proceed with a caveat rather than fake it, but you lose the validation.

**It's a large prompt: ~12k tokens when it fires.** In Claude Code and on claude.ai only
the ~370-token description sits in context; the full instructions load only when the skill
actually triggers. Pasted into a system prompt elsewhere, there's no such gating — you pay
the full ~12k on every single turn, whether or not you're repurposing anything. Load it
into a dedicated project or conversation rather than your global instructions.

## Repo layout

```
lifestyleos-marketplace/
├── .claude-plugin/marketplace.json   ← the marketplace manifest
├── content-repurposer/               ← a plugin
│   ├── .claude-plugin/plugin.json
│   └── skills/
│       ├── content-reverse-engineer/
│       ├── clip-cutter/              ← SKILL.md + scripts/clipcut.py
│       ├── carousel-builder/
│       └── setup/                    ← first-run questions
├── downloads/                        ← ready-to-upload skill ZIPs for the Claude app
├── scripts/build-zips.sh             ← rebuilds downloads/ from the skill folders
├── artifacts/                        ← shared non-plugin assets
├── NAMING.md                         ← naming conventions
└── LICENSE
```

Adding another plugin means dropping a folder alongside `content-repurposer/` and adding
one entry to `.claude-plugin/marketplace.json`. Everything ships from this one repo, so
there is still only one URL to hand out.

## License

MIT — see `LICENSE`. Free to use, fork, and adapt.
