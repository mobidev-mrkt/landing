# Webinar page: AI SDLC on a Legacy Codebase

Recording page for the fireside chat "AI-Native Speed on a Legacy Codebase: How to Outpace Competitors with AI-Driven SDLC" (September 30, 2026).

**URL:** `https://mobidev.biz/webinar/ai-sdlc-on-legacy-software-codebase`

Built from the existing webinar template on mobidev.biz (`/webinar/how-ai-driven-development-gives-scaleups-the-edge-in-2026`), using the same theme blocks and class names. The doc's SEO/SAIO requirements needed three blocks the theme doesn't have yet. Those are added as new blocks with the `ais-` prefix.

Open `index.html` to view it. It pulls the theme CSS directly from mobidev.biz, so you need internet. No build step.

## Files

| File | What it is |
|---|---|
| `index.html` | Standalone preview: `<head>` with meta/OG/canonical, theme CSS, the page, the JS. Not for uploading to WP. |
| `wordpress/page-content.html` | Page body only. Paste into a Custom HTML block (or rebuild from theme blocks, see below). |
| `wordpress/ai-sdlc-webinar.css` | Styles for the new blocks only. Everything else comes from the theme. |
| `wordpress/ai-sdlc-webinar.js` | Click-to-load video, chapters → seek, HubSpot form, dataLayer events. |
| `wordpress/schema.jsonld.html` | JSON-LD: Event, VideoObject + Clip, FAQPage, Person. Goes in the `<head>`. |
| `TODO.md` | What's left before launch. **Read it first.** |

## Before this goes live

The full list is in `TODO.md`. Blockers: video ID, timecodes for chapters 6–14, HubSpot form ID for the Readiness Discovery, uploadDate/duration, OG image.

## Blocks on the page

| # | Block | Source | Note |
|---|---|---|---|
| 1 | Hero: H1, intro, proof bar, 2 buttons | theme `hero-webinar` | The template has a gated HubSpot form on the right. Here the video is open, so the hero is one column (`data-layout="single"`) |
| 2 | Video + chapters | **new** `ais-video` | YouTube loads on click. Chapters are links with `&t=`, and with JS they jump the player to the timecode |
| 3 | What You'll Take Away | theme `cards-icon` | Icons icon-1…4 from the existing template |
| 4 | Key Answers from the Webinar | **new** `ais-answers` | The main SAIO block: H3 question + a short answer AI can quote |
| — | Mid-page CTA | theme `cta` | Same as in the template |
| 5 | Speakers | theme `speakers` | 3 cards: 2 speakers + moderator |
| 6 | Moderator's Insight | theme `author-block` | **Text placeholder**, Helen writes it |
| 7 | This session is for you if… | theme `link-cards` | 3 personas, all lead to the form |
| 8 | FAQ | **new** `ais-faq` | `<details>`, 5 questions, same as FAQPage |
| 9 | Free AI SDLC Readiness Discovery | **new** `ais-discovery` | The page's single conversion action, a HubSpot form |

Left out on purpose: the `choose-cards` (Key Numbers) block from the template. Those numbers are already in the hero proof bar, and the doc doesn't ask for it.

Changes from the template that matter for SEO: the template puts the title and section headings in `<p>`, so those pages have no H1/H2. Here the title is `<h1>` and section headings are `<h2>` inside the same wrappers (`.hero-webinar__title *` and `.section-heading-rem *` in the theme style any tag, so it looks the same).

## Moving it into WordPress

Option A, fast: a page using the `webinar` template, one Custom HTML block with `page-content.html`. Enqueue `ai-sdlc-webinar.css` and `.js` (or paste them inline into the same block in `<style>`/`<script>`). Put the JSON-LD in the `<head>` through whatever field you already use.

Option B, the right way: build blocks 1, 3, 5, 6, 7 and the CTA from the existing Gutenberg theme blocks (Hero Single Webinar, Cards with Icon, Speakers, Author, Link Cards, CTA) using the text from `page-content.html`. Add blocks 2, 4, 8, 9 as Custom HTML. If blocks 2/4/8 are needed on other webinars, it's worth turning them into theme blocks.

Hero H1: the theme's Hero Single Webinar block outputs the title as `<p>`. For the H1, either change the block template or use the hero as Custom HTML.

HubSpot: the JS listens for the `hubspot:ready` event the theme already fires, and creates the form in `#discovery-form`. In the preview, HubSpot doesn't load (the ID isn't set), so the fallback button is shown.

## Design tokens

From the theme `:root`: `--font-inter` / `--font-open`, `--Black-for-Text #303B4E`, `--Button-Green-Send #01978C`, `--color-white-grey #F7F7F7`, `--Gray-for-small-text #697EA3`. Gradient `#12B292 → #2EB0F1` as in the theme's `cta` and `hero-webinar`.

## SEO / analytics / accessibility

- Title, description, canonical and OG come from the doc and are in the `<head>` of `index.html`. In WP they're set through Yoast.
- JSON-LD parses as valid JSON. Rich Results validation is only possible once the placeholders are filled.
- dataLayer events: `cta_click` (with `cta_label`), `video_play`, `chapter_click`, `discovery_form_view`, `discovery_form_start`, `discovery_form_submit`. **Not checked by hand in GTM.**
- Checked at 1440 and 375 px: no horizontal scroll, one H1. Contrast wasn't measured with a tool. Keyboard navigation wasn't checked by hand.
- Images from cloudfront didn't load in the sandbox preview (network restriction). They will on the site.
