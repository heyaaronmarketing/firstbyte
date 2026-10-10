# SEO audit — October 8, 2026

Goal: rank organically for The Woodlands and Greater Houston searches.
Scope: all 293 HTML pages in `site/` (272 indexable).

## How to re-run

```bash
python3 tools/seo_pass.py     # applies the fixes below (idempotent)
python3 tools/seo_audit.py    # read-only report; pass a file name to also write a CSV
python3 tools/check_site.py   # links, anchors, titles, H1s
```

Run `seo_pass.py` last after any rebuild (`build_case_studies.py`, `build_new_posts.py`,
`apply_partner_badges.py` or the older generators), so titles and schema stay correct.

## Before and after

| Check (indexable pages) | Before | After |
| --- | --- | --- |
| Titles over 60 characters (cut off in Google) | 61 | 1 (homepage, kept for the brand name) |
| Meta descriptions over 160 characters | 44 | 0 |
| Pages with no meta description | 1 | 0 |
| Titles naming The Woodlands, Houston or a nearby city | 205 | 217 |
| Pages without breadcrumb schema (excluding the homepage) | 9 | 0 |
| Relative (broken) canonical URLs | 5 | 0 |
| Pages carrying the wrong page's schema | 9 (case studies) | 0 |
| Images with missing or filename alt text | 0 | 0 |

## What changed

**Title tags.** Every core page now names the service and the market, under 60 characters:
"Google Ads Agency in The Woodlands & Houston", "SEO Company in The Woodlands & Houston",
"Home Services Marketing in The Woodlands & Houston", and so on. Grammar fixes ("Restaurants
Marketing" → "Restaurant Marketing"). All 140 city-service pages use "SEO Company in Katy, TX"
style titles. 46 blog titles were shortened so they don't truncate, and local terms were added
where they read naturally (e.g. "How to Rank in the Google Map Pack in Houston").

**Meta descriptions.** Rewritten for the homepage, services, industries, contact, blog and case
study hubs, plus templated rewrites for the 20 "Digital marketing agency in {city}" pages and the
140 city-service pages (the old template read "grow with seo that drives real results"). Every
description is 158 characters or fewer and ends with the Leak Check offer where it fits.
Open Graph and Twitter tags match the new title and description on every page.

**H1s.** The small eyebrow H1s on the main service pages, blog, case studies and contact now
include "The Woodlands & Houston".

**Schema markup.**
- LocalBusiness (`ProfessionalService`) `areaServed` now adds Montgomery County, Harris County and
  Greater Houston to the 21 cities, on every page that carries it.
- WebPage `name`/`description` match the new titles.
- BreadcrumbList added to contact, services hub, industries hub, terms and the 4 work pages.
- Case study pages no longer carry the home-services industry page's FAQ and Service schema
  (a template leak); each has Article + BreadcrumbList only.
- The 5 new blog posts carry BlogPosting (with `spatialCoverage` for The Woodlands and Houston),
  BreadcrumbList and FAQPage for their visible FAQ sections.
- All JSON-LD blocks parse as valid JSON.

**Indexing.** Canonicals on the `/work_tax/` pages were relative paths; they are now absolute.
The duplicate `/work_tax/performance-marketing/page/1/` archive is now `noindex, follow`.

**Alt text.** No images were missing alt text. Partner logos now read "Google Partner",
"Meta Business Partner", etc. Decorative duplicates in the homepage photo wall stay `alt=""`,
which is correct.

## New content

Five posts built from Google autocomplete research for Houston and The Woodlands, each
targeting a search with commercial intent the blog didn't cover:

| Post | Target searches |
| --- | --- |
| How Much Does SEO Cost in Houston & The Woodlands? | houston seo company, seo services the woodlands, seo pricing |
| Google Ads Management in Houston | google ads management houston, google ads agency houston |
| Local SEO for Contractors in Houston | local seo for contractors / electricians / roofing companies |
| Dental Marketing in The Woodlands & Houston | local seo for dentists, dental marketing |
| Law Firm Marketing in Houston | local seo for lawyers / law firms |

Each links to the matching service page and related posts, and appears first on the blog
index, the homepage blog section and the sitemap.

## Still to do (outside the code)

1. **Google Business Profile**: the strongest local ranking factor. Confirm the primary category
   ("Marketing agency" or "Internet marketing service"), add every service, post weekly, and
   keep adding photos. Make sure the address and phone match the site exactly.
2. **Reviews**: aim for 25+ Google reviews, then 2–4 a month, and reply to each. Once the profile
   has real reviews, consider showing them on the site.
3. **Citations**: claim Clutch, DesignRush, Semrush Agency Partners, Yelp, BBB, the Woodlands Area
   Chamber and Bing Places with identical name, address and phone.
4. **Google Search Console**: submit `sitemap.xml`, then request indexing for the 5 new posts and
   the 9 case study pages.
5. **Thin city-service pages**: the 140 old-design city × service pages are templated. Consolidate
   or rewrite the 10–15 that matter most (Houston, The Woodlands, Spring, Conroe, Katy) with real
   local proof, and noindex or redirect the rest over time.
6. **Official partner badges**: for Google and Meta especially, download the badge from each
   partner portal and drop it in `site/assets/firstbyte/partners/<key>-badge.svg`, then run
   `python3 tools/apply_partner_badges.py`.

---

## Full-site audit: October 9, 2026

Scope: all 137 pages (135 indexable). Every JSON-LD block, title, description, heading, canonical,
Open Graph tag, image, internal link, the sitemap, robots, redirects, response headers, live
redirect behaviour and Core Web Vitals on representative pages.

### Fixed (tools/seo_fixes_oct_2026.py — run after any generator)
| Issue | Pages | Fix |
|---|---|---|
| Organization / LocalBusiness `logo` and `image` pointed at a deleted WordPress file | home, contact | `icon-512.png` logo (ImageObject 512x512) and `og-image.png` |
| Breadcrumbs pointed at redirected URLs (`/services/`, `/industries/`) | 13 pages (26 crumbs) | redirected steps removed, positions renumbered |
| Case-study `Article` lacked `@id`, `mainEntityOfPage`, `image`, dates | 8 | complete Article markup linked to `#organization` |
| Generic share image on posts, case studies, services, industries, city and hub pages | 118 | page-specific 1200x630 share images in `/assets/firstbyte/og/`, also used as `BlogPosting`/`Article` image |
| Blog author/publisher not tied to the site entity | 87 | author + publisher reference `#organization` |
| Pages with few internal links | 33 hub pages | "From the blog" section with 3 relevant guides on every industry, service and city page |
| Case-study pages skipped from h1 to h3 | 8 | first heading is now an h2 (same styling) |
| No RSS feed | — | `/blog/feed.xml` (87 posts) + `<link rel="alternate">` on every page |
| No web app manifest | — | `/site.webmanifest` + `<link rel="manifest">` |
| `llms.txt` listed retired pages and only 10 posts | — | key pages, case studies and all 87 guides; retired links removed |
| Sitemap entries without `lastmod` | 9 | filled in; changed pages get today's date |
| No HSTS / Permissions-Policy header | all | added to `_headers` |
| `office.webp` 285 KB | 1 | recompressed (186 KB) |
| Terms page title under 30 characters | 1 | lengthened |

### Checked and fine
Valid JSON-LD on every page; no undefined `@id` references; FAQ schema matches visible text; one H1
per page; self-referencing absolute canonicals; robots meta with `max-image-preview:large`; no broken
internal links or links to redirects; every indexable page in the sitemap and nothing noindex in it;
HTTPS, zstd compression, 404 status for missing pages, trailing-slash redirects; Core Web Vitals on the
live site: LCP 0.12–0.24 s, CLS 0–0.001, TTFB about 55 ms.

### Needs the owner (outside the code)
1. **www.firstbyte.agency is broken** (Cloudflare Error 1000, "DNS points to prohibited IP"). In Cloudflare
   DNS, replace the `www` record with a proxied `CNAME www -> firstbyte.agency` (or `AAAA www -> 100::`, proxied),
   then add a Redirect Rule: hostname `www.firstbyte.agency` -> `https://firstbyte.agency${uri}` (301).
2. **Google Search Console**: verify the domain, submit `sitemap.xml`, check Page indexing for the retired URLs.
3. **sameAs**: only Facebook and LinkedIn are listed. Add the Google Business Profile (Maps) URL, Instagram,
   YouTube, Clutch, etc. when available.
4. **Named author** (done Oct 9): all posts now credit Sean Melton (`/about/#sean-melton`) in the byline, author box and BlogPosting schema.
5. **Homepage vs Houston city page** both target "digital marketing agency ... Houston". Consider making the
   homepage title lead with The Woodlands and let `/digital-marketing-agency-houston-tx/` own Houston.
6. **Reviews**: no review/rating markup is used (correct: self-serving ratings aren't eligible). Grow
   Google reviews; the hero trust line shows the rating once filled in.
7. **Pricing in llms.txt**: it still describes the $250/month Launch plan. Confirm it's still offered.

### Left as-is, on purpose
- 741 images without `width`/`height`: measured layout shift is ~0 because CSS sizes them.
- 31 older posts linked from only 1–2 pages: all are linked from the blog index (2 clicks from home).
- `dateModified` is only changed when a post's content changes.
- City pages share about a third of their wording (median); each has unique local sections.
