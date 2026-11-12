"""Ten vertical deep-dives (November 2026, batch 11): live events, eCommerce, CPG, sports & fitness, restaurants,
hospitality. Build: python3 tools/build_new_posts.py posts_nov_2026_k && python3 tools/render_og.py posts_nov_2026_k
"""
import posts_k_a, posts_k_b, posts_k_c, posts_k_d, posts_k_e  # noqa: E401

DATE = "2026-11-12"
_M = [posts_k_a.POSTS, posts_k_b.POSTS, posts_k_c.POSTS, posts_k_d.POSTS, posts_k_e.POSTS]
POSTS = [m[i] for i in range(2) for m in _M if i < len(m)]
