"""Ten problem-driven posts (November 2026, batch 13): Meta ad account disabled, Google Ads suspended, redesign
without losing rankings, getting your site/domain back, agency contract red flags, signs your agency isn't
working, click fraud and spam leads, Quality Score, 2027 marketing plan, LSA lead disputes. Build:
  python3 tools/build_new_posts.py posts_nov_2026_m && python3 tools/render_og.py posts_nov_2026_m
"""
import posts_m_a, posts_m_b, posts_m_c, posts_m_d, posts_m_e  # noqa: E401

DATE = "2026-11-17"
_M = [posts_m_a.POSTS, posts_m_b.POSTS, posts_m_c.POSTS, posts_m_d.POSTS, posts_m_e.POSTS]
POSTS = [m[i] for i in range(2) for m in _M if i < len(m)]
