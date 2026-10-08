/* First Byte — analytics.js
   GA4 event tracking for firstbyte.agency. Loaded on every page after the gtag snippet.
   Every event also goes to window.dataLayer, so a GTM container added later sees the same events.

   Events (all carry page_type):
     generate_lead      lead form sent (site.js)                 offer, industry, ad_spend, form_location
     form_start         first interaction with a lead form        form_location
     form_error         a lead form failed to send (site.js)      form_location, error
     sign_up            #SundayByte newsletter signup (site.js)   method
     click_to_call      tel: link                                 link_location
     email_click        mailto: link                              link_location
     cta_click          primary button (Leak Check, etc.)         cta_text, cta_location, cta_destination
     case_study_cta     "Run a business like X?" button           case_study, industry
     case_study_tab     a homepage case study tab opened          case_study
     scroll_depth       25/50/75/100% on blog posts + case studies  percent
     lead_engine_*      blackjack widget steps (leadmode.js)
   Outbound clicks, site search, video and file downloads come from GA4 enhanced measurement.
*/
(function () {
  'use strict';
  var win = window, doc = document;

  var path = location.pathname;
  var pageType =
    path === '/' ? 'home' :
    /^\/blog\/?$/.test(path) ? 'blog_index' :
    /^\/blog\//.test(path) ? 'blog_post' :
    /^\/case-studies\/?$/.test(path) ? 'case_study_index' :
    /^\/case-studies\//.test(path) ? 'case_study' :
    /^\/services\//.test(path) ? 'service' :
    /^\/industries\//.test(path) ? 'industry' :
    /^\/digital-marketing-agency-/.test(path) ? 'city' :
    /^\/(seo|paid-advertising|web-design|brand-development|influencer-marketing|performance-marketing|public-relations)-.+-tx\//.test(path) ? 'city_service' :
    /^\/contact\//.test(path) ? 'contact' :
    /^\/thank-you\//.test(path) ? 'thank_you' :
    /^\/about\//.test(path) ? 'about' : 'other';

  /* Send one event to GA4 (and the dataLayer). opts.callback runs once the hit is sent,
     or after 900 ms if GA is blocked, so a redirect never waits on analytics. */
  function track(name, params, opts) {
    params = params || {};
    params.page_type = pageType;
    var done = false, cb = opts && opts.callback;
    var finish = function () { if (!done) { done = true; if (cb) cb(); } };
    try {
      win.dataLayer = win.dataLayer || [];
      var dl = { event: name }; for (var k in params) dl[k] = params[k];
      win.dataLayer.push(dl);
      if (typeof win.gtag === 'function') {
        var p = {}; for (var j in params) p[j] = params[j];
        p.transport_type = 'beacon';
        if (cb) p.event_callback = finish;
        win.gtag('event', name, p);
      }
    } catch (_e) { /* analytics must never break the page */ }
    if (cb) { if (typeof win.gtag !== 'function') finish(); else setTimeout(finish, 900); }
  }
  win.fbTrack = track;

  /* Where on the page an element sits, in words a report reader recognises. */
  function where(el) {
    if (el.closest('.mbar, .fblm-mobilebar')) return 'mobile_bar';
    if (el.closest('header, .nav')) return 'header';
    if (el.closest('footer, .foot')) return 'footer';
    if (el.closest('.bp-side')) return 'blog_sidebar';
    if (el.closest('.bp-inline')) return 'blog_inline';
    if (el.closest('.hero, .sv-hero, .bp-hero, .hub-hero, .lg-hero')) return 'hero';
    if (el.closest('#contact, .contact, form')) return 'contact';
    if (el.closest('.cs-stage, .cs')) return 'case_study';
    if (el.closest('.mid-cta')) return 'mid_page';
    var sec = el.closest('section[id]');
    return sec ? sec.id : 'body';
  }
  function label(el) { return (el.innerText || el.textContent || '').replace(/\s+/g, ' ').replace(/[→↗]/g, '').trim().slice(0, 80); }

  doc.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a, button');
    if (!a) return;
    var href = a.getAttribute('href') || '';
    if (/^tel:/i.test(href)) { track('click_to_call', { link_location: where(a), link_text: label(a) }); return; }
    if (/^mailto:/i.test(href)) { track('email_click', { link_location: where(a) }); return; }
    if (a.classList.contains('cst')) {
      var t = a.querySelector('b'); track('case_study_tab', { case_study: t ? t.textContent.trim() : label(a) }); return;
    }
    if (a.matches('.cs-cta, .cta-row .btn[data-industry]')) {
      var stage = a.closest('.cs-stage'), brand = stage && stage.querySelector('.cs-logo');
      track('case_study_cta', { case_study: brand ? (brand.getAttribute('alt') || brand.getAttribute('aria-label') || '').replace(/ logo$/i, '') : document.title, industry: a.getAttribute('data-industry') || '' });
    }
    if (a.matches('.btn-p, .btn-g, .mb-form, .cs-cta, .cs-more, .case-cta') && a.getAttribute('type') !== 'submit') {
      track('cta_click', { cta_text: label(a), cta_location: where(a), cta_destination: href.slice(0, 120) });
    }
  }, true);

  /* form_start: first focus inside each lead form */
  Array.prototype.forEach.call(doc.querySelectorAll('form[data-lead]'), function (f) {
    var started = false;
    f.addEventListener('focusin', function () { if (!started) { started = true; track('form_start', { form_location: where(f) }); } });
  });

  /* scroll depth on long-form pages */
  if (pageType === 'blog_post' || pageType === 'case_study') {
    var marks = [25, 50, 75, 100], hit = {};
    var onScroll = function () {
      var h = doc.documentElement, max = h.scrollHeight - win.innerHeight;
      if (max <= 0) return;
      var pct = (win.scrollY || h.scrollTop) / max * 100;
      for (var i = 0; i < marks.length; i++) {
        if (pct >= marks[i] - 1 && !hit[marks[i]]) { hit[marks[i]] = 1; track('scroll_depth', { percent: marks[i] }); }
      }
      if (hit[100]) win.removeEventListener('scroll', onScroll);
    };
    win.addEventListener('scroll', onScroll, { passive: true });
  }
})();
