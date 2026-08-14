# Vibecode Product Audit — landing page

Static, dependency-free landing page for the **AI Code Rescue / Vibe Coding Fix** offer, plus Terms of Service and Privacy Policy pages. Built to be finalised by your team and moved into WordPress.

Open `index.html` in any browser to see it. No build step, no npm, no framework.

---

## What's in the box

| File | What it is |
|---|---|
| `index.html` | The landing page. Single file: markup + CSS + JS inline. |
| `terms.html` | Terms of Service (text as supplied, unchanged). |
| `privacy.html` | Privacy Policy (text as supplied, unchanged). |
| `assets/mobidev-logo.png` | Wordmark, 320×80, transparent. Used in header and footer. |
| `assets/favicon.png`, `assets/apple-touch-icon.png` | Icons cut from the wordmark. |
| `assets/clients/*.webp` | 14 client logos for the marquee, taken from mobidev.biz. |
| `wordpress/` | The same page split for WordPress. See below. |
| `sync-preview.sh` | Local dev helper. Not needed for production. |

---

## Before this page goes live

These are the only blockers. Everything else works as is.

1. **Stripe payment links.** Open `index.html`, find `CHECKOUT_LINKS` near the bottom, paste one Payment Link per tier:
   ```js
   var CHECKOUT_LINKS = {
     tier1: '', // $399   Vibecode Product Audit
     tier2: '', // $899   Audit + Single Bug Fix
     tier3: ''  // $1,099 Audit + Two Fixes + Action Plan
   };
   ```
   While a link is empty the button falls back to the intake form, so the page is safe to publish before Stripe is ready.
2. **Success story** — the block marked `[PLACEHOLDER]` holds an invented story and empty metrics. Replace with a real case, or delete the section and its `Success story` nav link.
3. **Who reads your code** — three cards with `[Engineer name]` / `[Role]` placeholders and silhouette avatars. Add real people and photos, or delete the section.
4. **Sample report** — the document mock in "What you get" is illustrative and says so on the card. Swap for a real anonymised report page when one exists.
5. **Legal page links.** In WordPress the footer links must point at the real permalinks, not `terms.html` / `privacy.html`.
6. **Form destination.** See "Form" below. Right now the form posts nowhere.

Prices on the page are **$399 / $899 / $1,099** with 1 / 2 / 3 business day delivery. An earlier draft of the copy doc used $499 / $999 / $1,199 — confirm which is correct before launch.

---

## Design tokens

Taken from the MobiDev brand guideline (Text Style + Color Palette sheets).

```
--black       #222222   main text, dark sections
--green       #4AD57B   accent, primary buttons
--green-dark  #12B292   links, hover, gradient end
--blue        #2EB0F1   gradient start
--sec-white   #F7F7F7   section backgrounds
--white       #FFFFFF
--line        #E4E6E5   borders
--muted       #5A5C5B   secondary text
```

Type: **Inter** (display: 900/700) + **Open Sans** (body). H1 48 / H2 40 / H3 24 / body 16, scaled down with `clamp()` on small screens. The blue→green gradient is used only for highlights (hero accent words, badges, metric numbers), per the guideline.

Both files are self-contained: all CSS lives in one `<style>` block at the top, all JS in one `<script>` block at the bottom, in source order matching the page.

---

## Page structure

1. Sticky header with the wordmark and anchor nav
2. Hero (fits one screen: `min-height: calc(100svh - 72px)`)
3. Client logo marquee (infinite CSS scroll, pauses on hover)
4. The problem — three inbound messages, attributed by role, not by name
5. Your options — AI tool vs freelancer vs this audit (dark section)
6. How it works — four steps
7. What you get — report contents + document mock
8. Pricing — three packages, "not included" collapsibles, payment note, "not the right thing to buy" filter
9. Success story `[PLACEHOLDER]` + Clutch reviews widget
10. How we work — six guarantees
11. Who reads your code `[PLACEHOLDER]`
12. FAQ — five questions
13. Final CTA + intake form
14. Footer with legal links

---

## Moving it to WordPress

The `wordpress/` folder has the same page, split up:

| File | Use |
|---|---|
| `page-content.html` | Body markup only. Paste into a Gutenberg **Custom HTML** block or an Elementor **HTML** widget. |
| `vibecode-audit.css` | The stylesheet. |
| `vibecode-audit.js` | Checkout links, package preselect, scroll reveal. |
| `page-vibecode-audit.php` | Optional child-theme page template that enqueues the two files above. |

Steps that work with any theme:

1. Upload `assets/` (logo, icons, `clients/`) to the child theme, e.g. `/wp-content/themes/<child>/assets/vibecode/`, or to the media library.
2. In `page-content.html` and `vibecode-audit.css`, find-and-replace `assets/` with the real URL of that folder.
3. Copy `page-vibecode-audit.php` into the child theme root and pick the template on a new page. Or skip it, use a blank canvas template, and enqueue the CSS/JS yourself.
4. Paste `page-content.html` into the page.
5. Create two more pages for Terms and Privacy (content from `terms.html` / `privacy.html`) and point the footer links at them.

Two things to watch:

- **Class collisions.** The CSS uses short names (`.btn`, `.wrap`, `.step`, `.pain`). If the theme already defines any of them, wrap the whole markup in `<div class="vca">` and prefix the selectors, or the theme will bleed in.
- **The theme's own header and footer.** The page ships its own sticky header and footer. Either use a canvas/blank template, or delete the `<nav class="nav">` and `<footer>` blocks and let the theme provide them.

### Form

The form is plain HTML with `data-netlify` attributes left over from static hosting. In WordPress, replace the whole `<form>` element with your plugin's shortcode (WPForms, Gravity Forms, Contact Form 7) keeping these fields:

- Package (select: the three tiers + "Not sure yet")
- Name, work email
- Repo link or how the code will be shared
- What are you most stuck on (textarea)

Keep the line under the button: it links to Terms and Privacy, which is where the order consent lives.

### Clutch widget

The reviews block loads `https://widget.clutch.co/static/js/widget.js`. It renders nothing without network access and can be blocked by aggressive cookie/consent tooling — if the page has a consent banner, this script belongs in the "third party" category. Company id is `17222`; the reviews shown are pinned by id in `data-reviews`.

---

## Analytics, SEO, accessibility

- `<title>` and `<meta name="description">` are filled on all three pages. No Open Graph tags yet — add them when the final URL and share image exist.
- No analytics or pixels are installed. Nothing tracks the visitor and no cookies are set by the page itself. Add GA4/GTM where the client's consent setup requires.
- Contrast, focus order and alt text were checked. Animation (marquee, scroll reveal) is disabled under `prefers-reduced-motion: reduce`.
- Tested at 375, 768, 1280 and 1440 px. No horizontal scroll; the Clutch iframe scrolls inside its own box on narrow screens.

## Local preview

```bash
python3 -m http.server 4646
```

Then open http://localhost:4646. `sync-preview.sh` exists only because the dev machine's server could not read the Desktop folder directly; it is not part of the deliverable.
