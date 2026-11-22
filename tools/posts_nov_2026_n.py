"""Ten Houston/The Woodlands posts (November 2026, batch 14): pressure washing, concrete contractors, window and
door replacement, used car dealers, dermatology, bakeries and coffee shops, party/event rentals, boutique retail,
choosing a marketing agency, and Katy/Cypress. Build:
  python3 tools/build_new_posts.py posts_nov_2026_n && python3 tools/render_og.py posts_nov_2026_n
"""
import posts_n_a, posts_n_b, posts_n_c, posts_n_d, posts_n_e  # noqa: E401

DATE = "2026-11-22"
_M = [posts_n_a.POSTS, posts_n_b.POSTS, posts_n_c.POSTS, posts_n_d.POSTS, posts_n_e.POSTS]
POSTS = [m[i] for i in range(2) for m in _M if i < len(m)]
