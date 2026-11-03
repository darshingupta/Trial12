"""Build the deliverables for one sectional from its content module.

Usage: python3 build.py rc|lr OUTDIR
Writes OUTDIR/<prefix>_Paper.docx, OUTDIR/<prefix>_Answer_Key.docx and OUTDIR/<prefix>.html.
"""
import base64, importlib, json, os, sys
from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
which, OUT = sys.argv[1], sys.argv[2]
M = importlib.import_module(which)
P, META = M.P, M.META
os.makedirs(OUT, exist_ok=True)
LET = "abcd"
ROMAN = ["I", "II", "III", "IV", "V", "VI"]
INK = RGBColor(0x18, 0x21, 0x2C); MUT = RGBColor(0x5A, 0x65, 0x73)
ACC = RGBColor.from_string(META["accent_hex"])

CODES = {
 "X": ["Unearned absolute", "Needs 'only / every / never / always / no bearing at all', or turns the passage's 'may' into a fact. The passage never earns it."],
 "P": ["Part, not the whole", "True of one paragraph, one example or one cause, but not of the whole passage or the whole effect asked about."],
 "B": ["Too broad", "Turns this case into a rule about everything of its kind."],
 "W": ["Wrong weighting", "Gives a later consequence or a side point the role of the cause or thesis."],
 "A": ["Added idea", "Brings in a cause, motive, fact or remedy the passage never gives, often one that is plausible in the real world."],
 "N": ["Supported, not needed", "Plausible or even helpful, but the argument survives without it (assumption), or it backs a premise rather than the link asked about."],
 "R": ["Rival view or echo", "The view the author reports or rejects, or the passage's own words with the meaning shifted."],
 "L": ["Mix-up or reversal", "Swaps two things the passage keeps apart, contradicts a stated line, or helps the argument when the stem asks you to hurt it."],
 "E": ["NOT / EXCEPT reversal", "This option is supported (or does what the stem says the others do). Picking it means reading NOT or EXCEPT as if it were not there."],
 "O": ["Half-right option", "One half fits (often a word that echoes the passage); the other half, or the 'because' clause, is false."],
 "F": ["Word or figure misread", "The dictionary sense instead of the sense in context, a sound-alike, or the wrong figure of speech (simile vs metaphor vs personification)."],
 "T": ["Wrong target", "Bears on a side claim, a different mechanism or the outcome rather than the point the question names."],
 "K": ["Not forced", "On a must-be-true or necessary-condition question: one route that is possible, offered as if it were the only one."],
 "C": ["Correlation read as cause", "Treats an association, or a change caused by something else, as proof of the cause in question."],
 "S": ["The narrator taken at his word", "In fiction: accepts the narrator's own reading of events where the passage invites the reader to see past it."],
 "M": ["Clock or arithmetic slip", "Uses a raw camera time, adds an offset instead of subtracting it, or uses the wrong figure in a calculation."],
}

QS = [q for p in P for q in p["qs"]]
EX = importlib.import_module(which + "_ex").EX
for i, q in enumerate(QS, 1):
    q["n"] = i
    e = EX[i]
    assert set(e["r"]) == set(LET) - {q["ans"]}, f"Q{i}: reasons {sorted(e['r'])} vs key {q['ans']}"
    q["why"], q["src"] = e["why"], e["src"]
    q["reasons"] = dict(e["r"], **{q["ans"]: "Correct: see the explanation above."})
used = sorted({c for q in QS for c in q["traps"].values()})
def _rank(q):
    lens = [len(o.split()) for o in q["o"]]; k = LET.index(q["ans"])
    return sum(1 for x in lens if x > lens[k]) + 1, sum(1 for x in lens if x < lens[k]) == 0
LONGEST = sum(1 for q in QS if _rank(q)[0] == 1 and len(set(len(o.split()) for o in q["o"])) > 1)
SHORTEST = sum(1 for q in QS if _rank(q)[1] and len(set(len(o.split()) for o in q["o"])) > 1)
def fill(s): return s.replace("{LONGEST}", str(LONGEST)).replace("{SHORTEST}", str(SHORTEST)).replace("{NQ}", str(len(QS)))
for k in ("harder", "clat_types", "instructions"): META[k] = [fill(x) for x in META[k]]
for k in ("intro", "key_lede", "targets_lede"): META[k] = fill(META[k])


# ---------------------------------------------------------------- HTML test
def seal(obj, key):
    raw = json.dumps(obj, ensure_ascii=False).encode("utf-8")
    out = bytes(b ^ ((ord(key[i % len(key)]) + i * 7) % 256) for i, b in enumerate(raw))
    return base64.b64encode(out).decode()

def build_html():
    data = {"codes": {c: CODES[c] for c in used},
            "passages": [{"id": p["id"], "label": p["label"], "kind": p["kind"], "text": p["text"],
                          "qs": [{"stem": q["stem"], "o": q["o"]} for q in p["qs"]]} for p in P]}
    rev = {"key": [q["ans"] for q in QS], "traps": [q["traps"] for q in QS], "type": [q["type"] for q in QS],
           "why": [q.get("why", "") for q in QS], "reasons": [q.get("reasons", {}) for q in QS],
           "src": [q.get("src", "") for q in QS]}
    t = open(os.path.join(HERE, "template.html")).read()
    rep = {"__DATA__": json.dumps(data, ensure_ascii=False), "__SEAL__": json.dumps(seal(rev, META["sealkey"])),
           "__TITLE__": M.TITLE, "__MIN__": str(M.MINUTES), "__LSKEY__": META["lskey"], "__SEALKEY__": META["sealkey"],
           "__EYEBROW__": META["eyebrow"], "__INTRO__": META["intro"], "__NQ__": str(len(QS)), "__SHAPE__": META["shape"],
           "__SERIES__": META["series"], "__ACCENTNOTE__": META["accentnote"]}
    for a, b in rep.items():
        t = t.replace(a, b)
    for a, b in META.get("css", []):
        assert a in t, a
        t = t.replace(a, b)
    assert "__" not in t.replace("__proto__", ""), "unfilled placeholder"
    open(os.path.join(OUT, META["prefix"] + ".html"), "w").write(t)


# ---------------------------------------------------------------- Word helpers
def base_doc():
    d = Document()
    s = d.sections[0]
    s.page_height, s.page_width = Cm(29.7), Cm(21.0)
    s.left_margin = s.right_margin = Cm(2.0); s.top_margin = s.bottom_margin = Cm(1.8)
    st = d.styles["Normal"]; st.font.name = "Cambria"; st.font.size = Pt(10.5)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), "Cambria")
    st.paragraph_format.space_after = Pt(4)
    for name, size in (("Heading 1", 15), ("Heading 2", 12.5), ("Heading 3", 11)):
        h = d.styles[name]; h.font.name = "Calibri"; h.font.size = Pt(size); h.font.color.rgb = ACC; h.font.bold = True
        h.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
    p = s.footer.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(); f1 = OxmlElement("w:fldChar"); f1.set(qn("w:fldCharType"), "begin")
    it = OxmlElement("w:instrText"); it.text = "PAGE"; f2 = OxmlElement("w:fldChar"); f2.set(qn("w:fldCharType"), "end")
    r._r.append(f1); r._r.append(it); r._r.append(f2); r.font.size = Pt(9); r.font.color.rgb = MUT
    return d

def para(d, text, bold=False, italic=False, size=None, color=None, align=None, after=None, indent=None, before=None):
    p = d.add_paragraph()
    r = p.add_run(text); r.bold = bold; r.italic = italic
    if size: r.font.size = Pt(size)
    if color: r.font.color.rgb = color
    if align is not None: p.alignment = align
    if after is not None: p.paragraph_format.space_after = Pt(after)
    if before is not None: p.paragraph_format.space_before = Pt(before)
    if indent is not None: p.paragraph_format.left_indent = Cm(indent)
    return p

def shade(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr(); sh = OxmlElement("w:shd")
    sh.set(qn("w:val"), "clear"); sh.set(qn("w:color"), "auto"); sh.set(qn("w:fill"), hexcolor); tcPr.append(sh)

def table(d, header, rows, widths=None, size=9.5):
    t = d.add_table(rows=1, cols=len(header)); t.style = "Table Grid"; t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, h in enumerate(header):
        c = t.rows[0].cells[i]; c.text = h; shade(c, META["shade"]); c.paragraphs[0].runs[0].bold = True
        c.paragraphs[0].runs[0].font.size = Pt(size)
    for row in rows:
        cells = t.add_row().cells
        for i, v in enumerate(row):
            cells[i].text = str(v)
            for r in cells[i].paragraphs[0].runs: r.font.size = Pt(size)
    if widths:
        for row in t.rows:
            for i, w in enumerate(widths): row.cells[i].width = Cm(w)
    return t

def keep(p): p.paragraph_format.keep_with_next = True

def qrange(i):
    a = sum(len(p["qs"]) for p in P[:i]) + 1
    return a, a + len(P[i]["qs"]) - 1


# ---------------------------------------------------------------- Word paper
def build_paper():
    d = base_doc()
    para(d, M.TITLE.upper(), bold=True, size=24, color=ACC, align=WD_ALIGN_PARAGRAPH.CENTER, after=2)
    para(d, META["subtitle"], size=12.5, color=MUT, align=WD_ALIGN_PARAGRAPH.CENTER, after=16)
    t = d.add_table(rows=0, cols=2); t.style = "Table Grid"; t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for a, b in [("Questions", f"{len(QS)} ({META['shape']})"), ("Time", f"{M.MINUTES} minutes"),
                 ("Marking", "+1 right, −0.25 wrong, 0 blank"), ("Pattern", META["pattern"])]:
        c = t.add_row().cells; c[0].text = a; c[1].text = b; shade(c[0], META["shade"]); c[0].paragraphs[0].runs[0].bold = True
    para(d, "", after=6)
    d.add_heading("The passages", level=2)
    rows = []
    for i, p in enumerate(P):
        a, b = qrange(i); rows.append([ROMAN[i], p["kind"], f"{a}–{b}"])
    table(d, ["Passage", "Subject", "Questions"], rows, widths=[2.2, 10.5, 3])
    d.add_heading("Instructions", level=2)
    for c in META["instructions"]:
        d.add_paragraph(c, style="List Bullet")
    for i, p in enumerate(P):
        d.add_page_break()
        a, b = qrange(i)
        d.add_heading(f"{p['label']}  (Questions {a}–{b})", level=1)
        para(d, p["kind"].upper(), size=8.5, color=MUT, after=6)
        for t_ in p["text"]:
            x = para(d, t_, after=5); x.paragraph_format.line_spacing = 1.12
            x.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        para(d, "", after=2)
        for q in p["qs"]:
            s = d.add_paragraph(); keep(s); s.paragraph_format.space_before = Pt(8)
            r = s.add_run(f"{q['n']}. "); r.bold = True; r.font.color.rgb = ACC
            s.add_run(q["stem"])
            for k, o in enumerate(q["o"]):
                x = para(d, f"({LET[k].upper()})  {o}", after=1, indent=0.6)
                x.paragraph_format.first_line_indent = Cm(-0.6); x.paragraph_format.left_indent = Cm(1.2)
                if k < 3: keep(x)
    d.add_page_break()
    d.add_heading("Answer sheet", level=1)
    para(d, "Fill one bubble per question. Leave it blank to skip (no penalty).", color=MUT, after=8)
    cols = 3; per = -(-len(QS) // cols)
    t = d.add_table(rows=per, cols=cols); t.style = "Table Grid"
    for c in range(cols):
        for r in range(per):
            n = c * per + r + 1
            cell = t.rows[r].cells[c]
            cell.text = f"{n:>2}    Ⓐ  Ⓑ  Ⓒ  Ⓓ" if n <= len(QS) else ""
            for run in cell.paragraphs[0].runs: run.font.size = Pt(11)
    para(d, "", after=10)
    for lab in ["Right: ______", "Wrong: ______", "Skipped: ______", "Score (+1 / −0.25): ______", f"Time taken (limit {M.MINUTES}:00): ______"]:
        para(d, lab, after=6)
    d.save(os.path.join(OUT, META["prefix"] + "_Paper.docx"))


# ---------------------------------------------------------------- Word key
def build_key():
    d = base_doc()
    para(d, f"{M.TITLE.upper()}: ANSWER KEY AND SOLUTIONS", bold=True, size=17, color=ACC, after=4)
    para(d, META["key_lede"], color=MUT, after=10)

    d.add_heading("Answers at a glance", level=2)
    rows = []
    for i, p in enumerate(P):
        rows.append([f"{p['label']}: {p['kind']}", "   ".join(f"{q['n']}-{q['ans'].upper()}" for q in p["qs"])])
    table(d, ["Passage", "Answers"], rows, widths=[7.5, 9.5], size=10)

    d.add_heading("How the question types were chosen: CLAT 2022–2026", level=2)
    for line in META["clat_types"]:
        d.add_paragraph(line, style="List Bullet")
    d.add_heading("One step above CL mocks: what makes this paper harder", level=2)
    for line in META["harder"]:
        d.add_paragraph(line, style="List Bullet")

    d.add_heading("What this paper targets", level=2)
    para(d, META["targets_lede"], color=MUT, after=6)
    rows = []
    for c in used:
        qs_ = [str(q["n"]) for q in QS if c in q["traps"].values()]
        rows.append([f"{c}  {CODES[c][0]}", ", ".join(qs_), META["target_notes"].get(c, "")])
    table(d, ["Trap", "Distractor in Q", "Why it is here (from your CL mock review)"], rows, widths=[4.2, 3.6, 9.2], size=9)

    d.add_heading("Answers and traps", level=2)
    rows = []
    for q in QS:
        cells = [str(q["n"]), q["type"], q["ans"].upper()]
        for l in LET:
            cells.append("key" if l == q["ans"] else q["traps"][l])
        rows.append(cells)
    table(d, ["Q", "Type (CLAT form)", "Key", "A", "B", "C", "D"], rows, widths=[1, 6.6, 1.2, 1.4, 1.4, 1.4, 1.4], size=9)

    d.add_heading("Trap codes", level=2)
    for c in used:
        x = d.add_paragraph(style="List Bullet"); r = x.add_run(f"{c}  {CODES[c][0]}. "); r.bold = True; x.add_run(CODES[c][1])

    if META.get("audit"):
        d.add_heading("Blind-solve audit", level=2)
        for line in META["audit"]:
            d.add_paragraph(line, style="List Bullet")

    for i, p in enumerate(P):
        d.add_page_break()
        a, b = qrange(i)
        d.add_heading(f"{p['label']}: {p['kind']}  (Questions {a}–{b})", level=1)
        if p.get("note"):
            x = d.add_paragraph(); r = x.add_run("The passage in one line. "); r.bold = True; x.add_run(p["note"])
        for q in p["qs"]:
            k = LET.index(q["ans"])
            h = d.add_heading(f"Q{q['n']}.  {q['type']}  ·  Answer ({q['ans'].upper()})", level=3)
            para(d, q["stem"], italic=True, color=MUT, after=3)
            x = d.add_paragraph(); r = x.add_run("Correct option. "); r.bold = True; x.add_run(f"({q['ans'].upper()}) {q['o'][k]}")
            x = d.add_paragraph(); r = x.add_run("Why. "); r.bold = True; x.add_run(q.get("why", ""))
            for l in LET:
                if l == q["ans"]:
                    continue
                x = para(d, "", after=2, indent=0.5)
                r = x.add_run(f"({l.upper()}) {q['traps'][l]} · {CODES[q['traps'][l]][0]}: "); r.bold = True
                x.add_run(q.get("reasons", {}).get(l, ""))
            x = d.add_paragraph(); r = x.add_run("Modelled on. "); r.bold = True; r.font.color.rgb = MUT
            r2 = x.add_run(q.get("src", "")); r2.font.color.rgb = MUT
    d.save(os.path.join(OUT, META["prefix"] + "_Answer_Key.docx"))


if __name__ == "__main__":
    build_html(); build_paper(); build_key()
    print("built", META["prefix"], "->", OUT)
