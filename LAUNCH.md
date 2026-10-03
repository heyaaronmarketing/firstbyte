# First Byte redesign: launch guide

This repo is the current firstbyte.agency repo with the redesign built in. It keeps the same layout (`site/`, the Cloudflare Worker in `src/worker.js`, `wrangler.jsonc`), so it deploys the same way as today.

## Uploading to GitLab
1. Unzip, then push the folder's contents to your GitLab project's default branch:
   `git init && git add . && git commit -m "Redesign" && git remote add origin <gitlab-url> && git push -u origin main`
2. Deploying, pick **one** of these:
   - **Cloudflare Workers Builds** (recommended, same as today): in Cloudflare → Workers & Pages → firstbyte → Settings → Builds, connect the GitLab repo. Every push to `main` deploys.
   - **GitLab CI**: in GitLab → Settings → CI/CD → Variables, add `CLOUDFLARE_API_TOKEN` (masked) and `CLOUDFLARE_ACCOUNT_ID`. The `deploy-cloudflare` job in `.gitlab-ci.yml` then deploys after the checks pass.
   - **GitLab Pages preview** (optional): set the variable `DEPLOY_GITLAB_PAGES=true`. Forms still work there, because they fall back to FormSubmit.
3. Every push runs `tools/check_site.py`. It fails the pipeline if a new page has a broken link, image or #anchor, a missing title, description or canonical, duplicate metadata, or not exactly one H1.
4. The existing secrets (`RESEND_API_KEY`, `ADMIN_USER`, `ADMIN_PASS`) and the `LEADS_KV` binding stay as they are. Nothing new to configure.

## What's new in `site/`
- **101 pages in the new design**, as static HTML with no framework:
  - **Homepage** (`/`)
  - **5 service pages** (`/services/<service>/`)
  - **Contact and Terms** (`/contact/`, `/terms-of-service/`)
  - **About** (`/about/`)
  - **8 industry pages** (`/industries/<industry>/`)
  - **Service areas**: the `/service-areas/` hub plus 20 city pages (`/digital-marketing-agency-<city>-tx/`)
  - **Blog**: the `/blog/` index plus 62 articles, 10 of them new
  - **Thank-you page** (`/thank-you/`, `noindex`)
- **404 page**: `site/404.html`. `wrangler.jsonc` now serves it (`not_found_handling: "404-page"`).
- **Shared assets**: `site/assets/firstbyte/` holds the stylesheets, images, icon sprite and `site.js`.
- **`site.js`**: the homepage pixel animation, number count-ups, case-study tabs with keyboard support, `/#work-<case>` deep links, "I need" chips, the newsletter, and form sending.
- **`sitemap.xml`**: all 232 existing URLs kept, 63 lastmod dates updated, 38 new URLs added.
- **Also replaced**: `llms.txt` and the favicons/OG image.
- **`robots.txt`**: unchanged.

Old pages that weren't redesigned are still live and unchanged:
- `/industries/retail/` and `/industries/banking/`
- the 140 `/seo-<city>-tx/`-style pages
- `/work/`, `/work_tax/`, `/launch/` and `/services/` (index)

## Forms and leads
- Every form posts to your existing `/api/contact` Worker. It emails sean@firstbyte.agency through Resend and saves the lead to `/admin/leads`, as today.
- The Worker was updated to accept the new forms (`_v=2`). Name and email are required. Company, budget, services and message are all included in the email. `_honey` is the spam trap.
- The old forms on pages still in the old design work exactly as before.
- Without JavaScript, a successful post goes to `/thank-you/`. An error goes to `/contact/?sent=0`, which shows a message.
- **Fallback:** if `/api/contact` can't be reached (e.g. a GitLab Pages preview), forms send through FormSubmit to sean@firstbyte.agency instead. The first FormSubmit email asks you to click "Activate" once.
- Newsletter signups arrive with the subject "New #SundayByte newsletter signup". They don't appear in the public "recent leads" toasts.

## Before you go live
- **SkinLab case study:** the metrics are placeholders. Confirm or edit them in `site/index.html` (search for `cs-sl`). Each number appears twice: in the visible text and in `data-v`.
- **301 redirects:** nothing links to the old `/seo-<city>-tx/`, `/work_tax/` and similar pages any more. Over the next few weeks, add 301 redirects from each one to its closest new page, and watch them in Search Console.
- **After deploy:** submit `https://firstbyte.agency/sitemap.xml` in Google Search Console.
- **Don't run the old build scripts:** `blog.py`, `geo_pages.py`, `homepage.py` and the other root-level `.py` scripts would overwrite the new pages.
