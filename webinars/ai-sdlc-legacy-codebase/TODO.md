# AI SDLC on a Legacy Codebase: open items before launch

Search the markup for `[` to find every placeholder. Each one below exists in the files, and each placeholder in the files is listed here.

## Blocking

- [ ] **YouTube video ID** `[VIDEO_ID]`: `page-content.html` (player, 14 chapter links) and `schema.jsonld.html` (thumbnail, embed, content URL, clips).
- [ ] **Timecodes for chapters 6–14** `[__:__]` / `[SEC]`: in the doc they are still `__:__`. Fill in the chapter list (`data-start` = seconds) and add a `Clip` for each one in `schema.jsonld.html`. Right now the schema has only 4 clips (0:00–14:58). The timecodes must match the YouTube description. If the waiting minutes get cut from the start of the recording, recalculate them in both places.
- [ ] **HubSpot form for the Readiness Discovery** `[HUBSPOT_FORM_ID]`: create the form (button text "Get my assessment") and put its ID in `data-form-id`. Portal `47062060` is already set, the same one the other webinars use. Until it's set, the block shows a "Get my assessment" button that goes to `/contact-us`, so the page can be published without it, but nothing gets tracked as a Discovery request.
- [ ] **VideoObject**: `uploadDate` `[YYYY-MM-DD]` and `duration` `[PT00H00M00S]`.
- [ ] **OG image** `[OG image URL]`: the doc says "TO ADD". Use alt from the doc: *AI-Native Speed on a Legacy Codebase: How to Outpace Competitors with AI-Driven SDLC*. The same image also goes in `Event.image`.

## Placeholders in the markup

- [ ] **Ievgen Zadorozhnyi**: photo (currently a grey silhouette with `[Photo: …]` alt) and LinkedIn `[LinkedIn URL: Ievgen Zadorozhnyi]`, which appears 2× in the markup and 1× in the schema. He has no page at mobidev.biz/our-team (404).
- [ ] **Helen Khailova-Horash**: LinkedIn for the schema `[LinkedIn URL: Helen Khailova-Horash]`. In the speakers block her name links to her author page, but the theme draws a LinkedIn icon next to the name. Either give it her LinkedIn or accept that.
- [ ] **Moderator's Insight** `[PLACEHOLDER: Helen's own 80–120 words…]`: the doc says "Пише Хелен?". This is a quote from a real person, so we don't generate it. Either Helen writes it, or the `author-block` section gets deleted.
- [ ] Remove the `ais-placeholder` class (red dashed outline) once the content is real.

## Claims to confirm

- [ ] **"120+ legacy projects modernized"** (hero). I couldn't find a public source on mobidev.biz. 65+ AI & ML products and 9.1 NPS already appear on other webinar pages.
- [ ] **"81% less delivery effort … 12-month AI SDLC transformation"**: the guide doesn't have this number. Is there a published case study to link from the "A real modernization case" card? Without a link, the blind judge counts it as unconfirmed proof.
- [ ] **30–40% / up to 50% / ~50% dead code / 15 roles**: these come from the speakers on air. Leave them as is, but they should match the recording word for word.
- [ ] **Speaker bios** (12+ and 13+ years, wording): confirm with Serhii and Ievgen.
- [ ] **Chapter 2 title changed**: in the doc it's "What is AI SDLC? AI in all five stages, not just coding". On the page and in the schema it's "…AI in all five stages of the lifecycle". The "not just X" construction counts as a hard fail in the page-builder skill. **Make the YouTube description match**, or revert the doc wording in both places.
- [ ] **FAQPage**: the doc mentions "6 questions from the FAQ", but the FAQ itself has 5. The schema has 5, exactly matching the page. If a 6th question is needed, add it to both.

## SEO / site placement

- [ ] In Yoast: Title, Meta description, OG title/description as in the doc (already in the `<head>` of `index.html`, just copy them).
- [ ] Inbound links: the card in /webinars (automatic), plus manual links from the blog post `how-to-use-ai-to-modernize-software-product`, from `/services/application-modernization`, and from the webinar `how-ai-driven-development-gives-scaleups-the-edge-in-2026`.
- [ ] After publishing: test in Rich Results Test (Event, VideoObject, FAQPage) and submit the URL in Search Console. Review at 30 and 90 days.

## Nice to have

- [ ] Describe the Readiness Discovery in more detail: format (call / written report), how long it takes, what's needed from the client, what's not included. The blind judge took the most points off "Offer clarity" for exactly this. I didn't make it up because the doc doesn't have it.
- [ ] A client quote or a short case block with a link, instead of only the 81% card.
- [ ] Check in GTM that the events fire: `cta_click`, `video_play`, `chapter_click`, `discovery_form_view`, `discovery_form_start`, `discovery_form_submit`.
