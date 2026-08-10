# LifestyleOS Marketplace

A Claude Code marketplace of content and lifestyle-operations plugins — tools for turning
raw material into research-validated, platform-ready output.

## Install

In Claude Code:

```
/plugin marketplace add https://github.com/Adaakal/lifestyleos-marketplace
/plugin install content-repurposer@lifestyleos-marketplace
```

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

Invoke it directly:

```
/content-repurposer:content-reverse-engineer
```

Or just describe a piece of content ("reverse engineer this video into posts: <url>") and it triggers on its own.

**This plugin is a generic, customizable template.** It ships with placeholder content
pillars and a default voice; you plug in your own. Open
`content-repurposer/skills/content-reverse-engineer/SKILL.md` and edit the three clearly
marked spots:

1. **Your Content Pillars** — the themes you post about, used to decide which clips are worth cutting and how to tag them.
2. **Your Voice** — how your copy should sound, so drafts come out in your voice.
3. **Content-database fields** (optional) — match the sync block to your own Notion/Airtable/sheet if you run a content pipeline.

## Repo layout

```
lifestyleos-marketplace/
├── .claude-plugin/marketplace.json   ← the marketplace manifest
├── content-repurposer/               ← a plugin
│   ├── .claude-plugin/plugin.json
│   └── skills/content-reverse-engineer/
├── artifacts/                        ← shared non-plugin assets
├── NAMING.md                         ← naming conventions
└── LICENSE
```

Adding another plugin means dropping a folder alongside `content-repurposer/` and adding
one entry to `.claude-plugin/marketplace.json`. Everything ships from this one repo, so
there is still only one URL to hand out.

## License

MIT — see `LICENSE`. Free to use, fork, and adapt.
