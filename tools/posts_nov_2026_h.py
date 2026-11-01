"""Ten agency-intent posts (November 2026, batch 8): website not showing up on Google, GA4 lead
tracking, agency pricing models, speed to lead, Facebook lead quality, Microsoft Ads, website
builders, SMS marketing rules in Texas, home builder marketing, auto repair shop marketing. Build:
  python3 tools/build_new_posts.py posts_nov_2026_h && python3 tools/render_og.py posts_nov_2026_h
"""
import posts_h_a, posts_h_b, posts_h_c, posts_h_d, posts_h_e  # noqa: E401

DATE = "2026-11-01"
POSTS = (posts_h_a.POSTS[:1] + posts_h_b.POSTS[:1] + posts_h_c.POSTS[:1] + posts_h_d.POSTS[:1] + posts_h_e.POSTS[:1]
         + posts_h_a.POSTS[1:] + posts_h_b.POSTS[1:] + posts_h_c.POSTS[1:] + posts_h_d.POSTS[1:] + posts_h_e.POSTS[1:])
