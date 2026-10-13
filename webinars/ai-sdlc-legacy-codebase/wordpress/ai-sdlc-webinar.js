/*
 * AI SDLC on a Legacy Codebase — webinar page behaviour.
 * 1. Click-to-load YouTube player (no iframe until the visitor asks for it).
 * 2. Chapter links seek the embedded player; without JS they open YouTube at the timecode.
 * 3. HubSpot readiness-discovery form, with a visible fallback if it can't load.
 * 4. dataLayer events for GTM: cta_click, video_play, chapter_click,
 *    discovery_form_view, discovery_form_start, discovery_form_submit.
 */
(function () {
  'use strict';

  var dl = (window.dataLayer = window.dataLayer || []);
  function track(event, params) {
    var payload = { event: event, page_type: 'webinar', webinar: 'ai-sdlc-legacy-codebase' };
    for (var k in params) if (Object.prototype.hasOwnProperty.call(params, k)) payload[k] = params[k];
    dl.push(payload);
  }
  function isPlaceholder(value) { return !value || value.charAt(0) === '['; }

  /* ---------- CTA clicks ---------- */
  document.addEventListener('click', function (e) {
    var el = e.target.closest && e.target.closest('[data-ais-event]');
    if (el) track(el.getAttribute('data-ais-event'), { cta_label: el.getAttribute('data-ais-label') || '' });
  });

  /* ---------- video ---------- */
  var player = document.querySelector('.ais-video__player');
  var videoId = player && player.getAttribute('data-video-id');

  function loadVideo(start) {
    if (!player || isPlaceholder(videoId)) return false;
    var src = 'https://www.youtube-nocookie.com/embed/' + encodeURIComponent(videoId) +
      '?autoplay=1&rel=0&modestbranding=1' + (start ? '&start=' + start : '');
    var iframe = player.querySelector('iframe');
    if (!iframe) {
      iframe = document.createElement('iframe');
      iframe.title = 'AI SDLC on a Legacy Codebase: full webinar recording';
      iframe.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture';
      iframe.allowFullscreen = true;
      player.innerHTML = '';
      player.appendChild(iframe);
    }
    iframe.src = src;
    return true;
  }

  if (player) {
    var poster = player.querySelector('.ais-video__poster');
    if (poster) poster.addEventListener('click', function () {
      if (loadVideo(0)) track('video_play', { video_start: 0 });
    });
  }

  var chapterLinks = document.querySelectorAll('.ais-chapters a[data-start]');
  Array.prototype.forEach.call(chapterLinks, function (a) {
    a.addEventListener('click', function (e) {
      var start = parseInt(a.getAttribute('data-start'), 10);
      if (isNaN(start)) return;               // timecode not filled in yet: let the link open YouTube
      if (!loadVideo(start)) return;          // no video id yet: same
      e.preventDefault();
      Array.prototype.forEach.call(chapterLinks, function (x) { x.removeAttribute('aria-current'); });
      a.setAttribute('aria-current', 'true');
      track('chapter_click', { video_start: start, chapter: a.textContent.replace(/\s+/g, ' ').trim() });
      var top = player.getBoundingClientRect().top + window.pageYOffset - 100;
      if (window.innerWidth < 1200) window.scrollTo({ top: top, behavior: 'smooth' });
    });
  });

  /* ---------- HubSpot form ---------- */
  var formBox = document.getElementById('discovery-form');
  if (formBox) {
    var portalId = formBox.getAttribute('data-portal-id');
    var formId = formBox.getAttribute('data-form-id');
    var started = false;

    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (entries) {
        if (entries[0].isIntersecting) { track('discovery_form_view', {}); io.disconnect(); }
      }, { threshold: 0.4 });
      io.observe(formBox);
    }

    var createForm = function () {
      if (isPlaceholder(formId) || !window.hbspt || formBox.getAttribute('data-ready')) return;
      formBox.setAttribute('data-ready', '1');
      window.hbspt.forms.create({
        portalId: portalId,
        formId: formId,
        region: 'na1',
        target: '#discovery-form',
        onFormReady: function ($form) {
          var fallback = formBox.querySelector('.ais-discovery__fallback');
          if (fallback) fallback.remove();
          var form = $form && $form.jquery ? $form[0] : $form;
          if (form && form.addEventListener) form.addEventListener('focusin', function () {
            if (!started) { started = true; track('discovery_form_start', {}); }
          });
        },
        onFormSubmitted: function () { track('discovery_form_submit', {}); }
      });
    };

    if (!isPlaceholder(formId)) {
      if (window.hbspt) createForm();
      window.addEventListener('hubspot:ready', createForm); // the MobiDev theme fires this after lazy-loading HubSpot
    }
  }
})();
