---
name: setup
description: "Walks a new user through the details content-repurposer needs to work for them: name, content pillars, voice, Canva carousel template, burn-in look and content database. Use on first install, when the user says \"set up\", \"get started\", \"configure\", \"change my pillars\" or \"change my voice\", or when another skill in this plugin reports a missing value."
license: MIT
---

# Setup

One short conversation that gets the plugin working for the person in front of you. Ask in plain words, one example per question, and never ask for something they already gave.

## What is set right now

| Detail | Needed for | Current value |
|---|---|---|
| Name on your content | Carousel byline, quotable lines | `${user_config.creator_name}` |
| Content pillars (3 to 6 themes) | Choosing and tagging clips | `${user_config.content_pillars}` |
| Voice notes | Every caption and post | `${user_config.voice_notes}` |
| Canva carousel template | Carousel Builder only | `${user_config.canva_template_id}` |
| Burned-in text box color | Clip Cutter only | `${user_config.burn_box_color}` |
| Burned-in text font | Clip Cutter only | `${user_config.burn_font}` |
| Content database | Syncing packages, optional | `${user_config.content_database}` |

A value is missing when it is empty or still shows a raw `${user_config...}` token.

## Steps

1. Show the person which details are set and which are missing. Leave out the token text. Say "not set yet".
2. Ask for the missing required ones first, together in one message: name and content pillars.
3. Ask which of the optional parts they plan to use (carousels, burned-in text, a content database). Only ask for the details behind the parts they say yes to.
4. For voice, offer the quick route: "Paste two or three posts you wrote and liked, and I'll describe the voice back to you for a yes or no." Write the voice notes from their posts, not from a generic creator voice.
5. For the Canva template, take a pasted link, confirm the design is 1080x1350 with `read-design` if the Canva connector is connected, and say plainly if the connector is missing.
6. Read the full set back and get a yes.

## Saving the answers

Answers only last for this conversation unless they are saved. End by telling the person the one that applies to them:

- **Claude Code:** run `/config` and fill in the content-repurposer rows with the values below. They also appear in the form shown when the plugin is enabled.
- **claude.ai or the desktop app:** paste the "My setup" block into the project's instructions. The skills in this plugin read it from there.

Always finish with the filled block, copy-ready:

```
My setup (content-repurposer)
Name: 
Content pillars: 
Voice: 
Canva carousel template: 
Burned-in text box color: 
Burned-in text font: 
Content database: 
```

Fill every line. Write "not used" for parts they skipped, so no later skill asks again.

## Rules

- Never invent a value to get past a blank.
- Never ask for passwords, API keys or account logins. Connectors handle sign-in.
- If a "My setup" block is already in the conversation or project instructions, treat it as the saved answers and only ask about lines that are blank.
