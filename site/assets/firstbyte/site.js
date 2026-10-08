/* First Byte — site.js
   Homepage interactions: pixel canvases, number count-up, case-study tabs + deep links,
   "I need" chips, newsletter signup. Every feature is optional: pages without the
   matching markup simply skip it, and the page works without JavaScript. */
(function () {
  'use strict';
  var doc = document, win = window;
  doc.documentElement.classList.remove('no-js');
  doc.documentElement.classList.add('js');
  var reduce = !!(win.matchMedia && win.matchMedia('(prefers-reduced-motion: reduce)').matches);
  var raf = win.requestAnimationFrame ? win.requestAnimationFrame.bind(win) : function (f) { return setTimeout(function () { f(Date.now()); }, 16); };
  var caf = win.cancelAnimationFrame ? win.cancelAnimationFrame.bind(win) : clearTimeout;
  var now = function () { return (win.performance && performance.now) ? performance.now() : Date.now(); };
  var $ = function (sel, root) { return (root || doc).querySelector(sel); };
  var $$ = function (sel, root) { return Array.prototype.slice.call((root || doc).querySelectorAll(sel)); };
  var hasIO = typeof win.IntersectionObserver !== 'undefined';

  /* ---------- mobile menu: close after a link tap or Escape ---------- */
  $$('details.menu, details').forEach(function (d) {
    if (!$('.mnav', d)) return;
    $$('a', d).forEach(function (a) { a.addEventListener('click', function () { d.removeAttribute('open'); }); });
  });
  doc.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') $$('details[open]').forEach(function (d) { if ($('.mnav', d)) d.removeAttribute('open'); });
  });

  /* ---------- pixel canvases (hero + contact) ---------- */
  var cvs = $$('canvas[data-fx]');
  if (cvs.length) {
    var GAP = 14, RGB = [1, 246, 242];
    var mouse = cvs.map(function () { return { x: -9999, y: -9999 }; });
    var vis = cvs.map(function () { return true; });
    var loopId = 0, last = 0;
    cvs.forEach(function (cv, i) {
      var host = cv.parentElement;
      if (!host) return;
      host.addEventListener('pointermove', function (e) { var r = cv.getBoundingClientRect(); mouse[i] = { x: e.clientX - r.left, y: e.clientY - r.top }; });
      host.addEventListener('pointerleave', function () { mouse[i] = { x: -9999, y: -9999 }; });
    });
    var paint = function (t) {
      var dpr = Math.min(2, win.devicePixelRatio || 1), T = t * 0.001;
      cvs.forEach(function (cv, i) {
        if (!vis[i]) return;
        var w = cv.clientWidth, h = cv.clientHeight;
        if (!w || !h) return;
        if (cv.width !== Math.round(w * dpr) || cv.height !== Math.round(h * dpr)) { cv.width = Math.round(w * dpr); cv.height = Math.round(h * dpr); }
        var ctx = cv.getContext('2d');
        if (!ctx) return;
        ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
        ctx.clearRect(0, 0, w, h);
        var m = mouse[i], buckets = [], k, x, y;
        for (k = 0; k < 10; k++) buckets.push([]);
        for (y = GAP / 2; y < h; y += GAP) {
          for (x = GAP / 2; x < w; x += GAP) {
            var n = Math.sin(x * 0.011 + T * 0.7) + Math.sin(y * 0.017 - T * 0.5) + Math.sin((x - y) * 0.007 + T * 0.35) + Math.sin(Math.hypot(x - w * 0.3, y - h * 0.5) * 0.02 - T * 1.1);
            var v = (n + 4) / 8; v = v * v * v * v;
            var d = Math.hypot(x - m.x, y - m.y), p = d < 220 ? (1 - d / 220) : 0;
            var a = Math.min(1, v * 1.1 + p * p * 1.3);
            if (a < 0.06) continue;
            buckets[Math.min(9, Math.floor(a * 10))].push(x, y, a);
          }
        }
        for (k = 0; k < 10; k++) {
          var arr = buckets[k];
          if (!arr.length) continue;
          ctx.fillStyle = 'rgba(' + RGB[0] + ',' + RGB[1] + ',' + RGB[2] + ',' + ((k + 1) / 10 * 0.85).toFixed(2) + ')';
          ctx.beginPath();
          for (var j = 0; j < arr.length; j += 3) { var s = 1 + arr[j + 2] * (GAP * 0.42); ctx.rect(arr[j] - s / 2, arr[j + 1] - s / 2, s, s); }
          ctx.fill();
        }
      });
    };
    var loop = function (t) {
      loopId = 0;
      if (reduce) { paint(t); return; }
      if (doc.hidden || !vis.some(Boolean)) return;
      if (t - last > 32) { last = t; paint(t); }
      loopId = raf(loop);
    };
    var kick = function () { if (!loopId) loopId = raf(loop); };
    if (hasIO) {
      var cio = new IntersectionObserver(function (es) {
        es.forEach(function (e) { var i = cvs.indexOf(e.target); if (i > -1) { vis[i] = e.isIntersecting; if (e.isIntersecting) kick(); } });
      }, { threshold: 0 });
      cvs.forEach(function (cv) { cio.observe(cv); });
    }
    doc.addEventListener('visibilitychange', kick);
    win.addEventListener('resize', function () { if (reduce) paint(now()); else kick(); });
    kick();
  }

  /* ---------- "by the numbers" count-up ---------- */
  var band = $('.band');
  if (band) {
    var vals = $$('.st .v[data-n]', band);
    var setK = function (k) {
      vals.forEach(function (el) {
        var to = +el.getAttribute('data-n'), tn = el.firstChild;
        while (tn && tn.nodeType !== 3) tn = tn.nextSibling;
        if (tn) tn.nodeValue = tn.nodeValue.replace(/\d[\d,]*/, String(Math.round(to * k)));
      });
    };
    var run = function () {
      band.classList.add('go');
      if (reduce) { setK(1); return; }
      setK(0);
      var t0 = now(), dur = 1800;
      var step = function (t) { var p = Math.min(1, (t - t0) / dur); setK(1 - Math.pow(1 - p, 4)); if (p < 1) raf(step); };
      raf(step);
    };
    if (hasIO) {
      var bio = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { bio.disconnect(); run(); } }); }, { threshold: 0.2 });
      bio.observe(band);
    } else run();
  }

  /* ---------- case studies: tabs, auto-advance, metric count-up, deep links ---------- */
  var cases = $('#work');
  if (cases) {
    var tabs = $$('.cst[data-case]', cases), stages = $$('.cs-stage[data-stage]', cases);
    var ci = 0, auto = 0, mraf = 0, casesVis = true;
    var ids = stages.map(function (s) { return s.getAttribute('data-id'); });
    var fmt = function (el, k) {
      var v = +el.getAttribute('data-v') * k, d = +el.getAttribute('data-d') || 0;
      var num = d ? v.toFixed(d) : Math.round(v).toLocaleString('en-US');
      el.textContent = (el.getAttribute('data-p') || '') + num + (el.getAttribute('data-s') || '');
    };
    var countMets = function (stage) {
      var bs = $$('.met b[data-v]', stage);
      caf(mraf);
      if (reduce) { bs.forEach(function (b) { fmt(b, 1); }); return; }
      var t0 = now(), dur = 1600;
      var step = function (t) { var p = Math.min(1, (t - t0) / dur), k = 1 - Math.pow(1 - p, 3); bs.forEach(function (b) { fmt(b, k); }); if (p < 1) mraf = raf(step); };
      mraf = raf(step);
    };
    var pick = function (i, fromAuto) {
      if (i < 0 || i >= stages.length) return;
      ci = i;
      tabs.forEach(function (t, j) {
        var on = j === i;
        t.classList.toggle('on', on);
        t.setAttribute('aria-selected', on ? 'true' : 'false');
        t.setAttribute('tabindex', on ? '0' : '-1');
        if (on) { t.classList.remove('on'); void t.offsetWidth; t.classList.add('on'); } /* restart progress bar */
      });
      stages.forEach(function (s, j) { if (j === i) s.removeAttribute('hidden'); else s.setAttribute('hidden', ''); });
      countMets(stages[i]);
      if (!fromAuto) startAuto();
    };
    var startAuto = function () {
      clearInterval(auto);
      if (reduce) return;
      auto = setInterval(function () { if (!casesVis || doc.hidden) return; pick((ci + 1) % stages.length, true); }, 9000);
    };
    tabs.forEach(function (t, j) {
      t.addEventListener('click', function () { pick(j, false); });
      t.addEventListener('keydown', function (e) {
        var k = e.key, n = null;
        if (k === 'ArrowDown' || k === 'ArrowRight') n = (j + 1) % tabs.length;
        else if (k === 'ArrowUp' || k === 'ArrowLeft') n = (j - 1 + tabs.length) % tabs.length;
        else if (k === 'Home') n = 0; else if (k === 'End') n = tabs.length - 1;
        if (n !== null) { e.preventDefault(); pick(n, false); tabs[n].focus(); }
      });
    });
    if (hasIO) {
      var wio = new IntersectionObserver(function (es) { es.forEach(function (e) { casesVis = e.isIntersecting; }); }, { threshold: 0.2 });
      wio.observe(cases);
    }
    var onHash = function () {
      var id = (location.hash || '').slice(1);
      if (!id) return;
      var m = id.match(/^work-([a-z]+)$/);
      if (!m && id !== 'work') return;
      if (m) { var j = ids.indexOf(m[1]); if (j > -1) pick(j, false); }
      /* re-align a few times while fonts/images settle, unless the visitor starts scrolling */
      var stop = false, cancel = function () { stop = true; };
      win.addEventListener('wheel', cancel, { once: true, passive: true });
      win.addEventListener('touchstart', cancel, { once: true, passive: true });
      win.addEventListener('keydown', cancel, { once: true });
      var align = function () { if (stop) return; var el = doc.getElementById('work'); if (el) el.scrollIntoView({ block: 'start' }); };
      [30, 250, 700, 1400, 2400].forEach(function (t) { setTimeout(align, t); });
    };
    win.addEventListener('hashchange', onHash);
    /* same-page links to a case (e.g. footer) */
    doc.addEventListener('click', function (e) {
      var a = e.target && e.target.closest ? e.target.closest('a[href*="#work-"]') : null;
      if (!a) return;
      var u; try { u = new URL(a.href, location.href); } catch (er) { return; }
      if (u.pathname === location.pathname && u.hash === location.hash) { e.preventDefault(); onHash(); }
    });
    stages.forEach(function (s) { $$('.met b[data-v]', s).forEach(function (b) { fmt(b, 1); }); });
    onHash();
    startAuto();
  }

  /* ---------- "I need" chips -> hidden services field ---------- */
  $$('form').forEach(function (f) {
    var chips = $$('.need[data-need]', f), out = f.querySelector('input[name="services"][type="hidden"]');
    if (!chips.length || !out) return;
    var sync = function () { out.value = chips.filter(function (c) { return c.classList.contains('on'); }).map(function (c) { return c.getAttribute('data-need'); }).join(', '); };
    chips.forEach(function (c) {
      c.addEventListener('click', function () { var on = !c.classList.contains('on'); c.classList.toggle('on', on); c.setAttribute('aria-pressed', on ? 'true' : 'false'); sync(); });
    });
    sync();
  });

  /* ---------- forms: lead forms + #SundayByte newsletter ----------
     Posts to the site's own /api/contact endpoint (Cloudflare Worker → email to the team +
     lead inbox). If the site is hosted somewhere without that endpoint, it falls back to
     FormSubmit so no lead is ever lost. Without JavaScript the form still posts natively. */
  var FALLBACK = 'https://formsubmit.co/ajax/sean@firstbyte.agency';
  var showErr = function (f, msg) {
    var box = f.querySelector('.form-err');
    if (!box) {
      box = doc.createElement('p');
      box.className = 'form-err'; box.setAttribute('role', 'alert');
      box.style.cssText = 'grid-column:1/-1;margin:0;padding:12px 16px;border-radius:12px;border:1px solid rgba(255,94,94,.45);background:rgba(255,94,94,.08);color:#ffd2d2;font-size:15px;line-height:1.45';
      var btn = f.querySelector('button[type="submit"]');
      var host = btn && btn.parentElement && btn.parentElement !== f ? btn.parentElement : btn;
      if (host) f.insertBefore(box, host); else f.appendChild(box);
    }
    box.textContent = msg;
  };
  $$('form[action="/api/contact"]').forEach(function (f) {
    var isNews = f.getAttribute('data-ajax') === 'news';
    f.addEventListener('submit', function (e) {
      if (!win.fetch || !win.FormData || !win.Promise) return;          /* native POST */
      e.preventDefault();
      if (f.getAttribute('data-sending')) return;
      var data = {};
      new FormData(f).forEach(function (v, k) { if (typeof v === 'string' && v !== '') data[k] = data[k] ? data[k] + ', ' + v : v; });
      if (!data.page) data.page = doc.title + ' (' + location.pathname + ')';
      var btn = f.querySelector('button[type="submit"]');
      var busy = function (on) {
        if (on) f.setAttribute('data-sending', '1'); else f.removeAttribute('data-sending');
        if (btn) { btn.disabled = on; btn.style.opacity = on ? '.7' : ''; btn.setAttribute('aria-busy', on ? 'true' : 'false'); }
      };
      var done = function () {
        if (isNews) {
          f.setAttribute('hidden', '');
          var ok = f.parentElement ? f.parentElement.querySelector('.news-ok') : null;
          if (ok) ok.removeAttribute('hidden');
          busy(false);
        } else {
          try {
            win.dataLayer = win.dataLayer || [];
            win.dataLayer.push({ event: 'generate_lead', lead_offer: data.offer || '', lead_industry: data.industry || '', lead_ad_spend: data.ad_spend || '' });
            if (typeof win.gtag === 'function') win.gtag('event', 'generate_lead', { offer: data.offer || '', industry: data.industry || '', ad_spend: data.ad_spend || '' });
            if (typeof win.fbq === 'function') win.fbq('track', 'Lead');
            win.sessionStorage.setItem('fb_lead', JSON.stringify({ name: (data.name || '').split(' ')[0], email: data.email || '' }));
          } catch (_e) { /* tracking never blocks the redirect */ }
          location.href = '/thank-you/';
        }
      };
      var fail = function (msg) { busy(false); showErr(f, msg || 'We couldn’t send that. Please call (713) 578-0634 or email contact@firstbyte.agency.'); };
      var viaFormSubmit = function () {
        var d = {};
        Object.keys(data).forEach(function (k) { if (k !== '_v' && k !== '_honey' && k !== '_next') d[k] = data[k]; });
        d._template = 'table'; d._captcha = 'false';
        return fetch(FALLBACK, { method: 'POST', headers: { 'Content-Type': 'application/json', Accept: 'application/json' }, body: JSON.stringify(d) })
          .then(function (r) { if (!r.ok) throw new Error('fallback ' + r.status); done(); });
      };
      busy(true);
      fetch('/api/contact', { method: 'POST', headers: { 'Content-Type': 'application/json', Accept: 'application/json' }, body: JSON.stringify(data) })
        .then(function (r) {
          if (r.status === 404 || r.status === 405 || r.status === 501) return viaFormSubmit();
          return r.json().catch(function () { return {}; }).then(function (j) {
            if (r.ok && j.ok !== false) return done();
            if (r.status >= 500) return viaFormSubmit();
            fail(j.error);
          });
        })
        .catch(function () { return viaFormSubmit(); })
        .catch(function () { fail(); });
    });
  });
  /* ---------- Lead form: pre-select Industry ----------
     ?industry=<slug> in the URL, or a click on any link with data-industry="<slug>",
     selects that option in every lead form on the page (slugs: see tools/apply_lead_form.py). */
  var setIndustry = function (slug) {
    if (!slug) return;
    $$('form[data-lead] select[name="industry"]').forEach(function (sel) {
      var opt = $('option[data-slug="' + slug.replace(/[^a-z0-9-]/gi, '') + '"]', sel);
      if (opt) { sel.value = opt.value; sel.dispatchEvent(new Event('change', { bubbles: true })); }
    });
  };
  try { setIndustry(new URLSearchParams(location.search).get('industry')); } catch (_e) { /* old browsers */ }
  $$('a[data-industry]').forEach(function (a) {
    a.addEventListener('click', function () { setIndustry(a.getAttribute('data-industry')); });
  });

  /* ---------- Hero trust line: Google rating ----------
     Shown only when BOTH data-rating and data-count are filled in the HTML. */
  $$('.g-rating').forEach(function (g) {
    var r = (g.getAttribute('data-rating') || '').trim(), c = (g.getAttribute('data-count') || '').trim();
    if (!r || !c) return;
    var rb = $('.g-r', g), cb = $('.g-c', g);
    if (rb) rb.textContent = r;
    if (cb) cb.textContent = c;
    g.classList.add('on');
  });

  try {
    var lead = JSON.parse(win.sessionStorage.getItem('fb_lead') || 'null');
    var hi = $('[data-lead-name]');
    if (lead && lead.name && hi) { hi.textContent = lead.name; var wr = $('[data-lead-name-wrap]'); if (wr) wr.removeAttribute('hidden'); }
  } catch (_e) { /* no storage */ }
  /* ---------- Client results: drafts stay hidden until approved ----------
     ?preview=results shows draft cards (with a DRAFT label) for review. */
  if (/[?&]preview=results\b/.test(location.search)) doc.documentElement.classList.add('show-drafts');
  $$('.tcards').forEach(function (g) {
    var live = $$('.tc', g).filter(function (c) { return c.getAttribute('data-status') !== 'draft'; }).length;
    var show = live || doc.documentElement.classList.contains('show-drafts');
    var sec = g.closest('section');
    if (show && sec) sec.classList.add('has-results');
  });
  /* no-JS fallback error redirect: /contact/?sent=0 */
  if (/[?&]sent=0\b/.test(location.search)) {
    var cf = $('form[action="/api/contact"]');
    if (cf) showErr(cf, 'Sorry — that didn’t go through. Please check your name and email, or call (713) 578-0634.');
  }
})();
