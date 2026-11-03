# AI SDLC Readiness Discovery landing: TODO before launch

Page: `ai-sdlc-discovery.html` (assets in `ai-sdlc-discovery/`). Built with page-builder, Landing page kit
(Service Page Kit without navigation, one action). Blind judge: **gate not taken, 61/85, no hard fails;
weakest axis = Technical layer.** Points are lost on the inputs below, not on copy.

## Blockers
- [ ] **Final URL** for the page, then add `<link rel="canonical">` with it and put that URL into the Shorts 01–05
      descriptions instead of `[LINK]`.
- [ ] **Form backend.** The form posts to Netlify Forms (`name="ai-sdlc-discovery"`), as `index.html` does. If the page
      goes to WordPress/HubSpot, swap the `fetch('/')` call for that form endpoint. Test that `form_submit` reaches
      GTM/GA4 on a preview.
- [ ] **What happens after the form** (confirm and adjust the copy in step 1 and the thank-you text): the questionnaire,
      who reviews it, how soon the call is booked.

## Claims to confirm (the judge marked these as gaps; nothing was invented)
- [ ] Call length, and whether the client gets anything in writing after it.
- [ ] What the "readiness level" looks like (a scale? how many levels?).
- [ ] "Offer valid for 48 hours" from the webinar slide was left out on purpose: add it back only if it applies to this page.
- [ ] The call is with Helen Khailova-Horash (Senior Solutions Manager). Confirm the line
      "she brings MobiDev's delivery engineers into the conversation" matches how presales works (on the webinar she said she
      would bring them in "if our schedules allow").

## Content that would lift the score
- [ ] **Soft alternative:** set `CHECKLIST_URL` in the page script to the AI-Driven Modernization Readiness Checklist page;
      the "Not ready for a call?" line appears by itself.
- [ ] **One short case** with a number (e.g. the legacy retail operations platform from the webinar) for screen 2.
- [ ] **FAQ of 3–4 questions** with FAQPage schema, once the answers above are known.
- [ ] **Headshot:** Helen's photo is cropped from the webinar's contact slide (168 px); swap for the original file.

## Deliberately left out (3-screen limit, campaign page)
Navigation and breadcrumbs, related services, standards/stack, engagement models table (the offer is free).
The page is `noindex, follow` so it does not compete with service pages on mobidev.biz.

## Deviation from the design system
Eyebrow text on the grey section uses `#0B7A64` instead of `--green-dark` (#12B292 is 2.5:1 there, below 4.5:1).
