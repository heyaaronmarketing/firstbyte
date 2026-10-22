"""Ten agency-intent posts (October 2026, batch 7): Google Ads not converting, who owns your ad
accounts, fractional CMO vs agency, how long SEO takes, Hispanic marketing in Houston, B2B energy
and industrial marketing, selling event tickets, Google Shopping for Shopify, multi-location local
SEO, YouTube ads for local businesses. Build:
  python3 tools/build_new_posts.py posts_oct_2026_g && python3 tools/render_og.py posts_oct_2026_g
"""
import posts_g_a, posts_g_b, posts_g_c, posts_g_d, posts_g_e  # noqa: E401

DATE = "2026-10-22"
POSTS = (posts_g_a.POSTS[:1] + posts_g_b.POSTS[:1] + posts_g_c.POSTS[:1] + posts_g_d.POSTS[:1] + posts_g_e.POSTS[:1]
         + posts_g_a.POSTS[1:] + posts_g_b.POSTS[1:] + posts_g_c.POSTS[1:] + posts_g_d.POSTS[1:] + posts_g_e.POSTS[1:])
