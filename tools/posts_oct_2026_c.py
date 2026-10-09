"""Five long-tail keyword posts (October 2026, batch 3), rendered by tools/build_new_posts.py.

Keywords were picked from Google autocomplete (real search demand) where page one is weak
(directories, forums, outdated or off-target pages): "how much is a billboard in houston",
"google business listing scam calls", "is yelp advertising worth it for small business",
"is angi leads worth it for contractors", "why are my google reviews disappearing".
Build:  python3 tools/build_new_posts.py posts_oct_2026_c && python3 tools/render_og.py posts_oct_2026_c
"""
import posts_c_a, posts_c_b, posts_c_c, posts_c_d, posts_c_e  # noqa: E401

DATE = "2026-10-09"
POSTS = posts_c_a.POSTS + posts_c_e.POSTS + posts_c_d.POSTS + posts_c_c.POSTS + posts_c_b.POSTS
