"""Ten Houston/The Woodlands posts (November 2026, batch 18): social media management cost, branding/logo cost,
HIPAA-compliant healthcare marketing, LinkedIn ads for B2B, Google Ad Grants, short-term rental direct bookings,
TikTok ads, video production cost, 2027 marketing calendar, website maintenance cost. Build:
  python3 tools/build_new_posts.py posts_nov_2026_r && python3 tools/render_og.py posts_nov_2026_r
"""
import posts_r_a, posts_r_b, posts_r_c, posts_r_d, posts_r_e  # noqa: E401

DATE = "2026-11-27"
_M = [posts_r_a.POSTS, posts_r_b.POSTS, posts_r_c.POSTS, posts_r_d.POSTS, posts_r_e.POSTS]
POSTS = [m[i] for i in range(2) for m in _M if i < len(m)]
