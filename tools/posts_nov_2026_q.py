"""Fifteen mixed-format Houston/The Woodlands posts (November 2026, batch 17): sign rules, city/ZIP naming for
local SEO, local SEO myths, local PR, chambers/networking, sponsorships, EDDM/direct mail, new-mover marketing,
trade shows, hurricane playbook, rodeo season, growth corridors, Asian American marketing, owner Q&A, glossary.
Build: python3 tools/build_new_posts.py posts_nov_2026_q && python3 tools/render_og.py posts_nov_2026_q
"""
import posts_q_a, posts_q_b, posts_q_c, posts_q_d, posts_q_e  # noqa: E401

DATE = "2026-11-27"
_M = [posts_q_a.POSTS, posts_q_b.POSTS, posts_q_c.POSTS, posts_q_d.POSTS, posts_q_e.POSTS]
POSTS = [m[i] for i in range(3) for m in _M if i < len(m)]
