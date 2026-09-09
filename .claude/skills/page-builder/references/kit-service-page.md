# Service Page Kit

The page where traffic turns into an enquiry. The reader already knows what they need and is checking
three things: do you do this, what does it cost, and who actually performs the work.

The usual failure: three paragraphs about how leading the agency is, nothing concrete about scope,
silence on price, one "Contact us" at the bottom. The buyer gets no answer to any of their questions
and goes to read a competitor.

## Structure — 16 slots, top to bottom

**1. Breadcrumbs** — `Home → Services → [Service]`. Orientation for the reader, hierarchy for the crawler.

**2. H1** — formula: `[Service] for [who] — [outcome]`. One H1. Primary query in it and in the first
100 words.

**3. Hero** — one sentence on what this is and who it is for, the headline number beside it (years,
projects, geographies, typical turnaround), primary action visible without scrolling.

**4. Trust strip** — client logos or figures: how many projects in this service, in which markets,
which certifications. It sits here because the next thing the reader decides is whether to keep reading.

**5. Who this is for** — 3–5 symptoms in the buyer's own words, taken from calls. The reader must
recognise themselves within ten seconds.

**6. What's included — and what isn't** — the artifacts the client receives and can sign off:
models, drawing sets, reports, access, documentation. Nouns, not adjectives. Then the boundary: what
this service explicitly excludes. An honest boundary removes half the misunderstandings on the call
and builds more trust than any slogan.

**7. How we work** — the process by stage or week: what happens, who is involved on your side, what
is needed from the client and when. The buyer is purchasing predictability and this is where they see it.

**8. Engagement models and price** — the options (dedicated team, fixed scope, time and materials),
the starting figure, what moves the number. An empty price costs you the lead: a reader with no
reference point closes the tab. Minimum is a range or "from".

**9. Why us** — 3–4 points, each carrying proof: a figure, a certification, a named standard, a link
to a case. A point without proof gets deleted.

**10. Standards, stack, tools** — for technical services: codes, certifications, software, file
handover formats. For consulting: methodology and artifacts. This is what the technical evaluator
checks while the commercial one reads the price.

**11. Proof — cases from this service** — 2–3 case cards from this specific service, each with a
number and a link to the full case. Plus a pull quote.

**12. Who performs the work** — team or practice lead: photo, role, experience. For services this
carries more weight than for products, because people are what is being bought.

**13. FAQ** — real objections from calls: what it costs, how long it takes, what if the result doesn't
fit, who owns the IP, how NDAs are handled, how time zones work. Direct feed for AI search and
friction removal in one block.

**14. Final action + form** — one primary action, minimal fields, and an alternative for readers not
ready for a call: take the checklist, see a sample of work.

**15. Related services** — 3 cards. Keeps the reader inside the cluster and distributes internal weight.

**16. Hidden technical layer** — Service + FAQPage + BreadcrumbList schema, clean URL, canonical.

## Slots by category

| Category | Slots |
|---|---|
| **Offer clarity** | H1 formula · who this is for · what's included and what isn't · how we work · models and price |
| **Trust** | trust strip · why-us with proof · standards and certifications · cases from this service · who performs · quote |
| **Conversion** | hero action · inline actions · final form · soft alternative · related services |
| **Search & AI visibility** | breadcrumbs · single H1 · FAQ · Service/FAQ/Breadcrumb schema · clean URL |

## Intake questionnaire — delivery lead / founder

One 45–60 minute session should cover all 16 slots. Ask for numbers. "I can't say exactly" → ask for a range.

**A. Offer and boundary** — What do you call this service on a call? What does the client receive at
the end, listed as artifacts? What do clients often assume is included but isn't? Where does this
service end and the neighbouring one begin?

**B. Who it's for** — Ideal buyer: size, market, geography, decision-maker role? What symptoms do they
arrive with — verbatim phrases? Who do you *not* sell this to, and why?

**C. Process** — Stages from first call to handover, with durations? Who is involved at each stage?
What is needed from the client, and at which step? What most often causes slippage?

**D. Money** — Which engagement models? Starting figure? Typical project range? What moves the price
most? What can be published openly versus only said on a call?

**E. Differentiation** — Why do they choose you over a competitor or in-house — three reasons with
proof? Which standards, codes, certifications do you hold? What stack and handover formats? What do
you do differently, and how is that visible to the client?

**F. Proof** — Which 2–3 projects from this service can be shown, with numbers? Which clients can be
named openly, which anonymised? How many projects in this service overall, in which markets? Who is
the practice lead — name, role, years?

**G. Objections** — Top seven questions asked on calls about this service? What most often kills the
deal? What gets asked about IP, NDAs, time zones, staff substitution?

**H. Legal and media** — What cannot be published? Do you have client brand assets, team photos,
work screenshots?

## Writer SOP

1. **First sentence is about the client.** Who they are and what they get. "We are a leading team"
   moves to the end or gets cut.
2. **Language from calls.** Write in the words the buyer uses for their own problem. Internal jargon
   stays internal.
3. **Scope as nouns.** "Drawing set, clash report, updated model" — not "quality delivery".
4. **The boundary is mandatory.** The "what's not included" section saves hours on calls.
5. **Price always appears.** At least a floor or a range.
6. **Every why-us carries proof.** No figure, certification or case — the point goes.
7. **FAQ from real objections.** From calls and email, not invented.
8. **One primary action plus inline ones.** Read about the process → chance to see an example right there.
9. **Internal links:** 2–3 cases from this service, 2 related services, 1–2 articles.
10. **Mark visuals in the draft:** `[HERO]`, `[TRUST STRIP]`, `[PROCESS]`, `[MODELS TABLE]`,
    `[CASE CARD]`, `[TEAM]`, `[QUOTE]`.
11. **Run the humanisation pass** (`copy-humanisation.md`) as a separate step once the draft is
    finished, not while writing. Negative parallelism ("not X, but Y") and rule-of-three punch
    triads are hard fails at the blind judge, not style preferences.
12. **Fact-check** every number, name, certification and price against the delivery lead's answers
    before handover.

## Technical checklist — template, set once

**Schema** — Service (name, `provider`, `areaServed`, `serviceType`) · FAQPage on the FAQ block ·
BreadcrumbList on the breadcrumbs · Organization from the site template · `Offer` with `priceRange`
if a figure appears on the page.

**URL** — `/services/` → `/services/service-name/`. One service, one address. Campaign duplicates live
separately as landing pages, never as copies of the service page. Industry variations use
`/services/service/industry/` with their own text — copied text with one word swapped creates
cannibalisation. Latin slug, no parameters or numbers. Canonical set.

**Template and analytics** — sticky CTA on mobile · form with minimal fields, visible consent,
confirmation state · analytics events on form view, first input, submit, and phone/email clicks ·
"Related services" auto-selected by category · WebP, lazy-load, images under 200KB · indexable, in
sitemap, has inbound internal links.

## Designer brief

| Marker | What to produce |
|---|---|
| `[HERO]` | First screen: headline, one sentence, headline number, action button |
| `[TRUST STRIP]` | Row of logos or figures directly under the hero |
| `[PROCESS]` | Stage diagram with durations, readable on mobile |
| `[MODELS TABLE]` | Engagement models compared: when it fits, what's included, starting figure |
| `[CASE CARD]` | Case card with a number and a link to the full version |
| `[TEAM]` | Photo, role and experience of the practice lead |
| `[QUOTE]` | Client pull quote with photo or logo |

Client's design system, their colours and type. Real artifacts from projects rather than stock
imagery; blur data under NDA but keep the shape. Check the models table, process diagram and form on
a phone. Alt text on every visual.

## Pre-launch checklist

- [ ] H1 follows the formula: service + for whom + outcome
- [ ] Primary action visible without scrolling
- [ ] Trust strip filled with real data
- [ ] "What's included" plus the "what's not included" boundary
- [ ] Process with stage durations and the client's role
- [ ] Price: range or floor
- [ ] Every why-us point carries proof
- [ ] 2–3 cases from this service plus a quote
- [ ] Who performs the work: photo, role, experience
- [ ] FAQ from real objections plus FAQPage schema
- [ ] Internal links: cases, related services, blog
- [ ] Service + Breadcrumb schema, clean URL, canonical
- [ ] Analytics events verified firing by hand
- [ ] All `[markers]` replaced with final visuals
- [ ] Mobile check
