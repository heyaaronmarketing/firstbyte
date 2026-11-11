"""Fifteen niche-business posts (November 2026, batch 10): solar, painting, fences, tree service, junk removal,
insurance agencies, CPA firms, mortgage loan officers, funeral homes, martial arts studios, tutoring centers,
salons and barbershops, senior living, plastic surgeons, urgent care. Build:
  python3 tools/build_new_posts.py posts_nov_2026_j && python3 tools/render_og.py posts_nov_2026_j
"""
import posts_j_a, posts_j_b, posts_j_c, posts_j_d, posts_j_e  # noqa: E401

DATE = "2026-11-11"
_M = [posts_j_a.POSTS, posts_j_b.POSTS, posts_j_c.POSTS, posts_j_d.POSTS, posts_j_e.POSTS]
POSTS = [m[i] for i in range(3) for m in _M if i < len(m)]
