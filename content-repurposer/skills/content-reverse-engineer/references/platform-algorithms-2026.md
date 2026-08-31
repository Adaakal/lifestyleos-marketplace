# Platform Algorithm Playbook — verified August 2026 (PERISHABLE)

This file is the deep-dive behind the "Platform Algorithm Priorities" digest in SKILL.md.
Read it when drafting Part B platform blocks, when advising the user on platform strategy, or
when a package decision hinges on *how a platform ranks content* rather than what the copy says.

**Perishability warning:** everything here describes ranking behavior as researched in
mid-2026. Algorithms shift monthly. Rule 10 in SKILL.md applies to every claim in this file —
before leaning hard on a specific tactic (especially in advice the user will build a habit
around), confirm it with a quick web search. Never present a tactic from this file as
evergreen truth.

---

## Instagram — connection signals over vanity metrics

Instagram has re-weighted away from likes, superficial comments, and hashtags toward signals
of direct human connection and immersion.

**Ranking signals, strongest first:**
1. **Sends per reach** — the DM/share airplane tap is the single most-weighted signal
   (confirmed publicly by Adam Mosseri). One DM share ≈ ~15 likes in ranking weight. It tells
   the system the content pulls real-world relationships onto the app.
2. **Saves by non-followers** — a stranger saving a post signals high "intent" value and
   breaks content out of follower-only distribution into the topic-driven recommendation
   engine (users now explicitly pick topics via the "Your Algorithm" dashboard).
3. **Retention on speech-driven video** — talking-head, conversational, "unedited-feeling"
   video with a human speaking in the first ~1.5 seconds outperforms polished
   music-over-b-roll. Polish has been commoditized by generative AI; raw human audio commands
   longer watch time and replays.

**What this means for drafting:**
- Engineer a **send trigger** into every Reel: one line or moment that makes a viewer forward
  it to a *specific person* ("this is so us", "you need this"). Name it in the IG block.
- Build **save-worthiness** for cold strangers: checklists, step-by-steps, named tools —
  reference material someone keeps. Carousels inherently over-index on saves.
- **Speak the keywords out loud.** Instagram indexes spoken audio via auto-captions, plus
  alt text and the caption, into search (including external search engines). Hashtags are
  functionally decorative for targeting — 3–5 is plenty; the caption keywords, spoken
  keywords, and the "Add Topic" selection do the real work.
- **Topical identity is judged on the last 9–12 posts.** Scattered pillars = dropped reach.
  When a clip bridges pillars, this is one more reason to commit to the dominant one.
- Favor cuts where the creator talks to camera over silent b-roll with trending audio.

## TikTok — commerce, length, and search

TikTok is prioritizing content that either keeps users in-app longer or generates direct
revenue.

**What it's boosting:**
1. **Shop-integrated content** — product links, live shopping, review roundups get an
   automatic distribution edge. (Only relevant when there's an actual product/affiliate —
   never bolt commerce onto a clip that doesn't carry it.)
2. **Longer and serial content** — 1–10min videos (including horizontal/landscape) are
   boosted; sub-15s clips are actively suppressed. Multi-part series and playlists that drive
   sequential watching get rewarded.
3. **Search-intent content (TikTok SEO)** — Gen Z/Millennials use TikTok as a search engine.
   Keyword-rich *spoken* words, in-video text, and descriptions targeting real queries give a
   clip shelf-life beyond the FYP cycle. "How-to" framing wins.
4. **Interactive formats** — stitch/duet bait, native video replies to comments, polls and
   debate-sparking CTAs count as "community depth."
5. **Feature-biased formats** — Photo Mode carousels (often out-reach video for the same
   idea), newly released native effects/filters, and clean HD/4K uploads get baseline boosts.

**What this means for drafting:**
- When the source supports it, propose the **60s+ cut as the TikTok primary**, not the
  tightest one. Note serial potential ("this is part 1 of a natural 3-parter").
- Put the target search phrase in the **spoken hook and on-screen text**, not just the caption.
- Make at least one CTA **interactive** (stitch/duet/reply prompt), not just "follow for more."
- When a clip's idea works as slides (a checklist, a framework), offer a **Photo Mode
  carousel variant** alongside the video block.

## YouTube (Shorts + long-form) — satisfaction over raw watch time

YouTube is re-engineering recommendations around *user satisfaction*, not pure watch time.

**Ranking signals:**
1. **Satisfaction surveys** — explicit "did you enjoy this?" feedback can override
   watch-time metrics.
2. **Return viewer velocity** — how fast past viewers come back for a new upload; this is
   what unlocks homepage impressions. Consistency and bingeable serialization feed it.
3. **Atypical CTR** — thumbnails/titles that appeal beyond the core audience. YouTube's
   native A/B thumbnail testing is favored — always give options to test.
4. **First-30-seconds retention** — no long intros, hook immediately (this skill's
   answer-first rule already enforces it).
5. **Multi-format ecosystems** — channels combining Shorts + long-form + podcasts, and
   platform-native features (chapters, cards, multi-language audio tracks), signal quality.

**What this means for drafting:**
- Ship **2 thumbnail-text options** per Short/video for native A/B testing.
- Name the **series/playlist** a Short belongs to; pinned comment can point to the next
  video in the chain ("next-video clicks from the same creator" is heavy-lifted).
- Long-form candidates flagged by this skill (see Edge Cases) are more valuable than they
  used to be — a Substack/YouTube deep-dive from an uncuttable idea feeds both platforms'
  current priorities.

## Substack — media-first hub, native video, paid conversion

Substack pivoted hard into video: a TikTok-style vertical media feed in the app, "For You"
discovery that surfaces content to strangers (not just followers), and a native TV app
(Apple TV / Google TV) positioned against YouTube/Patreon for premium long-form. Its
business model is a 10% cut of paid subscriptions, so **the algorithm favors content that
converts free viewers to paid** — over 80% of top-earning publications use video/audio.

**One-time publication setup (walk the user through this once, then reference it):**
- Settings → Site Design → Homepage layout → **Grid or Magazine** (media cards, not text links).
- Toggle the **Video/Podcast tab on** in top navigation so videos aggregate into a library.

**Per-post formatting rules:**
1. **Video at the absolute top of the post.** Substack reads the first asset to decide how
   the post displays in the app's media tabs. A video buried under paragraphs won't surface
   in the video feed.
2. **Upload natively, never embed.** Upload the high-bitrate `.mp4`/`.mov` directly;
   Substack's player scales for the TV apps, and native uploads are prioritized in discovery
   over YouTube embeds.
3. **Cut a 60–90s native clip** with Substack's built-in clipper from any long-form upload —
   these clips are what get pushed into the vertical discovery feed. Use the automated
   closed-captioning so the clip works with sound off.
4. **Custom 16:9 thumbnail (1920×1080)** with high-contrast, couch-readable text — never the
   auto freeze-frame.
5. **Treat the post body like a YouTube description** — bullet points, clear keywords —
   Substack's internal search indexes it.
6. **Paywall as a cliffhanger, not a wall.** For premium video: Paid Subscribers Only with a
   **2–3 minute free preview** that cuts off *right before the most valuable insight or
   demonstration*. The app prompts the viewer to subscribe mid-watch. Never fully hide a
   premium video; never let the preview end after the payoff.

**What this means for drafting:**
- The Substack block is **video-first**: video placement + native clip choice + thumbnail
  come before the essay scaffolding.
- The hybrid format wins: written analysis + native video at the top + (for paid posts) a
  Chat/Live tie-in — Substack rewards creators acting like an integrated media company,
  delivering email + audio + video in one interface.
- The 60–90s Substack clip can usually be the same cut as the TikTok/Reels edit — one EDL,
  one extra upload destination. Say so in the package when true.

---

## Cross-platform through-lines (the durable part)

Even when the specifics above rot, these have held across every platform's shift and are the
safest bets:

- **Shareability and save-worthiness are clip-selection criteria**, not caption garnish —
  pick moments people forward and keep, and every algorithm rewards it.
- **Spoken keywords are the new metadata.** Every platform transcribes audio and indexes it;
  what the creator *says* in the first lines matters more than any tag field.
- **Native beats embedded.** Every platform boosts its own upload/feature stack and
  demotes links out.
- **Serialization compounds.** Series, parts, and playlists feed return-viewer metrics
  everywhere.
- **Audio-off is the default viewing mode.** Burned-in captions/on-screen text are
  table stakes on every vertical feed.
