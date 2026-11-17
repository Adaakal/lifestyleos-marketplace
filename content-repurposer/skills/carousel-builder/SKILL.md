---
name: carousel-builder
description: "Build a 6-slide-max carousel in your Canva template from a clip package, article or idea, where every slide stands alone. Use for any carousel, slide post or photo-mode request, and after content-reverse-engineer packages."
license: MIT
---

<!--
  SETUP: this skill reads two values the user fills in once.
  1. Canva carousel template (required)   2. Name for the byline (required)
  Voice comes from content-reverse-engineer's "Your Voice" section.
  Requires the Canva connector.
-->

# Carousel Builder

Turns one piece of content into a finished carousel in a Canva template. Runs on its own, or right after content-reverse-engineer has packaged a source, using that package's validated research. Never add a claim the package did not already validate. If a slide needs a new fact, check it first.

## ⚙️ Setup check (run before any work)

This skill needs a few details from the person using it. Their saved answers appear in the "Your ..." sections below.

A value is **missing** when it is empty, or when it still shows a raw `${user_config...}` token (that happens outside Claude Code, where the setup form does not exist). A "My setup (content-repurposer)" block in the conversation or project instructions counts as the saved answers and fills any missing value.

Before doing the work:
1. Look at the values this skill marks **required** (Canva template, byline name). If any is missing, stop and ask for all the missing ones in a single message, in plain words, with one example each. Do not guess and do not invent a value.
2. Values marked **optional** fall back to the stated default. Mention once which defaults are in use.
3. Use the answers for the rest of the conversation, then tell the person how to save them so they are not asked again:
   - **Claude app (claude.ai or desktop):** give them a filled "My setup (content-repurposer)" block, copy-ready, and tell them to paste it into their Project instructions.
   - **Claude Code:** run `/config`, find this plugin's rows, and fill them in. `/content-repurposer:setup` walks through it.

If the Canva connector is not connected, say so first. Nothing below works without it.

## The three non-negotiables

1. **6 slides maximum.** One hook slide plus up to five content slides. Fewer is fine. Never more.
2. **Every slide stands alone.** Someone who sees only that slide, shared on its own or screenshotted, must understand what is being talked about. Each slide names its subject (the company, study, policy or topic) and states one complete point. No "as we saw", no "this one", no pronoun that points back to an earlier slide.
3. **The hook slide is always the most optimal one, without being asked.** Answer-first, the search phrase someone would actually type, and a reason to swipe. Built every time.

## Standalone test (run on every slide before building)

Cover the other slides. Read this one. Ask:
- Does it say who or what this is about by name?
- Does it make one full point a stranger could repeat?
- Would it still make sense if it were the only slide someone saw?

If any answer is no, rewrite the body, not the title.

## Voice

Slide copy follows the "Your Voice" section of content-reverse-engineer, plus the positive positioning rule. Sentence case unless the template's style renders caps.

## ⚙️ Your Template (required)

Canva design to build from: `${user_config.canva_template_id}`, 1080x1350.

If that is missing, ask: "Which Canva design should I build your carousels from? Paste its link." Any 1080x1350 design with a hook page and content pages works.

**Always copy it first** with `copy-design`, then edit the copy. Never edit the original. Rename the copy `Carousel: <topic> (<platform>, <month year>)`.

The element map below is a worked example from a common minimalist carousel layout (a light ground, one ink color, a mix of light, display-caps and script type). Do not assume it matches. Run `read-design` on the creator's design and use the element map and limits it shows.

### Page 1, hook slide (example element map)
| Role | Template text | Limit that fits |
|---|---|---|
| Top label, light 42px | @reallygreatsite | ~36 chars; widen the box for long labels. Use it for subject + source + date |
| Line 1, light 110px | 5 simple | ~12 chars |
| Line 2, display caps 194px | Content | ~8 chars |
| Line 3, script 148px | Ideas | ~9 chars |
| Line 4 left, light 77px | to post on | ~13 chars |
| Pill text, bold 62px | social media | ~12 chars |

Read together, lines 1 to 4 plus the pill form the hook sentence. Example shape: label "Healthcare AI · AMA brief, Oct 2026" / "Who's liable" / "WHEN AI" / "is wrong?" / "AMA splits it" + pill "three ways".

### Pages 2 to 6, content slides (example)
- **Number** (script): 1 to 5.
- **Title** (display caps): a short label, about 12 characters per line, two lines max. The title can be a single word because the body carries the full point.
- **Body** (light, centered): up to 4 lines, about 38 to 40 characters per line, written with manual line breaks. Keep the last line short enough to clear any arrow button, and keep it above the bottom rule.
- Last slide: remove the swipe arrow, then add a small line for the byline and sources (`add_text`, then `format_text` in the ink color, small and centered).

## ⚙️ Your Byline (required)

Name on the last slide: `${user_config.creator_name}`.

If that is missing, ask what name goes on their content.

## Canva build steps

1. `copy-design` on your template.
2. `read-design` on the copy with `open_transaction: true` and `design_content` to get locator IDs (they change with each copy).
3. `edit-design` page by page with `replace_text`, `resize_element`, `position_element`. Check each returned thumbnail for wrapping, overlaps with rules or arrows, and any text in the wrong style.
4. Show the user the slides and get a yes before `finalize: commit`. Saving is permanent.
5. Export: Instagram as PNG pages at 1080x1350. LinkedIn as a PDF document upload. TikTok photo mode needs a 1080x1920 resize.

## Slide plan shape

- **Slide 1:** hook (subject, the answer, a swipe reason).
- **Slides 2 to 5:** one point each, ordered so the carousel builds, while each slide still stands alone.
- **Slide 6:** the creator's read on it, a genuine question as the CTA, byline, sources.

## Output

Deliver, in order:
1. The Canva design link and a one-line note on any slide that needed adjusting.
2. Slide copy as copy-ready blocks, one per slide, label on its own line above each block, so it can be pasted or edited anywhere.
3. One decided posting slot for the carousel, taken from the package's ship plan. Never a menu.

## Other templates

If the user names a different design or pastes a Canva link, resolve it, read its element map the same way, and follow these rules in that layout. The three non-negotiables do not change with the template.
