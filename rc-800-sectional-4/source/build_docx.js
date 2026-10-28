// Builds the question paper and the separate answer key (A4) from content.json.
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, ShadingType,
  AlignmentType, BorderStyle, PageBreak, Footer, PageNumber, LevelFormat, HeadingLevel,
  TabStopType, VerticalAlign,
} = require("docx");

const C = JSON.parse(fs.readFileSync(path.join(__dirname, "content.json"), "utf8"));
const OUT = path.join(__dirname, "..");
const L = "abcd";
const INK = "1A2230", MUTED = "5A6676", ACCENT = "23477A", RULE = "C9D1DC", SOFT = "E8EEF6", GREEN = "E1F1E7";
const SERIF = "Cambria", SANS = "Calibri";
const PAGE_W = 11906, MARGIN = 1134, TEXT_W = PAGE_W - 2 * MARGIN; // A4, 2 cm margins

const run = (text, o = {}) => new TextRun({ text, font: o.font || SERIF, size: o.size || 22, bold: o.bold, italics: o.italics, color: o.color || INK });
const para = (children, o = {}) => new Paragraph({
  children: Array.isArray(children) ? children : [children],
  spacing: { before: o.before ?? 0, after: o.after ?? 120, line: o.line ?? 288 },
  alignment: o.align, indent: o.indent, keepNext: o.keepNext, keepLines: true,
  border: o.border, heading: o.heading, numbering: o.numbering, pageBreakBefore: o.pageBreakBefore,
});
const h = (text, o = {}) => para(run(text, { font: SANS, size: o.size || 28, bold: true, color: o.color || INK }),
  { before: o.before ?? 240, after: o.after ?? 120, keepNext: true, heading: o.heading, pageBreakBefore: o.pageBreakBefore,
    border: o.rule ? { bottom: { style: BorderStyle.SINGLE, size: 6, color: RULE, space: 4 } } : undefined });
const label = (text) => para(run(text.toUpperCase(), { font: SANS, size: 17, bold: true, color: MUTED }), { after: 60, keepNext: true });

const border = { style: BorderStyle.SINGLE, size: 4, color: RULE };
const borders = { top: border, bottom: border, left: border, right: border };
function cell(content, w, o = {}) {
  const kids = (Array.isArray(content) ? content : [content]).map(c => typeof c === "string"
    ? para(run(c, { font: o.font || SANS, size: o.size || 20, bold: o.bold, color: o.color }), { after: 0, line: 252, align: o.align })
    : c);
  return new TableCell({ children: kids, width: { size: w, type: WidthType.DXA }, borders,
    shading: o.fill ? { type: ShadingType.CLEAR, color: "auto", fill: o.fill } : undefined,
    margins: { top: 70, bottom: 70, left: 110, right: 110 }, verticalAlign: o.valign || VerticalAlign.CENTER, columnSpan: o.span });
}
function table(widths, rows) {
  return new Table({ width: { size: widths.reduce((a, b) => a + b, 0), type: WidthType.DXA }, columnWidths: widths,
    rows: rows.map((r, i) => new TableRow({ children: r, tableHeader: i === 0, cantSplit: true })) });
}
const footer = (title) => new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [
  new TextRun({ text: title + "  ·  page ", font: SANS, size: 16, color: MUTED }),
  new TextRun({ children: [PageNumber.CURRENT], font: SANS, size: 16, color: MUTED })] })] });
const numbering = { config: [{ reference: "bul", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
  style: { paragraph: { indent: { left: 360, hanging: 240 } } } }] },
  { reference: "num", levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT,
  style: { paragraph: { indent: { left: 360, hanging: 300 } } } }] }] };
const styles = { default: { document: { run: { font: SERIF, size: 22, color: INK } } } };

function questionBlock(q, withKey) {
  const out = [];
  out.push(para([run(`${q.n}. `, { font: SANS, bold: true }), run(q.stem, { font: SANS, bold: true })], { before: 200, after: 80, keepNext: true }));
  if (q.quote) out.push(para(run(q.quote, { italics: true }), { indent: { left: 400, right: 400 }, after: 80, keepNext: true }));
  if (q.after) out.push(para(run(q.after, { font: SANS, bold: true }), { after: 80, keepNext: true }));
  q.opts.forEach((t, i) => {
    const isKey = withKey && L[i] === q.key;
    out.push(para([run(`(${L[i]})\t`, { font: SANS, bold: true, color: isKey ? "2A7A4D" : INK }), run(t, { bold: isKey })],
      { indent: { left: 567, hanging: 567 }, after: 60, keepNext: i < 3 }));
  });
  return out;
}

/* ============================================================ QUESTION PAPER */
function paper() {
  const kids = [];
  kids.push(para(run("CLAT · ENGLISH LANGUAGE · READING COMPREHENSION", { font: SANS, size: 18, bold: true, color: MUTED }), { before: 1400, after: 120 }));
  kids.push(para(run("RC 800 Sectional 4", { font: SERIF, size: 60, bold: true }), { after: 120 }));
  kids.push(para(run("Four passages, 24 questions, Countdown CLAT formats at GMAT 800 / CAT difficulty", { font: SERIF, size: 26, italics: true, color: MUTED }), { after: 480,
    border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: ACCENT, space: 10 } } }));
  const fw = [2600, TEXT_W - 2600];
  kids.push(table(fw, [
    [cell("Format", fw[0], { bold: true, fill: SOFT }), cell("Detail", fw[1], { bold: true, fill: SOFT })],
    [cell("Questions", fw[0]), cell("24 (4 passages × 6 questions)", fw[1])],
    [cell("Time", fw[0]), cell("45 minutes", fw[1])],
    [cell("Marking", fw[0]), cell("+1 for a right answer, −0.25 for a wrong answer, 0 for a blank", fw[1])],
    ...C.passages.map((p, i) => [cell(`Passage ${i + 1} (Q${i * 6 + 1}–${i * 6 + 6})`, fw[0]), cell(p.kind, fw[1])]),
  ]));
  kids.push(h("Instructions", { size: 24, before: 360 }));
  [
    "Read each passage and answer the six questions that follow it. Each question has exactly one best answer.",
    "Every passage carries at least one strengthen or weaken question and at least one assumption or conclusion question. Answer each from the passage and the information in the question alone.",
    "Questions on a word, a line or a paragraph refer to the passage directly above them. Count paragraphs from the top of the passage.",
    "Mark your answers on the answer sheet at the end of the paper by filling in one bubble per question. A question with more than one bubble filled counts as wrong.",
    "Time yourself strictly: stop at 45:00. Then score the sheet with the separate answer key: +1 right, −0.25 wrong, 0 blank.",
  ].forEach(t => kids.push(para(run(t), { numbering: { reference: "num", level: 0 }, after: 80 })));
  const nw = [2600, TEXT_W - 2600];
  kids.push(para(run(""), { after: 200 }));
  kids.push(table(nw, ["Name", "Date", "Start time", "Finish time"].map(x => [cell(x, nw[0], { bold: true }), cell(" ", nw[1])])));

  C.passages.forEach((p, i) => {
    kids.push(para(run(p.kind.toUpperCase(), { font: SANS, size: 17, bold: true, color: MUTED }), { pageBreakBefore: true, after: 40, keepNext: true }));
    kids.push(h(`Passage ${i + 1}`, { size: 30, before: 0, rule: true }));
    p.text.forEach(t => kids.push(para(run(t, { size: 22 }), { align: AlignmentType.JUSTIFIED, after: 140, line: 300 })));
    kids.push(h(`Questions ${i * 6 + 1}–${i * 6 + 6}`, { size: 22, before: 240, color: ACCENT }));
    p.qs.forEach(q => questionBlock(q, false).forEach(x => kids.push(x)));
  });

  // Answer sheet
  kids.push(para(run("ANSWER SHEET", { font: SANS, size: 17, bold: true, color: MUTED }), { pageBreakBefore: true, after: 40, keepNext: true }));
  kids.push(h("RC 800 Sectional 4", { size: 30, before: 0, rule: true }));
  kids.push(para(run("Fill in one bubble per question. Leave a question blank rather than guess if you cannot eliminate at least two options.", { size: 20, color: MUTED }), { after: 200 }));
  const qw = 520, bw = 430, gap = 300; // two blocks of 12 rows side by side
  const block = (from) => [...Array(12)].map((_, r) => from + r);
  const widths = [qw, bw, bw, bw, bw, gap, qw, bw, bw, bw, bw];
  const head = [cell("Q", qw, { bold: true, fill: SOFT, align: AlignmentType.CENTER }), ...L.split("").map(l => cell(l, bw, { bold: true, fill: SOFT, align: AlignmentType.CENTER })),
    new TableCell({ children: [new Paragraph("")], width: { size: gap, type: WidthType.DXA }, borders: { top: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" }, bottom: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" }, left: border, right: border } }),
    cell("Q", qw, { bold: true, fill: SOFT, align: AlignmentType.CENTER }), ...L.split("").map(l => cell(l, bw, { bold: true, fill: SOFT, align: AlignmentType.CENTER }))];
  const left = block(1), right = block(13);
  const rows = [head, ...left.map((n, r) => {
    const m = right[r];
    const bub = () => cell("○", bw, { align: AlignmentType.CENTER, size: 26 });
    return [cell(String(n), qw, { bold: true, align: AlignmentType.CENTER, fill: (n - 1) % 6 < 6 && Math.floor((n - 1) / 6) % 2 ? "F4F6F9" : undefined }), bub(), bub(), bub(), bub(),
      new TableCell({ children: [new Paragraph("")], width: { size: gap, type: WidthType.DXA }, borders: { top: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" }, bottom: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" }, left: border, right: border } }),
      cell(String(m), qw, { bold: true, align: AlignmentType.CENTER, fill: Math.floor((m - 1) / 6) % 2 ? "F4F6F9" : undefined }), bub(), bub(), bub(), bub()];
  })];
  kids.push(table(widths, rows));
  kids.push(para(run("Shaded question numbers mark Passages 2 and 4.", { size: 17, color: MUTED, font: SANS }), { before: 80, after: 280 }));
  const sw = [3600, 1600, 1600, TEXT_W - 6800];
  kids.push(table(sw, [
    [cell("Scoring", sw[0], { bold: true, fill: SOFT }), cell("Count", sw[1], { bold: true, fill: SOFT }), cell("× mark", sw[2], { bold: true, fill: SOFT }), cell("Score", sw[3], { bold: true, fill: SOFT })],
    [cell("Right", sw[0]), cell("______", sw[1]), cell("× (+1)", sw[2]), cell("= ________", sw[3])],
    [cell("Wrong", sw[0]), cell("______", sw[1]), cell("× (−0.25)", sw[2]), cell("= ________", sw[3])],
    [cell("Blank", sw[0]), cell("______", sw[1]), cell("× 0", sw[2]), cell("= 0", sw[3])],
    [cell("Net score (out of 24)", sw[0], { bold: true }), cell("", sw[1]), cell("", sw[2]), cell("= ________", sw[3], { bold: true })],
    [cell("Time taken (mm:ss)", sw[0], { bold: true }), cell("", sw[1]), cell("", sw[2]), cell("________", sw[3])],
  ]));
  return new Document({ creator: "RC 800", title: "RC 800 Sectional 4: Question Paper", styles, numbering,
    sections: [{ properties: { page: { size: { width: PAGE_W, height: 16838 }, margin: { top: MARGIN, bottom: MARGIN, left: MARGIN, right: MARGIN } } },
      footers: { default: footer("RC 800 Sectional 4 · Question paper") }, children: kids }] });
}

/* ============================================================ ANSWER KEY */
function key() {
  const kids = [];
  const all = C.passages.flatMap(p => p.qs);
  kids.push(para(run("ANSWER KEY · KEEP SEPARATE FROM THE PAPER", { font: SANS, size: 18, bold: true, color: MUTED }), { after: 80 }));
  kids.push(para(run("RC 800 Sectional 4", { font: SERIF, size: 52, bold: true }), { after: 80 }));
  kids.push(para(run("Answers, trap codes and full explanations", { size: 26, italics: true, color: MUTED }), { after: 300,
    border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: ACCENT, space: 10 } } }));

  kids.push(h("1. Answers at a glance", { size: 26 }));
  const gw = [3300, ...Array(6).fill((TEXT_W - 3300) / 6)];
  kids.push(table(gw, [
    [cell("Passage", gw[0], { bold: true, fill: SOFT }), ...[1, 2, 3, 4, 5, 6].map(i => cell(`Q ${i}`, gw[i], { bold: true, fill: SOFT, align: AlignmentType.CENTER }))],
    ...C.passages.map((p, pi) => [cell(`${p.label}: ${p.kind}`, gw[0]), ...p.qs.map((q, j) => cell(`${q.n}  ${q.key}`, gw[j + 1], { bold: true, align: AlignmentType.CENTER, font: SANS }))]),
  ]));
  const cnt = { a: 0, b: 0, c: 0, d: 0 }; all.forEach(q => cnt[q.key]++);
  kids.push(para(run(`Key spread: a ${cnt.a}, b ${cnt.b}, c ${cnt.c}, d ${cnt.d}. The key is the longest option in 6 questions, the second longest in 6, the third longest in 6 and the shortest in 6.`, { size: 19, color: MUTED, font: SANS }), { before: 80 }));

  kids.push(h("2. What this paper targets", { size: 26 }));
  kids.push(para(run("Each row is a trap family from your error log and the questions where a wrong option is built on it.", { size: 20 }), { after: 100 }));
  const fam = {}; all.forEach(q => q.codes.forEach(c => { if (c !== "K") (fam[c] = fam[c] || new Set()).add(q.n); }));
  const order = ["X", "P", "B", "W", "A", "N", "R", "L", "E", "O", "F", "G", "T", "M"];
  const tw = [700, 3200, TEXT_W - 3900];
  kids.push(table(tw, [[cell("Code", tw[0], { bold: true, fill: SOFT }), cell("Trap family", tw[1], { bold: true, fill: SOFT }), cell("Questions with a distractor built on it", tw[2], { bold: true, fill: SOFT })],
    ...order.filter(c => fam[c]).map(c => [cell(c, tw[0], { bold: true, align: AlignmentType.CENTER }), cell(C.codes[c][0], tw[1]), cell([...fam[c]].sort((a, b) => a - b).map(n => "Q" + n).join(", "), tw[2])])]));
  kids.push(para(run("Question types", { font: SANS, bold: true, size: 21 }), { before: 200, after: 80, keepNext: true }));
  const types = {}; all.forEach(q => (types[q.type] = types[q.type] || []).push(q.n));
  const yw = [3600, TEXT_W - 3600];
  kids.push(table(yw, [[cell("Type", yw[0], { bold: true, fill: SOFT }), cell("Questions", yw[1], { bold: true, fill: SOFT })],
    ...Object.entries(types).map(([t, ns]) => [cell(t, yw[0]), cell(ns.map(n => "Q" + n).join(", "), yw[1])])]));
  kids.push(para(run("Critical reasoning inside RC, as you asked: strengthen/weaken in every passage (Q2, Q8, Q14, Q20, plus the would-NOT-support Q6) and assumption or conclusion in every passage (Q3, Q9, Q15, Q21). To make room, this paper drops the logical-sequence and author's-approach types and has one detail-why and one quoted-line question instead of two each.", { size: 19, color: MUTED, font: SANS }), { before: 80 }));

  kids.push(h("3. Answers and traps", { size: 26, pageBreakBefore: true }));
  kids.push(para(run("Key marked ✓. Every other cell names the trap that wrong option is built on.", { size: 20 }), { after: 100 }));
  const aw = [700, 3300, 800, ...Array(4).fill((TEXT_W - 4800) / 4)];
  kids.push(table(aw, [
    [cell("Q", aw[0], { bold: true, fill: SOFT, align: AlignmentType.CENTER }), cell("Type", aw[1], { bold: true, fill: SOFT }), cell("Key", aw[2], { bold: true, fill: SOFT, align: AlignmentType.CENTER }),
      ...L.split("").map((l, i) => cell(`(${l})`, aw[3 + i], { bold: true, fill: SOFT, align: AlignmentType.CENTER }))],
    ...all.map(q => [cell(String(q.n), aw[0], { align: AlignmentType.CENTER, bold: true }), cell(q.type, aw[1]), cell(q.key, aw[2], { bold: true, align: AlignmentType.CENTER }),
      ...q.codes.map((c, i) => cell(c === "K" ? "✓" : c, aw[3 + i], { align: AlignmentType.CENTER, bold: c === "K", fill: c === "K" ? GREEN : undefined }))]),
  ]));

  kids.push(h("4. Trap code legend", { size: 26 }));
  const lw = [700, 2700, TEXT_W - 3400];
  kids.push(table(lw, [[cell("Code", lw[0], { bold: true, fill: SOFT }), cell("Trap", lw[1], { bold: true, fill: SOFT }), cell("What it does", lw[2], { bold: true, fill: SOFT })],
    ...order.map(c => [cell(c, lw[0], { bold: true, align: AlignmentType.CENTER }), cell(C.codes[c][0], lw[1]), cell(C.codes[c][1], lw[2])])]));

  kids.push(h("5. Full explanations", { size: 26, pageBreakBefore: true }));
  C.passages.forEach((p, pi) => {
    kids.push(h(`${p.label}: ${p.kind}`, { size: 23, color: ACCENT, before: pi ? 360 : 120, rule: true }));
    p.qs.forEach(q => {
      kids.push(label(`Q${q.n} · ${q.type}`));
      questionBlock(q, true).forEach(x => kids.push(x));
      const ki = L.indexOf(q.key);
      kids.push(para([run("Correct option: ", { font: SANS, bold: true, color: "2A7A4D" }), run(`(${q.key}). `, { bold: true }), run(q.reasons[ki])], { before: 100, after: 80 }));
      kids.push(para(run(q.why, { size: 21 }), { after: 80 }));
      kids.push(para(run("Why the other options fail", { font: SANS, bold: true, size: 20 }), { after: 40, keepNext: true }));
      q.opts.forEach((_, i) => { if (i === ki) return;
        kids.push(para([run(`(${L[i]}) · ${q.codes[i]} (${C.codes[q.codes[i]][0]}): `, { font: SANS, bold: true, size: 20 }), run(q.reasons[i], { size: 21 })],
          { numbering: { reference: "bul", level: 0 }, after: 40 })); });
      kids.push(para([run("Modelled on: ", { font: SANS, bold: true, size: 19, color: MUTED }), run(q.src, { size: 19, color: MUTED, italics: true })], { before: 60, after: 200,
        border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: RULE, space: 8 } } }));
    });
  });
  return new Document({ creator: "RC 800", title: "RC 800 Sectional 4: Answer Key", styles, numbering,
    sections: [{ properties: { page: { size: { width: PAGE_W, height: 16838 }, margin: { top: MARGIN, bottom: MARGIN, left: MARGIN, right: MARGIN } } },
      footers: { default: footer("RC 800 Sectional 4 · Answer key") }, children: kids }] });
}

(async () => {
  fs.writeFileSync(path.join(OUT, "RC_800_Sectional_4_Paper.docx"), await Packer.toBuffer(paper()));
  fs.writeFileSync(path.join(OUT, "RC_800_Sectional_4_Answer_Key.docx"), await Packer.toBuffer(key()));
  console.log("written");
})();
