"""Ten specialty-niche posts (October 2026, batch 6): IV therapy, medical weight loss, massage,
esthetician, dog grooming, dog daycare/boarding, auto detailing, cryotherapy/recovery, lash studios,
Pilates studios. Build:
  python3 tools/build_new_posts.py posts_oct_2026_f && python3 tools/render_og.py posts_oct_2026_f
"""
import posts_f_a, posts_f_b, posts_f_c, posts_f_d, posts_f_e  # noqa: E401

DATE = "2026-10-13"
POSTS = (posts_f_a.POSTS[:1] + posts_f_b.POSTS[:1] + posts_f_c.POSTS[:1] + posts_f_d.POSTS[:1] + posts_f_e.POSTS[:1]
         + posts_f_a.POSTS[1:] + posts_f_b.POSTS[1:] + posts_f_c.POSTS[1:] + posts_f_d.POSTS[1:] + posts_f_e.POSTS[1:])
