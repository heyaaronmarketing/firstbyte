"""Five long-tail keyword posts (October 2026, batch 4), rendered by tools/build_new_posts.py.

Keywords from Google autocomplete with weak page-one competition: "google business profile video
verification", "is nextdoor advertising worth it", "google guaranteed vs google verified",
"google business profile suspended after changing address", "radio advertising cost houston".
Build:  python3 tools/build_new_posts.py posts_oct_2026_d && python3 tools/render_og.py posts_oct_2026_d
"""
import posts_d_a, posts_d_b, posts_d_c, posts_d_d, posts_d_e  # noqa: E401

DATE = "2026-10-11"
POSTS = posts_d_e.POSTS + posts_d_a.POSTS + posts_d_c.POSTS + posts_d_b.POSTS + posts_d_d.POSTS
