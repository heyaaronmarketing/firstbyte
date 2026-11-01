"""Build /privacy-policy/ and wire it in site-wide (Nov 2026).

- Creates site/privacy-policy/index.html from the Terms page shell (same header, footer, styles).
- Adds a "Privacy" link next to "Terms" in every footer.
- Adds a short consent line under every lead form's submit button and under the newsletter form.
- Links "Privacy Policy" from the Terms page.
- Adds the page to sitemap.xml and llms.txt.

Re-runnable: each step checks whether it has already been applied.
Run from the repo root: python3 tools/build_privacy_policy.py
"""
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
UPDATED = "November 1, 2026"
UPDATED_ISO = "2026-11-01"

TOC = [
    ("p1", "Who we are"),
    ("p2", "Information we collect"),
    ("p3", "How we use it"),
    ("p4", "Cookies & analytics"),
    ("p5", "Who we share it with"),
    ("p6", "Calls, texts & email"),
    ("p7", "How long we keep it"),
    ("p8", "Your choices & rights"),
    ("p9", "Security, children & links"),
    ("p10", "Changes & contact"),
]

BODY = f"""<h2 id="p0" style="margin-top: 0">Overview</h2>
<p><b>Last updated: {UPDATED}</b></p>
<p>This Privacy Policy explains what personal information First Byte LLC (“First Byte,” “we,” “us”) collects when you visit firstbyte.agency, fill out one of our forms, respond to one of our ads, or otherwise contact us, and how we use and protect it. The short version: we collect what you give us so we can reply to you and do the work you ask for, we use basic analytics to improve the site, and <b>we don’t sell your personal information</b>.</p>

<h2 id="p1">Who we are</h2>
<p>First Byte LLC is a digital marketing agency at 9000 Six Pines Dr, The Woodlands, TX 77380. You can reach us at <a href="mailto:contact@firstbyte.agency">contact@firstbyte.agency</a> or <a href="tel:+17135780634">(713) 578-0634</a>.</p>

<h2 id="p2">Information we collect</h2>
<p><b>Information you give us.</b> When you fill out a form on our site, request a free audit, or contact us, we collect what you enter, which can include:</p>
<ul>
<li>Your name, email address and phone number</li>
<li>Your website, company and industry</li>
<li>The services you’re interested in, your budget range and any message you send</li>
<li>Your email address, if you sign up for our #SundayByte newsletter</li>
</ul>
<p><b>Information from ad lead forms.</b> If you submit a lead form inside one of our ads (for example, an Instant Form on Facebook or Instagram), the platform shares the details you submit with us, such as your name, email, phone number and your answers to the form’s questions. The platform’s own privacy policy also applies to how it handles that information.</p>
<p><b>Information collected automatically.</b> When you visit our site or submit a form, we and our service providers automatically receive certain technical information, such as your IP address, browser and device type, approximate location (country or city), the page that referred you, the pages you view and the links you click.</p>
<p><b>Calls and emails.</b> If you call or email us, we keep a record of the conversation details you share so we can follow up.</p>

<h2 id="p3">How we use it</h2>
<ul>
<li>To reply to your inquiry, prepare your free audit or proposal, and schedule calls</li>
<li>To provide, manage and bill for services if you become a client</li>
<li>To send our newsletter, if you subscribed (you can unsubscribe anytime)</li>
<li>To understand how our site and ads perform and to improve them</li>
<li>To keep our site and forms secure and to filter spam and abuse</li>
<li>To comply with the law and protect our rights</li>
</ul>

<h2 id="p4">Cookies &amp; analytics</h2>
<p>We use Google Analytics 4 to understand how visitors use our site, for example which pages are viewed and which buttons are clicked. Google Analytics uses cookies and similar technologies, and Google processes this data under its own policies. You can learn more at <a href="https://policies.google.com/technologies/partner-sites" rel="noopener" target="_blank">How Google uses information from sites that use its services</a>, and you can opt out with the <a href="https://tools.google.com/dlpage/gaoptout" rel="noopener" target="_blank">Google Analytics opt-out browser add-on</a>.</p>
<p>Our site is hosted and protected by Cloudflare, which may set strictly necessary cookies to keep the site secure and fast. Our fonts are served by Google Fonts, which means your browser connects to Google’s servers when a page loads.</p>
<p>We may also use advertising and measurement tools from platforms such as Meta and Google to measure how our ads perform and to show our ads to people who have visited our site. You can control cookies through your browser settings, and you can manage ad preferences in your Facebook, Instagram and Google account settings.</p>

<h2 id="p5">Who we share it with</h2>
<p><b>We don’t sell your personal information.</b> We share it only as needed to run our business:</p>
<ul>
<li><b>Service providers</b> that work on our behalf, such as website hosting and data storage (Cloudflare), email delivery (Resend), analytics (Google), and the email, scheduling and customer-management tools we use to respond to you. They may use your information only to provide services to us.</li>
<li><b>Advertising platforms</b>, such as Meta and Google, when you interact with our ads or lead forms, as described above.</li>
<li><b>Legal and safety</b> reasons, when required by law or to protect our rights, our clients or others.</li>
<li><b>Business transfers</b>, if First Byte is involved in a merger, acquisition or sale of assets.</li>
</ul>

<h2 id="p6">Calls, texts &amp; email</h2>
<p>If you give us your phone number or email address in a form, you agree that we may call, text or email you about your request. We won’t send you marketing text messages unless you’ve agreed to receive them. Message and data rates may apply, and you can reply STOP to any text to opt out. Every marketing email includes an unsubscribe link.</p>

<h2 id="p7">How long we keep it</h2>
<p>We keep inquiry and client records for as long as we need them to respond to you, provide our services, and meet our legal, accounting and business needs. After that, we delete them or keep them only in a form that no longer identifies you.</p>

<h2 id="p8">Your choices &amp; rights</h2>
<p>You can ask us at any time to:</p>
<ul>
<li>Tell you what personal information we have about you, or give you a copy</li>
<li>Correct information that is wrong</li>
<li>Delete your information</li>
<li>Stop sending you marketing emails or texts</li>
</ul>
<p><b>State privacy rights.</b> Depending on where you live, including Texas, California and other states with consumer privacy laws, you may have additional rights, such as the right to opt out of targeted advertising or the sale of your personal information, and the right to appeal a decision we make about your request. We will not discriminate against you for using these rights.</p>
<p>To make a request, email <a href="mailto:contact@firstbyte.agency?subject=Privacy%20request">contact@firstbyte.agency</a> with the subject “Privacy request,” or call <a href="tel:+17135780634">(713) 578-0634</a>. We may need to confirm your identity before acting on a request, and we will respond within 45 days. If we deny your request, you can appeal by replying with the subject “Privacy appeal.”</p>

<h2 id="p9">Security, children &amp; links</h2>
<p><b>Security.</b> Our site uses HTTPS encryption, and access to inquiry records is restricted to our team. No method of transmission or storage is completely secure, so we can’t guarantee absolute security.</p>
<p><b>Children.</b> Our site and services are meant for businesses and are not directed to children under 13. We do not knowingly collect personal information from children.</p>
<p><b>Other websites.</b> Our site links to other websites, such as client sites, articles and social networks. Their own privacy policies apply when you visit them.</p>

<h2 id="p10">Changes &amp; contact</h2>
<p>We may update this Privacy Policy from time to time. When we do, we’ll change the “Last updated” date at the top of this page.</p>
<p>Questions about this policy or your information? Email <a href="mailto:contact@firstbyte.agency">contact@firstbyte.agency</a>, call <a href="tel:+17135780634">(713) 578-0634</a>, or write to First Byte LLC, 9000 Six Pines Dr, The Woodlands, TX 77380.</p>"""

DESC = ("How First Byte LLC collects, uses and protects personal information from firstbyte.agency, "
        "our forms and our ads. We don’t sell your personal information.")

CONSENT = ('<p class="form-consent">By sending, you agree First Byte may contact you about your request. '
           'We never sell your info. <a href="/privacy-policy/">Privacy Policy</a></p>')
NEWS_CONSENT = ('<p class="form-consent form-consent-l">Unsubscribe anytime · <a href="/privacy-policy/">Privacy Policy</a></p>')
CSS = ("\n/* nov-2026: form consent line */\n"
       ".form-consent{margin:12px 0 0;font-size:13px;line-height:1.45;color:rgba(255,255,255,.62);text-align:center}"
       ".form-consent a{color:inherit;text-decoration:underline;text-underline-offset:2px}"
       ".form-consent a:hover{color:#fff}.form-consent-l{text-align:left}\n")


def build_page():
    src = (SITE / "terms-of-service" / "index.html").read_text(encoding="utf-8")
    s = src
    # head
    s = s.replace("<title>Terms of Service | First Byte Digital Marketing</title>",
                  "<title>Privacy Policy | First Byte Digital Marketing</title>")
    s = re.sub(r'(<meta (?:name|property)="(?:description|og:description|twitter:description)" content=")[^"]*(")',
               lambda m: m.group(1) + DESC + m.group(2), s)
    s = s.replace("Terms of Service | First Byte", "Privacy Policy | First Byte")
    s = s.replace("https://firstbyte.agency/terms-of-service/", "https://firstbyte.agency/privacy-policy/")
    s = s.replace('"name": "Terms of Service",', '"name": "Privacy Policy",')
    # hero
    s = re.sub(r'<h1 class="seo-h1">.*?</h1>\s*<p class="sv-disp">.*?</p>\s*<p class="sub"[^>]*>.*?</p>',
               '<h1 class="seo-h1"><span class="tri"></span>Privacy Policy · First Byte LLC</h1>\n'
               '<p class="sv-disp">Your info, handled straight.</p>\n'
               '<p class="sub" style="max-width: 640px">What we collect when you contact us, why we collect it, '
               'and your choices. We don’t sell your personal information. Questions? Email '
               '<a href="mailto:contact@firstbyte.agency" style="color: #fff">contact@firstbyte.agency</a> or call '
               '<a href="tel:+17135780634" style="color: #fff">(713) 578-0634</a>.</p>', s, count=1, flags=re.S)
    # body: replace the TOC + legal text block
    toc = ('<nav class="toc" aria-label="On this page"><span class="lbl" style="padding: 6px 10px 10px">On this page</span>'
           + "".join(f'<a href="#{i}">{t}</a>' for i, t in TOC)
           + '<a href="/contact/" style="color: var(--cyan)">Contact us →</a></nav>')
    s, n = re.subn(r'<nav class="toc" aria-label="On this page">.*?</nav>\s*<div class="tbody">.*?</div>\s*</div></section>',
                   toc + '\n<div class="tbody">' + BODY + '</div>\n</div></section>', s, count=1, flags=re.S)
    assert n == 1, "terms body block not found"
    out = SITE / "privacy-policy" / "index.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(s, encoding="utf-8")
    return out


def wire_site():
    changed = 0
    for p in SITE.rglob("*.html"):
        s = p.read_text(encoding="utf-8"); o = s
        # footer links
        if 'href="/privacy-policy/"' not in s or p.parent.name == "privacy-policy":
            s = s.replace('<a href="/terms-of-service/">Terms</a></span></div>',
                          '<a href="/terms-of-service/">Terms</a> · <a href="/privacy-policy/">Privacy</a></span></div>')
            s = s.replace('<a href="/terms-of-service/">Terms</a></nav>',
                          '<a href="/terms-of-service/">Terms</a><a href="/privacy-policy/">Privacy</a></nav>')
            s = s.replace('<a href="/terms-of-service/">Terms</a> · <a href="/contact/">Contact</a>',
                          '<a href="/terms-of-service/">Terms</a> · <a href="/privacy-policy/">Privacy</a> · <a href="/contact/">Contact</a>')
        # consent under lead-form submit buttons
        if 'class="form-consent"' not in s:
            s = re.sub(r'(<button class="btn btn-p" type="submit"[^>]*>Send my message <span class="arr">→</span></button>)',
                       r'\1' + CONSENT, s)
            s = s.replace('<button type="submit" aria-label="Subscribe to #SundayByte">→</button></form>',
                          '<button type="submit" aria-label="Subscribe to #SundayByte">→</button></form>' + NEWS_CONSENT)
        # terms page: link the policy
        if p.parent.name == "terms-of-service" and 'according to our <a href="/privacy-policy/">' not in s:
            s = s.replace("according to our Privacy Policy and Cookie Notice, which are incorporated",
                          'according to our <a href="/privacy-policy/">Privacy Policy</a> (which includes our cookie notice), which is incorporated')
        s = s.replace("lead.css?v=11", "lead.css?v=12")
        if s != o:
            p.write_text(s, encoding="utf-8"); changed += 1
    css = SITE / "assets" / "firstbyte" / "lead.css"
    c = css.read_text(encoding="utf-8")
    if "nov-2026: form consent line" not in c:
        css.write_text(c.rstrip() + "\n" + CSS, encoding="utf-8")
    # sitemap + llms.txt
    sm = SITE / "sitemap.xml"
    if sm.exists():
        t = sm.read_text(encoding="utf-8")
        if "/privacy-policy/" not in t:
            entry = (f"  <url>\n    <loc>https://firstbyte.agency/privacy-policy/</loc>\n    <lastmod>{UPDATED_ISO}</lastmod>\n"
                     "    <priority>0.3</priority>\n  </url>\n")
            sm.write_text(t.replace("</urlset>", entry + "</urlset>"), encoding="utf-8")
    ll = SITE / "llms.txt"
    if ll.exists():
        t = ll.read_text(encoding="utf-8")
        if "/privacy-policy/" not in t:
            ll.write_text(t.rstrip() + "\n- [Privacy Policy](https://firstbyte.agency/privacy-policy/): What First Byte collects, why, and your choices.\n", encoding="utf-8")
    return changed


if __name__ == "__main__":
    page = build_page()
    n = wire_site()
    print("built", page.relative_to(ROOT), "| html files updated:", n)
