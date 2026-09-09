# Blog Page Kit

The blog is the inbound engine and the main source of internal links into case studies and service
pages. The rules changed, though: the page is now read by AI search as well as by Google. To be
quoted you have to be machine-readable — structured, marked up, dated, answering questions a human
actually asks.

## Structure — template, top to bottom

**1. Breadcrumbs** — `Home → Blog → Category → Article`.

**2. H1** — one per page. Then H2 and H3 only, never skipping levels. Primary query in the title and
in the first 100 words.

**3. Meta line** — reading time plus a visible `Updated: [date]`. Reading time lifts click-through;
a visible freshness date is a signal to both Google and AI search, which quote recent material more
readily.

**4. TL;DR** — 3–5 bullets at the top carrying the whole point. This is the fragment AI search
extracts most often, so it has to answer the question standing alone, without the rest of the article.

**5. Table of contents** — auto-built from H2, sticky on scroll. Humans navigate, machines parse.
Mandatory for long-form.

**6. Body** — not a wall of text. Interleave:
   - **Comparison tables.** Structured data is what AI search quotes most. Format: option · criterion · criterion.
   - **Client quotes** as pull-outs. Proof that real people stand behind the text.
   - **Inline CTAs** contextual to the section, not only one banner at the bottom.
   - **Video or screen-recording embeds.** An imperfect expert recording is a human signal an
     AI-generated competitor does not have.

**7. FAQ** — real buyer questions with short answers, phrased the way a person asks them. Direct feed
for AI answers.

**8. Author card** — name, photo, role, credentials. The expertise signal: who wrote this and why they
can be believed.

**9. Related articles** — 3 cards. Internal links the reader and the crawler both follow.

**10. Hidden technical layer** — Article schema with `datePublished` and `dateModified`, Author schema
tying the author to content across the site, clean URL.

## The 17 elements by category

| Category | Elements |
|---|---|
| **Structure & on-page** | sticky table of contents · TL;DR · breadcrumbs · heading hierarchy (one H1) · FAQ block |
| **Trust & authority** | author card with bio · Author schema · Article schema with dates · client quotes |
| **Conversion & engagement** | inline CTAs · related articles · reading time |
| **AI search optimisation** | comparison tables · video embeds · visible "updated" date |
| **URL structure** | clean hierarchy `/blog/article/` · no dates or numbers in the address |

## Writer SOP

1. **TL;DR first.** Write the 3–5 bullet summary before the body. If the point cannot be stated
   briefly, the article is not thought through yet.
2. **One H1, no level skipping.** H2 → H3, never H2 → H4.
3. **Write sections as answers to questions.** Every H2 answers one concrete buyer question. That is
   how the text lands in AI answers.
4. **At least one comparison table** where the topic allows. A table gets quoted more often than a
   paragraph.
5. **FAQ from real questions**, taken from calls, email and objections. Phrase them the way the client
   phrases them.
6. **Inline CTAs through the text**, not only at the end. Read about audits → "book an audit".
7. **Internal links are mandatory:** to adjacent articles, cases, service pages. Each article
   strengthens its neighbours.
8. **Primary query** in H1 and the first 100 words. No stuffing.
9. **Mark visuals in the draft:** `[COVER]`, `[AUTHOR CARD]`, `[TABLE]`, `[QUOTE]`, `[VIDEO]`.
10. **Run the humanisation pass** (`copy-humanisation.md`) as a separate step after the draft.
    Negative parallelism and punch triads are hard fails at the blind judge.
11. **Set `Updated: [date]`** and refresh it on every substantive edit. It is a real freshness signal,
    not decoration.

## Technical checklist — template, set once

**Schema** — Article with `datePublished` and `dateModified` · Author schema linking author to content
across the site · FAQ schema on the questions block · BreadcrumbList on the breadcrumbs.

**URL** — clean hierarchy `/blog/` → `/blog/article-name/` → `/blog/category/`. **No dates or numbers
in the address:** `/top-tools/` rather than `/top-10-tools-2026/`, so the URL does not age and the
article stays evergreen. Latin slug, no spaces or stray parameters.

**Template elements** — table of contents auto-built from H2 and sticky · reading time calculated
automatically · visible "Updated" pulled from `dateModified` · related-articles block auto-selected by
category or tags · author card pulled from the author profile.

## Designer brief

| Marker | What to produce |
|---|---|
| `[COVER]` | Article hero or cover with the headline |
| `[AUTHOR CARD]` | Photo, name, role, credentials — consistent across all articles |
| `[TABLE]` | Comparison table, readable on mobile via horizontal scroll |
| `[QUOTE]` | Client pull quote with photo or logo |
| `[VIDEO]` | Video or screen-recording embed with a preview frame |

Client's brand colours and type, white background behind screenshots. Most traffic is a phone: check
the table of contents, tables and CTAs on mobile. Alt text on every visual. Export WebP, lazy-load,
under 200KB where possible.

## Pre-launch checklist

- [ ] TL;DR (3–5 bullets) at the top and self-sufficient
- [ ] One H1, heading levels do not skip
- [ ] Table of contents builds and sticks
- [ ] Reading time plus visible "Updated" date in place
- [ ] At least one comparison table where appropriate
- [ ] FAQ from real questions plus FAQ schema
- [ ] Author card plus Author schema plus Article schema with dates
- [ ] Inline CTAs through the text, not only at the bottom
- [ ] Internal links to cases, service pages, adjacent articles plus a "Related" block
- [ ] URL clean, no dates or numbers
- [ ] Breadcrumbs plus BreadcrumbList schema
- [ ] Alt text on all visuals, mobile check
