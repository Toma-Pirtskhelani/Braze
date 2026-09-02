# -*- coding: utf-8 -*-
CSS = r"""
:root{
  --ink:#141821; --panel:#1C212C; --panel2:#232936;
  --vellum:#EDE9E1; --slate:#A6AFBE; --dim:#7B8698;
  --line:#263340; --line2:#3A4354;
  --strong:#6BAA75; --medium:#D9A441; --weak:#C9553F;
  --bar:#4A5567; --barlab:#8D97A8;
  --disp:"Instrument Serif",Georgia,serif;
  --body:"Libre Franklin",system-ui,sans-serif;
  --mono:"JetBrains Mono",ui-monospace,monospace;
}
*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%;overflow:hidden;background:#0B0E14}
body{font-family:var(--body);-webkit-font-smoothing:antialiased}
#viewport{position:fixed;inset:0;display:grid;place-items:center;
  background:radial-gradient(130% 95% at 50% -12%,#1B2029 0%,#0B0E14 72%)}
#stage{width:1280px;height:720px;position:relative;transform-origin:center center;
  background:var(--ink);box-shadow:0 44px 130px -30px rgba(0,0,0,.92),0 0 0 1px var(--line)}
/* Bottom padding was 88px, which left 45px of clear air between the content box and the
   top of the ledger and pushed five slides into overflow for the sake of it. 74px keeps
   31px of clearance - still more than the ledger needs - and buys every slide 14px. */
section.s{position:absolute;inset:0;padding:56px 74px 74px;opacity:0;visibility:hidden;
  transition:opacity .3s ease,transform .3s ease;transform:translateY(8px);display:flex;flex-direction:column}
section.s.on{opacity:1;visibility:visible;transform:none}
@media (prefers-reduced-motion:reduce){section.s{transition:none}}

h1{font-family:var(--disp);font-weight:400;color:var(--vellum);line-height:1.0;letter-spacing:-.02em;text-wrap:balance}
h2{font-family:var(--disp);font-weight:400;font-size:46px;color:var(--vellum);line-height:1.05;letter-spacing:-.01em;text-wrap:balance}
h3{font-family:var(--body);font-weight:600;font-size:15px;color:var(--vellum);text-wrap:balance}
.eyebrow{font-family:var(--mono);font-size:10.5px;letter-spacing:.24em;text-transform:uppercase;
  color:var(--dim);display:flex;align-items:center;gap:11px}
.eyebrow::before{content:"";width:20px;height:1px;background:var(--line2)}
.head{flex:none;margin-bottom:26px}
.head h2{margin-top:13px;max-width:24ch}
.head .kick{margin-top:13px;font-size:18px;line-height:1.45;color:var(--slate);max-width:70ch;font-weight:400;text-wrap:balance}
.head .kick strong{color:var(--vellum);font-weight:600}
.body{flex:1;min-height:0;display:flex;flex-direction:column;gap:14px;justify-content:center}
p{font-size:16px;line-height:1.55;color:var(--slate);text-wrap:balance}
strong{color:var(--vellum);font-weight:600}
.mono{font-family:var(--mono)}

/* title */
.title-s{justify-content:center;padding-left:104px;padding-right:104px}
.title-s .mark{width:50px;margin-bottom:24px}
.title-s h1{font-size:108px;line-height:.94}
.title-s .subject{font-family:var(--mono);font-size:18px;letter-spacing:.28em;text-transform:uppercase;
  color:var(--slate);margin-top:20px}
.title-s .lede{font-size:19px;line-height:1.5;color:var(--slate);margin-top:26px;white-space:nowrap}
.title-s .srcstrip{display:grid;grid-template-columns:repeat(6,1fr);gap:0;margin-top:48px;
  border-top:1px solid var(--line2)}
.title-s .srcitem{padding:16px 20px 0 0}
.title-s .sn{font-family:var(--mono);font-size:9.5px;letter-spacing:.12em;text-transform:uppercase;
  color:var(--dim);line-height:1.55;white-space:nowrap}
.title-s .sv{font-size:16px;color:var(--vellum);font-weight:500;line-height:1.3;margin-top:3px;
  font-variant-numeric:tabular-nums;white-space:nowrap}
.title-s .byline{display:flex;justify-content:space-between;align-items:baseline;margin-top:44px;
  font-size:15px;color:var(--dim)}
.title-s .byline strong{color:var(--vellum);font-weight:600}

/* .body already spaces its children with gap, so the 20px margin here was double-counted. */
.ruleband{border-top:1px solid var(--line2);padding-top:22px;margin-top:4px}
.ruleband .klabel{display:block;margin-bottom:14px}

/* self-guided demo links */
.demo{display:flex;align-items:baseline;gap:10px;margin-top:10px}
.demo .dn{font-size:14.5px;color:var(--vellum);font-weight:600;flex:none}
.demo a{font-family:var(--mono);font-size:11.5px;letter-spacing:.03em;word-break:break-all}

/* brand assets */
.brandtag{position:absolute;top:52px;right:74px;background:#fff;border-radius:10px;
  padding:14px 16px;display:grid;place-items:center}
.brandtag img{display:block;width:100%;height:auto}
.plate{background:#fff;border-radius:10px;padding:16px 18px;display:grid;place-items:center;flex:none}
.plate img{display:block;width:100%;height:auto}
.portrait{width:120px;height:120px;flex:none;display:block;border-radius:50%;background:#8BA0FF}
.figurehead{display:flex;gap:18px;align-items:center}
.figurehead .fname{font-size:17px;color:var(--vellum);font-weight:600;line-height:1.25}
.figurehead .frole{font-family:var(--mono);font-size:10px;letter-spacing:.1em;color:var(--medium);text-transform:uppercase;margin-top:7px}
.figurehead .fnote{font-size:14px;color:var(--slate);line-height:1.45;margin-top:9px}
.figurehead .fedu{font-family:var(--mono);font-size:10px;letter-spacing:.04em;color:var(--dim);
  line-height:1.6;margin-top:10px}

.brandmark{display:block;margin-bottom:20px}
.brandmark circle,.brandmark path{vector-effect:non-scaling-stroke}

/* divider */
.div-s{justify-content:center;padding-left:104px}
.div-s .pn{font-family:var(--mono);font-size:12px;letter-spacing:.3em;color:var(--medium);text-transform:uppercase}
.div-s h2{font-size:70px;margin-top:14px}
.div-s ul{margin-top:30px;list-style:none;display:grid;gap:11px;max-width:64ch}
.div-s li{font-size:18.5px;color:var(--slate);padding-left:34px;position:relative;line-height:1.4;text-wrap:balance}
.div-s li .qn{position:absolute;left:0;top:4px;font-family:var(--mono);font-size:10.5px;color:var(--medium);letter-spacing:.08em}
.div-s .foot{margin-top:34px;font-family:var(--mono);font-size:10.5px;letter-spacing:.15em;color:var(--dim);text-transform:uppercase}

/* figures - the one big-number component */
.figrow{display:grid;gap:16px;align-items:start}
.fig{display:flex;flex-direction:column;gap:9px}
.fig .fv{font-family:var(--disp);font-size:58px;color:var(--vellum);line-height:.95;letter-spacing:-.02em}
.fig .fv em{font-style:normal;font-size:.62em;color:var(--dim)}
.fig .fl{font-family:var(--mono);font-size:10px;letter-spacing:.09em;text-transform:uppercase;color:var(--dim);line-height:1.4;text-wrap:balance}
.fig.sm .fv{font-size:40px} .fig.lg .fv{font-size:78px}
.fig.neg .fv{color:var(--weak)}
.fig.dim .fv{color:var(--slate);opacity:.72} .fig.dim .fl{opacity:.72}
.fig.boxed{background:var(--panel);border:1px solid var(--line);border-radius:4px;padding:20px 22px}

/* tag label used on cards and section blocks */
.klabel{font-family:var(--mono);font-size:10px;letter-spacing:.15em;text-transform:uppercase;color:var(--dim);font-weight:400}
.klabel.acc{color:var(--medium)}
.klabel.colhead{display:block;margin-bottom:12px;min-height:1.4em}

/* the seven-stage pipeline on the Part II divider */
.pipeline{display:grid;grid-template-columns:repeat(7,1fr);gap:9px;margin-top:56px;max-width:1072px}
.pipeline .step{padding:20px 16px}
.pipeline .si{font-size:11px}
.pipeline .st{font-size:17px;margin-top:11px}

/* stats */
.statrow{display:grid;gap:14px}
.stat{background:var(--panel);border:1px solid var(--line);border-radius:4px;padding:20px 22px}
.stat .n{font-family:var(--disp);font-size:46px;color:var(--vellum);line-height:1;letter-spacing:-.02em}
.stat.huge .n{font-size:64px}
.stat .l{font-family:var(--mono);font-size:10px;letter-spacing:.08em;text-transform:uppercase;color:var(--dim);margin-top:10px;line-height:1.35}

/* tiles */
.tiles{display:grid;gap:14px}
.tile{background:var(--panel);border:1px solid var(--line);border-radius:4px;padding:18px 20px}
.tile .ti{line-height:0;color:var(--medium)}
.ico{display:block}
.tile .tt{font-size:16px;color:var(--vellum);font-weight:600;margin-top:11px}
.tile .td{font-size:14px;color:var(--slate);margin-top:6px;line-height:1.4;text-wrap:balance}

/* grade tiles */
.tile.grade{padding:26px 24px}
.tile.grade .gh{font-family:var(--body);font-weight:600;font-size:19px;color:var(--vellum);margin-top:14px;line-height:1.3}
.tile.grade .td{margin-top:12px;font-size:15px}

/* delivery routing table */
.routegrid{display:grid;gap:8px}
.routehead,.route{display:grid;grid-template-columns:34px 118px 26px 1fr 108px 160px;align-items:center;gap:10px}
.routehead span{font-family:var(--mono);font-size:9px;letter-spacing:.13em;text-transform:uppercase;color:var(--dim)}
.route{background:var(--panel);border:1px solid var(--line);border-radius:4px;padding:13px 16px}
.route .ri{color:var(--medium);line-height:0}
.route .rn{font-size:16px;color:var(--vellum);font-weight:600}
.route .rarrow{color:var(--line2);font-size:15px}
.route .rv{font-size:15px;color:var(--slate)}
.route .rc{font-family:var(--mono);font-size:11px;letter-spacing:.05em;color:var(--dim)}
.route .rc-w{color:var(--weak)} .route .rc-s{color:var(--strong)}
.route .rr{font-family:var(--mono);font-size:11px;color:var(--dim);text-align:right}

/* a figure band, anchored on a rule rather than floating */
.figband{border-top:1px solid var(--line2);padding-top:16px}
.figband .klabel{display:block;margin-bottom:14px}

.vsrc{display:inline-block;margin-top:8px;font-family:var(--mono);font-size:10px;letter-spacing:.06em;color:var(--dim)}
.vsrc.bought{color:var(--strong)}

.tourgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.tourcard{background:var(--panel);border:1px solid var(--line);border-left:2px solid var(--medium);border-radius:4px;padding:22px 22px 20px;display:flex;flex-direction:column}
.tourcard .tlv{font-family:var(--mono);font-size:10px;letter-spacing:.13em;text-transform:uppercase;color:var(--medium)}
.tourcard .tt{font-family:var(--disp);font-size:28px;color:var(--vellum);line-height:1.15;margin-top:12px;text-wrap:balance}
.tourcard .tdd{font-size:15px;color:var(--slate);line-height:1.5;margin-top:11px;text-wrap:balance;flex:1}
.tourcard a{display:block;font-family:var(--mono);font-size:11px;letter-spacing:.01em;margin-top:16px;word-break:break-all}

.tourstrip{border-top:1px solid var(--line2);padding-top:15px;display:flex;align-items:baseline;gap:18px}
.tourstrip .tsl{font-family:var(--mono);font-size:10px;letter-spacing:.13em;text-transform:uppercase;color:var(--dim);flex:1 1 100%}
.tourstrip .tsn{font-size:17px;color:var(--vellum);font-weight:600}
.tourstrip a{font-family:var(--mono);font-size:12px;letter-spacing:.02em}

/* channels */
.chgrid{display:grid;grid-template-columns:repeat(9,1fr);gap:9px}
.chan{background:var(--panel);border:1px solid var(--line);border-radius:4px;padding:16px 12px 14px;
  display:flex;flex-direction:column;align-items:flex-start;gap:11px}
.chan .ci{color:var(--medium);line-height:0}
.chan .cn{font-size:14px;color:var(--vellum);font-weight:600;line-height:1.2;min-height:1.2em}
.chan .cd{font-family:var(--mono);font-size:9px;letter-spacing:.05em;color:var(--dim);line-height:1.45;margin-top:-4px}

/* numbered findings */
.numgrid{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(3,auto);grid-auto-flow:column;gap:16px 40px}
.num{display:flex;gap:15px;align-items:baseline;border-top:1px solid var(--line);padding-top:12px}
.num .ni{font-family:var(--mono);font-size:11px;color:var(--medium);flex:none;letter-spacing:.1em}
.num .nt{font-size:16px;color:var(--vellum);font-weight:600;line-height:1.25}
.num .nd{font-size:13.5px;color:var(--dim);line-height:1.4;margin-top:5px}

/* bars */
/* Row pitch was 26px track + 13px gap. On an 8- or 11-row chart that alone pushed three
   slides past the safe line. 24 + 10 reads identically at presentation size and gives a
   tall chart back ~40px. */
.bars{display:grid;gap:10px}
.barrow{display:flex;align-items:center;gap:14px}
.bl{font-family:var(--mono);font-size:11px;color:var(--barlab);width:172px;flex:none;letter-spacing:.04em;line-height:1.3}
.bt{flex:1;height:24px;background:var(--line);border-radius:3px;overflow:hidden}
.bf{height:100%;border-radius:3px}
.bv{font-family:var(--mono);font-size:15px;width:62px;text-align:right;flex:none;color:var(--slate)}

/* flow */
.flow{display:grid;gap:7px}
.step{background:var(--panel);border:1px solid var(--line);border-radius:4px;padding:14px 12px}
.step.key{background:var(--panel2);border-color:var(--medium)}
.step.mk-s{background:var(--panel2);border-color:var(--strong)}
.step.mk-m{background:var(--panel2);border-color:var(--medium)}
.step.mk-w{background:var(--panel2);border-color:var(--weak)}
.step.mk-s .si{color:var(--strong)} .step.mk-m .si{color:var(--medium)} .step.mk-w .si{color:var(--weak)}
.step .si{font-family:var(--mono);font-size:10px;color:var(--dim);letter-spacing:.1em}
.step.key .si{color:var(--medium)}
.step .st{font-size:14px;color:var(--vellum);margin-top:8px;line-height:1.3;font-weight:600;text-wrap:balance}
.step .sd{font-family:var(--mono);font-size:10px;color:var(--slate);margin-top:7px;line-height:1.35;text-wrap:balance}

/* timeline */
.timeline{display:grid;gap:0;position:relative}
.timeline::before{content:"";position:absolute;left:0;right:0;top:34px;height:1px;background:var(--line2)}
.timeline.has-total::before{right:var(--tlcut)}
.tlitem{position:relative;padding-top:56px;padding-right:14px}
.tlitem::before{content:"";position:absolute;left:0;top:29px;width:11px;height:11px;border-radius:50%;
  background:var(--medium);border:2px solid var(--ink)}
.tld{position:absolute;top:0;left:0;font-family:var(--mono);font-size:10.5px;color:var(--dim);letter-spacing:.08em}
.tlv{font-family:var(--disp);font-size:32px;color:var(--vellum);line-height:1}
.tlc{font-size:13px;color:var(--slate);margin-top:7px;line-height:1.35;text-wrap:balance}
/* the accumulation: off the line, boxed, and summed rather than plotted */
.tlitem.tot{padding-left:22px;padding-right:0;border-left:1px solid var(--line2)}
.tlitem.tot::before{display:none}
.tlitem.tot .tld{left:22px;color:var(--medium)}
.tlitem.tot .tlv{color:var(--medium)}

/* separates a timeline from what follows it */
.tlband{padding-bottom:22px;border-bottom:1px solid var(--line)}

/* logos */
.logos{display:grid;gap:9px}
/* A split column is a narrower, taller frame than a full-width body, and the default
   card paddings overflow it on the two slides that stack seven logos or four tiles down
   one side. Tightened only inside .split, so full-width uses keep their air. */
.split .logos{gap:7px}
.split .logo{padding:11px 8px}
.split .tiles{gap:11px}
.split .tile{padding:14px 16px}
.split .tile .tt{margin-top:8px}

.logo{background:var(--panel);border:1px solid var(--line);border-radius:4px;padding:14px 8px;
  text-align:center;font-size:13.5px;color:var(--slate);font-weight:500}
.logo.acc{border-color:var(--medium);color:var(--vellum)}

/* cards */
.cards{display:grid;gap:14px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:4px;padding:18px 20px;border-left:2px solid var(--line2)}
.card.g{border-left-color:var(--strong)} .card.a{border-left-color:var(--medium)} .card.r{border-left-color:var(--weak)}
.card h3{margin-bottom:8px} .card p{font-size:14.5px;text-wrap:balance}

.quote{font-family:var(--disp);font-size:19px;line-height:1.32;color:var(--vellum);margin-top:10px;text-wrap:balance}

/* Sparse slides fill their frame instead of floating in it.
   A body carrying only one or two blocks leaves 150-290px of the stage unused, and a
   centred lump of small type in an empty frame reads as an unfinished slide rather
   than as a restrained one. Nothing is added to fix that: the hero element is simply
   sized to the space it has. Quantity query - ":nth-child(-n+2):last-child" matches a
   body whose last child is among its first two, i.e. one with two children or fewer.

   The bound is deliberately TWO and not three. A three-block body is usually already
   near full - a chart, a figure row and a rule band - and scaling its type pushed five
   slides into overflow, where content spills past the safe line and collides with the
   footer. Anything wider than this needs measuring, not guessing. */
.body:has(> :nth-child(-n+2):last-child) > .quote{font-size:29px;line-height:1.3}
.body:has(> :nth-child(-n+2):last-child) > p{font-size:19px;line-height:1.55}
.body:has(> :nth-child(-n+2):last-child) .fig.sm .fv{font-size:52px}
.body:has(> :nth-child(-n+2):last-child) .fig .fl{font-size:12px}
/* the quote body is a BLOCK. It was briefly given class="q", which is the question-backlog
   flex row - that turned every <strong> inside a quote into a flex item on one nowrap line. */
.quote .qbody{display:block}

/* big line */
.bigline{font-family:var(--disp);font-size:44px;line-height:1.16;color:var(--vellum);max-width:28ch;text-wrap:balance}
.bigline em{font-style:normal;color:var(--medium)}
.bigsub{font-size:17px;color:var(--slate);margin-top:20px;max-width:64ch;line-height:1.5;text-wrap:balance}
.split{display:grid;gap:26px;align-items:center}

/* map */
.mapwrap{width:100%;display:grid;place-items:center}
.worldsvg{width:100%;max-width:610px;height:auto;display:block}
.wd circle{fill:var(--line2);opacity:.85}
.pin{fill:var(--medium)}
.pin.p-s{fill:var(--strong)} .pin.p-w{fill:var(--weak)}
.halo{fill:none;stroke:var(--medium);stroke-width:.34;opacity:.55}
.halo.p-s{stroke:var(--strong)} .halo.p-w{stroke:var(--weak)}
.pinlab{fill:var(--vellum);font-family:var(--mono);font-size:1.95px;letter-spacing:.05em;
  paint-order:stroke;stroke:var(--ink);stroke-width:.55px;stroke-linejoin:round}

.maplegend{display:flex;gap:26px;flex-wrap:wrap;justify-content:center;font-family:var(--mono);font-size:10px;
  letter-spacing:.06em;color:var(--dim);margin-top:-6px}
.maplegend span{display:flex;align-items:center;gap:8px}
.maplegend .lg{width:8px;height:8px;border-radius:50%;display:block;flex:none}
.maplegend .lg-s{background:var(--strong)} .maplegend .lg-m{background:var(--medium)}
.maplegend .lg-w{background:var(--weak)}
.maplegend .lgnote{font-style:italic;letter-spacing:.03em;opacity:.8}

/* chrome */
#ledger{position:absolute;left:74px;right:74px;bottom:32px;display:flex;gap:3px;align-items:flex-end;height:11px}
#ledger .tk{flex:1;height:2px;background:var(--line);border-radius:1px;transition:all .25s ease;cursor:pointer}
#ledger .tk.seen{background:var(--line2)}
#ledger .tk.cur{height:9px}
#ledger .tk.cur[data-g="s"]{background:var(--strong)}
#ledger .tk.cur[data-g="m"]{background:var(--medium)}
#ledger .tk.cur[data-g="w"]{background:var(--weak)}
#counter{position:absolute;right:74px;bottom:50px;font-family:var(--mono);font-size:10px;color:var(--dim);letter-spacing:.1em}
#label{position:absolute;left:74px;bottom:50px;font-family:var(--mono);font-size:10px;color:var(--dim);letter-spacing:.1em}

/* notes */
#notes{position:fixed;right:0;top:0;bottom:0;width:420px;background:#10141B;border-left:1px solid var(--line2);
  padding:26px 26px 30px;overflow:auto;z-index:70;transform:translateX(100%);transition:transform .22s ease}
#notes.on{transform:none}
#notes h4{font-family:var(--mono);font-size:10px;letter-spacing:.18em;color:var(--medium);text-transform:uppercase;margin-bottom:14px}
#notes .nb{font-size:15px;line-height:1.62;color:var(--slate);white-space:pre-wrap}
#notes .nb strong{color:var(--vellum)}
#grid{position:fixed;inset:0;background:rgba(11,14,20,.985);z-index:80;padding:30px;overflow:auto;display:none}
#grid.on{display:block}
#grid .gg{display:grid;grid-template-columns:repeat(7,1fr);gap:10px;max-width:1560px;margin:0 auto}
#grid .gi{aspect-ratio:16/9;background:var(--panel);border:1px solid var(--line);border-radius:4px;padding:10px;
  cursor:pointer;display:flex;flex-direction:column;justify-content:space-between;transition:.15s}
#grid .gi:hover{border-color:var(--medium);background:var(--panel2)}
#grid .gn{font-family:var(--mono);font-size:9px;color:var(--dim)}
#grid .gt{font-size:10.5px;color:var(--vellum);line-height:1.3}
#grid h4{font-family:var(--mono);font-size:11px;letter-spacing:.2em;color:var(--dim);text-transform:uppercase;text-align:center;margin-bottom:20px}
#help{position:fixed;left:18px;bottom:14px;font-family:var(--mono);font-size:10px;color:#3B424F;z-index:60}
#help b{color:#5D6675}

/* four-question backlog */
.bqgrid{display:grid;gap:20px;max-width:1000px}
.bq{display:flex;gap:26px;align-items:baseline;border-bottom:1px solid var(--line);padding-bottom:20px}
.bq .bqn{font-family:var(--mono);font-size:13px;color:var(--medium);flex:none;letter-spacing:.1em}
.bq .bqt{font-family:var(--disp);font-size:33px;color:var(--vellum);line-height:1.2;text-wrap:balance}

/* question backlog */
.qgrid{display:grid;grid-template-columns:1fr 1fr;gap:9px 26px}
.q{display:flex;gap:12px;align-items:baseline;border-bottom:1px solid var(--line);padding-bottom:7px}
.qn{font-family:var(--mono);font-size:10px;color:var(--medium);flex:none;letter-spacing:.08em;padding-top:2px}
.qt{font-size:14.5px;color:var(--vellum);font-weight:600;line-height:1.3}
.qd{font-size:12.5px;color:var(--dim);line-height:1.35;margin-top:3px}
a{color:var(--medium)}
"""
