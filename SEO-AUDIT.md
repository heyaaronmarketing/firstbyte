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
