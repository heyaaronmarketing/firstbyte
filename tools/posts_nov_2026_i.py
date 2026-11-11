"""Ten niche-business posts (November 2026, batch 9): foundation repair, garage doors, electricians, house
cleaning, veterinary clinics, physical therapy, orthodontists, daycares, movers, property management. Build:
  python3 tools/build_new_posts.py posts_nov_2026_i && python3 tools/render_og.py posts_nov_2026_i
"""
import posts_i_a, posts_i_b, posts_i_c, posts_i_d, posts_i_e  # noqa: E401

DATE = "2026-11-11"
POSTS = (posts_i_a.POSTS[:1] + posts_i_b.POSTS[:1] + posts_i_c.POSTS[:1] + posts_i_d.POSTS[:1] + posts_i_e.POSTS[:1]
         + posts_i_a.POSTS[1:] + posts_i_b.POSTS[1:] + posts_i_c.POSTS[1:] + posts_i_d.POSTS[1:] + posts_i_e.POSTS[1:])
