/* Typographic audit for the presenting deck.
   Serve build output, open it, paste this in the console. Reports:
     overflow        - content past the 1280x720 safe area
     shortLastLine   - any wrapped block whose last line is under 40% of its longest line
     clipped         - text cut off by a fixed width or nowrap
   A block's line boxes are measured per character through a Range, because
   getClientRects() on a block element returns one border box, not line boxes -
   an earlier version of this check used that and silently reported nothing. */
(async () => {
  await document.fonts.ready;
  await Promise.all([...document.images].map(i => i.complete ? 0 : new Promise(r => { i.onload = i.onerror = r; })));

  const lineWidths = el => {
    const rows = [], r = document.createRange();
    const walk = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
    let n;
    while ((n = walk.nextNode())) {
      if (!n.nodeValue.trim()) continue;
      let p = n.parentElement, skip = false;
      while (p && p !== el) {                       // ignore absolutely-positioned children
        if (getComputedStyle(p).position === 'absolute') { skip = true; break; }
        p = p.parentElement;
      }
      if (skip) continue;
      const s = n.nodeValue;
      for (let i = 0; i < s.length; i++) {
        if (!s[i].trim()) continue;
        r.setStart(n, i); r.setEnd(n, i + 1);
        const b = r.getBoundingClientRect();
        if (!b.width && !b.height) continue;
        const hit = rows.find(x => Math.abs(x.top - b.top) < 3);
        if (hit) { hit.left = Math.min(hit.left, b.left); hit.right = Math.max(hit.right, b.right); }
        else rows.push({ top: b.top, left: b.left, right: b.right });
      }
    }
    return rows.sort((a, b) => a.top - b.top).map(x => x.right - x.left);
  };

  const st = document.createElement('style');
  st.textContent = '.s{transition:none !important}';
  document.head.appendChild(st);
  const stage = document.getElementById('stage');
  const prev = stage.style.transform;
  stage.style.transform = 'scale(1)';

  const TEXT = 'p,li,h1,h2,h3,.sd,.st,.td,.tt,.fl,.qt,.qd,.nt,.nd,.sn,.sv,.lede,.kick,.bigline,.tlc,.logo,.subject,.gh';
  const slides = [...document.querySelectorAll('.s')];
  const R = { overflow: [], shortLastLine: [], clipped: [] };

  slides.forEach((s, i) => {
    slides.forEach(x => x.classList.remove('on'));
    s.classList.add('on');
    void s.offsetHeight;
    const id = `${i + 1} ${s.dataset.t}`;
    const sr = stage.getBoundingClientRect();
    let bot = 0, rgt = 0;
    s.querySelectorAll('*').forEach(el => {
      const b = el.getBoundingClientRect();
      if (!b.width && !b.height) return;
      bot = Math.max(bot, b.bottom - sr.top);
      rgt = Math.max(rgt, b.right - sr.left);
      if (el.scrollWidth > el.clientWidth + 1 && getComputedStyle(el).overflow !== 'visible')
        R.clipped.push({ id, cls: el.getAttribute('class') || el.tagName });
    });
    if (bot > 632 || rgt > 1206)
      R.overflow.push({ id, bottom: Math.round(bot - 632), right: Math.round(rgt - 1206) });
    s.querySelectorAll(TEXT).forEach(el => {
      const t = el.textContent.replace(/\s+/g, ' ').trim();
      if (t.length < 6) return;
      const L = lineWidths(el);
      if (L.length < 2) return;
      const ratio = L[L.length - 1] / Math.max(...L);
      if (ratio < 0.40)
        R.shortLastLine.push({ id, cls: el.getAttribute('class') || el.tagName, lines: L.length, ratio: +ratio.toFixed(2), tail: t.slice(-40) });
    });
  });

  stage.style.transform = prev;
  st.remove();
  if (typeof show === 'function') show(0);
  console.table(R.overflow); console.table(R.shortLastLine); console.table(R.clipped);
  return `slides=${slides.length} overflow=${R.overflow.length} shortLastLine=${R.shortLastLine.length} clipped=${R.clipped.length}`;
})()
