# Naming conventions

Two trees, one rule each.

```
Desktop/Claude/
├── SKILLs/               ← personal only. Never published.
└── SKILLs_Marketplace/   ← everything shared or published.
```

If a thing exists in both trees, the shared copy is the one that gets disambiguated.

## Where a prefix is needed — and where it isn't

**Claude Code plugin skills: no prefix.** Plugin skills are already namespaced by their
plugin, so two skills can share a name without colliding:

```
lifestyleos-content:content-reverse-engineer     ← personal (SKILLs/lifestyleos-personal)
content-repurposer:content-reverse-engineer      ← shared   (SKILLs_Marketplace)
```

Adding `marketplace-` to the skill folder would make the public one read as
`content-repurposer:marketplace-content-reverse-engineer` for anyone who installs it —
noise that means nothing outside this machine. So skill folder names stay clean.

**claude.ai and the Claude desktop app: prefix required.** Account skills there are a flat,
unnamespaced list. Two entries named `content-reverse-engineer` genuinely collide and there
is nothing to tell them apart. So when uploading a shared version to claude.ai, name it:

```
marketplace-content-reverse-engineer
```

and leave the personal upload as `content-reverse-engineer`.

**Marketplace names must be globally unique** in Claude Code — that registry is flat too.
Hence:

| Tree | Marketplace name | Path |
|---|---|---|
| Shared | `lifestyleos-marketplace` | `SKILLs_Marketplace/lifestyleos-marketplace` |
| Personal | `lifestyleos-personal` | `SKILLs/lifestyleos-personal` |

## Adding a new shared plugin

1. Create `SKILLs_Marketplace/lifestyleos-marketplace/<plugin-name>/`
2. Add `.claude-plugin/plugin.json` inside it
3. Add one entry to `.claude-plugin/marketplace.json`
4. `claude plugin install <plugin-name>@lifestyleos-marketplace`

No new repo, no new marketplace, no new URL to hand out.

## After editing any plugin source

Installed plugins run from a **snapshot copy** in
`~/.claude/plugins/cache/<marketplace>/<plugin>/<version>/`, not from these folders.
Editing a file here changes nothing until you refresh that cache:

```
claude plugin uninstall <plugin>@<marketplace>
claude plugin install   <plugin>@<marketplace>
```

Bump `version` in `plugin.json` when the content meaningfully changes, so the cache
directory name tells you which snapshot is live.

## If these folders ever move

Directory marketplaces are registered by **absolute path**. Moving a folder leaves a
dangling pointer that fails silently — the installed plugin keeps running from cache while
updates stop working. After any move:

```
claude plugin marketplace remove <name>
claude plugin marketplace add    <new/absolute/path>
claude plugin install <plugin>@<name>
```
