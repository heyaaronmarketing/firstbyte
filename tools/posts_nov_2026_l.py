"""Five answer-first niche posts (November 2026, batch 12) modeled on law-firm-marketing-houston, which AI search
cites: water damage restoration, financial advisors, optometrists, therapy practices, commercial cleaning.
Build: python3 tools/build_new_posts.py posts_nov_2026_l && python3 tools/render_og.py posts_nov_2026_l
"""
import posts_l_a, posts_l_b, posts_l_c, posts_l_d, posts_l_e  # noqa: E401

DATE = "2026-11-12"
POSTS = posts_l_a.POSTS + posts_l_b.POSTS + posts_l_c.POSTS + posts_l_d.POSTS + posts_l_e.POSTS
