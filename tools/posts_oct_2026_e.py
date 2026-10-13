"""Ten industry long-tail posts (October 2026, batch 5): plumbing, pest control, lawn care /
commercial landscaping, remodeling, home care. Keywords from Google autocomplete with weak
page-one competition. Build:
  python3 tools/build_new_posts.py posts_oct_2026_e && python3 tools/render_og.py posts_oct_2026_e
"""
import posts_e_a, posts_e_b, posts_e_c, posts_e_d, posts_e_e  # noqa: E401

DATE = "2026-10-13"
POSTS = (posts_e_a.POSTS[:1] + posts_e_b.POSTS[:1] + posts_e_d.POSTS[:1] + posts_e_c.POSTS[:1] + posts_e_e.POSTS[:1]
         + posts_e_a.POSTS[1:] + posts_e_b.POSTS[1:] + posts_e_d.POSTS[1:] + posts_e_c.POSTS[1:] + posts_e_e.POSTS[1:])
