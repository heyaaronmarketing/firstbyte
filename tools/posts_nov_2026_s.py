"""Refresh batch (November 2026): fifteen older, thin posts rewritten in depth under their existing URLs.
Each post keeps its original datePublished ("date") and gets dateModified ("modified"); REFRESH keeps the
cards where they are in the blog index and leaves the homepage alone. Build:
  python3 tools/build_new_posts.py posts_nov_2026_s && python3 tools/render_og.py posts_nov_2026_s
"""
import posts_s_a, posts_s_b, posts_s_c, posts_s_d, posts_s_e  # noqa: E401

DATE = "2026-11-27"
REFRESH = True
POSTS = posts_s_a.POSTS + posts_s_b.POSTS + posts_s_c.POSTS + posts_s_d.POSTS + posts_s_e.POSTS
