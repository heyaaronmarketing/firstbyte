# Client result approvals

**Status (Oct 8, 2026): all three cards approved and live.**

The three result cards on the homepage are set to `data-status="approved"`. For any future
card, start it as `data-status="draft"`: drafts stay hidden on the live site and can be
previewed at `https://firstbyte.agency/?preview=results`.

## How to publish a card

1. Send the client the email below (one per client).
2. Update the quote and numbers in `site/index.html` (search for `tcards`) to match
   exactly what the client approved.
3. Change that card's `data-status="draft"` to `data-status="approved"`.
4. Replace the initials (`<span class="tc-mono" ...>TT</span>`) with a headshot:
   `<img src="/assets/firstbyte/clients/todd-tarochione.webp" alt="Todd Tarochione">`
   (square, 200×200px or larger).
5. Commit and push. As soon as one card is approved, the old rotating quotes hide.

Keep the approval email in your records. Results shown on the site must be ones the
client has confirmed.

---

## Email: Todd Tarochione, G4 Electric

**Subject:** Can we feature G4 Electric on our site?

Hi Todd,

We're refreshing the First Byte website and would love to feature G4 Electric. Here's a
draft. Could you check the numbers against what you've seen and fix anything that's off?

> **2.4× more inbound calls in 90 days**
> "Within 90 days our phone was ringing 2.4× as often, and our cost per booked job
> dropped 38%. First Byte runs our ads like it's their own money."
> — Todd Tarochione, Owner, G4 Electric

If the real numbers are different, just send them back and I'll update it. A headshot
would be great too (a phone photo is fine).

Thanks,
Sean

---

## Email: Richard Silver, Verve Chiropractic

**Subject:** Can we feature Verve on our site?

Hi Richard,

We're refreshing the First Byte website and would love to feature Verve Chiropractic.
Here's a draft. Could you check the numbers and correct anything that's off?

> **63 new patients in the first 60 days**
> "We went from a handful of new patients a week to 63 in our first 60 days, at about
> $41 each. Now we know exactly which ads fill the schedule."
> — Richard Silver, Owner, Verve Chiropractic

Send back the real numbers if they differ and I'll update it. A headshot would be great too.

Thanks,
Sean

---

## Email: Vickie Bennet, Lavender Life

**Subject:** Can we feature Lavender Life on our site?

Hi Vickie,

We're refreshing the First Byte website and would love to feature Lavender Life.
Here's a draft. Could you check the numbers and correct anything that's off?

> **3.1× online revenue, year over year**
> "Online revenue is up 3.1× year over year and every ad dollar now returns $4.60.
> First Byte has been a game-changer for Lavender Life."
> — Vickie Bennet, President, Lavender Life

Send back the real numbers if they differ and I'll update it. A headshot would be great too.

Thanks,
Sean
