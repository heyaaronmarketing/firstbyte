"""Ten Houston/The Woodlands posts (November 2026, batch 15): home inspectors, locksmiths, collision repair,
car wash memberships, interior designers, photographers, private schools, self storage, outdoor living/patio
covers, staffing agencies. Build:
  python3 tools/build_new_posts.py posts_nov_2026_o && python3 tools/render_og.py posts_nov_2026_o
"""
import posts_o_a, posts_o_b, posts_o_c, posts_o_d, posts_o_e  # noqa: E401

DATE = "2026-11-24"
_M = [posts_o_a.POSTS, posts_o_b.POSTS, posts_o_c.POSTS, posts_o_d.POSTS, posts_o_e.POSTS]
POSTS = [m[i] for i in range(2) for m in _M if i < len(m)]
