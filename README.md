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

## Using it outside Claude Code

The packaging here is Claude Code's — `.claude-plugin/`, `marketplace.json`, and
`/plugin marketplace add` are its format, and no other tool reads them. The *payload* is
not: `SKILL.md` is ~5,200 words of plain-English instructions with no Claude-specific
syntax in the body, and the Clip Re-Timer is a standalone HTML file that needs no AI tool
at all.

Three ways to use it without installing the plugin:

**1. claude.ai or the Claude desktop app.** Upload `content-repurposer/skills/content-reverse-engineer/`
(SKILL.md plus its `assets/` folder) as a skill under Settings → Capabilities → Skills. It
loads on demand there the same way it does in Claude Code.

**2. Any other LLM.** Paste the body of `SKILL.md` — everything below the YAML
frontmatter — into a system prompt, a project's custom knowledge, or an uploaded file. The
frontmatter is a Claude-specific trigger mechanism and can be dropped. The
`## Universal Access Contexts` section is also Claude-specific and safe to delete.

**3. The Clip Re-Timer alone.** Open
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
