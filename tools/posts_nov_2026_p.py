"""Fifteen Houston/The Woodlands posts (November 2026, batch 16): irrigation, pool cleaning, appliance repair,
flooring, countertop fabricators, boat dealers/marinas, acupuncture, hearing/audiology, hospice, yoga, dance, music
lessons, food trucks, breweries/wineries/taprooms, catering. Build:
  python3 tools/build_new_posts.py posts_nov_2026_p && python3 tools/render_og.py posts_nov_2026_p
"""
import posts_p_a, posts_p_b, posts_p_c, posts_p_d, posts_p_e  # noqa: E401

DATE = "2026-11-25"
_M = [posts_p_a.POSTS, posts_p_b.POSTS, posts_p_c.POSTS, posts_p_d.POSTS, posts_p_e.POSTS]
POSTS = [m[i] for i in range(3) for m in _M if i < len(m)]
