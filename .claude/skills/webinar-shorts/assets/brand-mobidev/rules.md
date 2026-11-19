# Brand design rules: MobiDev

> Profile: `brand.json` next to this file. Source: MobiDev Brand Book 2026 (Google Drive folder
> `1V91AS2daFVsoZZ1M6gJ-vX718yaOsaqo`: `Brand Book 2026 Design Guidlines.fig`, `Colors.jpg`, `Typography.jpg`,
> backgrounds and banners). The agent reads this file before graphics (steps 7–8); revisions are appended with
> `brand.py rule mobidev "..."`.

## Colors (Brand Book 2026): four colors, nothing else
| Color | HEX | Use in Shorts |
|---|---|---|
| Main Black | #222222 | backgrounds, the strip under the window, plates of tags and CTA backgrounds |
| Main White | #FFFFFF | headings, lists, secondary text, text on green or coral plates |
| Accent Green | #4AD57B | the highlighted word, the marker plate of the spoken item, CTA button, counters, progress bars |
| Coral | #DE7356 | only for a problem, a mistake, a risk, "before": the strike-through in `contrast`, the "wrong way" item |
- One accent per moment: green for the answer or the gain, coral for the problem. Never both on one word.
- Green text on white is not allowed (contrast < 3): green goes as a plate with #222222 text, or as text on #222222.
- No gradients, glows, particles or "tech" backgrounds: flat black, white, green, coral. (The old #2EB0F1 → #12B292
  gradient and the #F7F7F7 grey are not in the 2026 book: do not use them.)

## Typography (Brand Book 2026)
| Level | Font | Weight | Book size (1080-wide canvas) | In Shorts |
|---|---|---|---|---|
| H1 | Inter | Black 900 | 160 px | stat numbers, the 1-word punch of a `hook stack` |
| H2 | Open Sans | Bold 700 | 80 px | hook lines, scene titles, CTA line 1 |
| H3 | Inter | Medium 500 | 48 px | list items, quote lines, labels above scenes |
| H4 | Open Sans | SemiBold 600 | 32 px (never smaller than 40 px in video) | captions, "NAME · ROLE", CTA clarifier |
- Subtitles: Open Sans SemiBold/Bold, white on the #222222 strip, the spoken word highlighted green ("Accent").
- Fonts are local woff2 (`assets/fonts/`, `source: local`): the container's browser cannot reach Google Fonts.

## On-screen style
- Video style "Brand", subtitles "Accent", scene tone `feature` (slide-in cards) for every scene; `cinematic` (scale-in) only for a quote. The expert tone allows calm, feature, cinematic, deadpan: no punchy or hype.
- Plates: square-ish corners (radius ≤ 12 px), flat fill, no drop shadows heavier than a 20% black blur.
- Logo: only on the end card (white logo on #222222).
- Speaker window: the Zoom crop on #222222, as in Webinar 13.

## Motion (popups and animated elements)
- Something moves on screen at least every 8–10 s: a popup card, a list item, a counter, a strike-through.
- Popups slide in 60 px from the side or rise from below (tone `feature`), land on the spoken word, leave on a fade.
- Numbers count up (`stat`), lists build item by item on their words, "before → after" strikes the old word in coral.
- No bouncing, shaking, spinning, emoji, stickers or memes; the brand tone is "expert".

## Voice and bans
- Expert, calm, specific. Claims, names and numbers only from the speech.
- No hype words ("revolutionary", "game-changing"), no emoji in on-screen text.

## Rules from revisions
<!-- revisions: brand.py rule adds dated rules at the end of this section; the heading may be in any language -->
