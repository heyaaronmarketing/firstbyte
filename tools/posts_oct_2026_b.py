"""Ten local industry posts (October 2026, batch 2), rendered by tools/build_new_posts.py.

Industries: HVAC, roofing, pool builders, real estate agents, restaurants, wedding venues,
chiropractors, medical practices, gyms/fitness studios, hotels. Each targets the phrases owners
in that industry search for in Houston and The Woodlands; sources are linked inline.
Build:  python3 tools/build_new_posts.py posts_oct_2026_b
"""
import posts_b_a, posts_b_b, posts_b_c, posts_b_d, posts_b_e  # noqa: E401

DATE = "2026-10-09"
# order = publish order; the first post becomes the featured card on the blog index
POSTS = posts_b_a.POSTS + posts_b_c.POSTS + posts_b_d.POSTS + posts_b_b.POSTS + posts_b_e.POSTS
