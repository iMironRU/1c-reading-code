#!/usr/bin/env python3
"""Печатный PDF: вёрстка по канону серии (docs/style-guide.md, разделы 15–17).

Обычная сборка pandoc для печати не годится: нужны шмуцтитулы с метками,
листинги с линейками, схемы без линеек, рубрики прописными, обратная
адресация ответов и запрет разрыва между меткой и кодом. Часть этого
делается разметкой до pandoc, часть — правкой готового .tex, поэтому
шаг собран в отдельный скрипт, а не в ключи pandoc.

    ./book.sh print            собрать печатный PDF
    ./book.sh print --keep     оставить промежуточные .tex и дерево

Движок берётся первый из найденных: tectonic, xelatex, lualatex.
"""
import argparse
import os
import re
import shutil
import subprocess
import sys
import pathlib
import datetime

import yaml

ROOT = pathlib.Path(".").resolve()
STAGE = ROOT / ".build-print"
OUT = ROOT / "dist"
REG = ROOT / "assets/qr/registry.yaml"
IMG = ROOT / "assets/qr/img"
HEADER = ROOT / "assets/print/header.tex"

CODE_LANGS = {"bsl", "запрос", "python", "javascript", "csharp", "java", "sql",
              "powershell", "bash", "yaml", "ini", "json", "xml"}
FENCE = re.compile(r"^```([^\n]*)\n(.*?)^```[ \t]*$", re.S | re.M)
FRONT = re.compile(r"\A---\n.*?\n---\n", re.S)
HEAD = re.compile(r"^#{1,5}\s")
CAMEL = re.compile(r"(?<=[а-яa-z])(?=[А-ЯA-Z])")
RUBRICS = ("Главное", "Контрольные вопросы", "Упражнения", "Ответы", "Открытие")
TEXHEAD = re.compile(r"\\(section|subsection)\{(.*?)\}\\label\{[^}]*\}", re.S)


def engine():
    for name, cmd in (("tectonic", ["tectonic", "-X", "compile"]),
                      ("xelatex", ["xelatex"]), ("lualatex", ["lualatex"])):
        if shutil.which(name):
            return name, cmd
    return None, None


def status_of(text):
    m = re.search(r"^---.*?status:\s*(\w+).*?---", text, re.S)
    return m.group(1) if m else "ready"


def keep(status, flt):
    return (flt == "all" or (flt == "review" and status in ("ready", "review"))
            or (flt == "ready" and status == "ready"))


def shift(text):
    out, fence = [], False
    for line in text.split("\n"):
        if re.match(r"^\s*(```|~~~)", line):
            fence = not fence
        if not fence and HEAD.match(line):
            line = "#" + line
        out.append(line)
    return "\n".join(out)


def typeset(text, rel, listings):
    """Листинг — в окружение с линейками и меткой, схема — без линеек.

    Метка подвешена к верхней линейке, а не стоит в поле сама по себе,
    и \\needspace не даёт странице порваться между ними."""
    n = [0]

    def one(m):
        lang, body = m.group(1).strip(), m.group(2)
        if lang.split(",")[0] not in CODE_LANGS:
            return "\\schemetop\n\\begin{Plain}\n" + body + "\\end{Plain}\n"
        if "песочница" in lang:
            n[0] += 1
            code = listings.get((rel, n[0]))
            top = "\\qrmark{%s}" % code if code else "\\plaintop"
        elif "ловушка" in lang:
            top = "\\trapmark"
        else:
            top = "\\plaintop"
        return top + "\n\\begin{Code}\n" + body + "\\end{Code}\n"

    return FENCE.sub(one, text)


def stage(meta, flt, chapters_qr):
    shutil.rmtree(STAGE, ignore_errors=True)
    STAGE.mkdir()
    modules = meta.get("modules") or {}
    order, n = [], 0

    front = ROOT / "front"
    if front.is_dir():
        for f in sorted(front.glob("*.md")):
            text = f.read_text(encoding="utf-8")
            if not keep(status_of(text), flt):
                continue
            body = FRONT.sub("", text)
            title = (re.search(r"^#\s+(.+)$", body, re.M) or [None, ""])[1].strip()
            body = re.sub(r"^#\s+.+$", "", body, count=1, flags=re.M)
            n += 1
            p = STAGE / f"{n:03d}_0_front.md"
            p.write_text(f"# {title} {{.unnumbered}}\n{shift(body)}", encoding="utf-8")
            order.append(p)

    for d in sorted(x for x in (ROOT / "chapters").iterdir() if x.is_dir()):
        files = [f for f in sorted(d.glob("*.md")) if not f.name.startswith("_")]
        files = [f for f in files if keep(status_of(f.read_text(encoding="utf-8")), flt)]
        if not files:
            continue
        n += 1
        title = re.sub(r"^(Модуль|Глава|Часть|Раздел)\s+\d+\.\s*", "",
                       str(modules.get(d.name, d.name))).strip()
        code = chapters_qr.get(d.name)
        qr = "\n\\chapterqr{%s}\n" % code if code else ""
        p = STAGE / f"{n:03d}_0_chapter.md"
        p.write_text(f"# {title}\n\n\\chapterlist\n{qr}", encoding="utf-8")
        order.append(p)
        for i, f in enumerate(files, 1):
            rel = str(f.relative_to(ROOT))
            q = STAGE / f"{n:03d}_{i:02d}_{f.name}"
            q.write_text(typeset(shift(FRONT.sub("", f.read_text(encoding="utf-8"))),
                                 rel, LISTINGS), encoding="utf-8")
            order.append(q)
    return order, n


def colophon(meta):
    commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                            capture_output=True, text=True).stdout.strip() or "—"
    rows = [("КНИГА", meta.get("title", "")), ("СЕРИЯ", meta.get("series", "")),
            ("АВТОР", meta.get("author", "")),
            ("ВЕРСИЯ ТЕКСТА", "\\texttt{%s}" % meta.get("version", "")),
            ("СБОРКА", "\\texttt{%s} · %s" % (commit, datetime.date.today().strftime("%d.%m.%Y"))),
            ("ФОРМАТ", meta.get("pdf", {}).get("print_trim", "170 × 240 мм")),
            ("ШРИФТЫ", "%s, %s" % (meta.get("pdf", {}).get("font_main", ""),
                                   meta.get("pdf", {}).get("font_mono", "")))]
    body = "\\\\[4pt]\n".join("{\\sffamily\\footnotesize %s} & %s" % r for r in rows)
    p = STAGE / "999_colophon.md"
    p.write_text("""\\cleardoublepage
\\thispagestyle{plain}
\\markboth{Выходные данные}{Выходные данные}
\\vspace*{0pt}

\\noindent{\\sffamily\\bfseries\\small ВЫХОДНЫЕ ДАННЫЕ}

\\vspace{12pt}

\\noindent\\begin{tabular}{@{}p{34mm}p{74mm}@{}}
%s \\\\
\\end{tabular}

\\vspace{16pt}
\\noindent\\rule{\\textwidth}{0.8pt}
\\vspace{8pt}

\\noindent Бумага — срез, а книга живёт дальше. Журнал изменений начинается
с версии \\texttt{%s} — с той, что у вас в руках, — и показывает только то,
что появилось позже.
""" % (body, meta.get("version", "")), encoding="utf-8")
    return p


# ─── Правки готового .tex ────────────────────────────────────────────────────
def breakable_tt(s):
    """Длинные имена не переносятся внутри \\texttt и лезут в поле. Рвём по
    точке, скобке, заглавной букве и экранированному пробелу — без дефиса:
    дефис внутри имени читается как часть имени."""
    key, out, i, n = "\\texttt{", [], 0, len(s)
    while True:
        j = s.find(key, i)
        if j < 0:
            out.append(s[i:])
            return "".join(out)
        out.append(s[i:j + len(key)])
        depth, k = 1, j + len(key)
        while k < n and depth:
            c = s[k]
            if c == "\\":
                k += 2
                continue
            depth += (c == "{") - (c == "}")
            k += 1
        body = s[j + len(key):k - 1]
        body = CAMEL.sub("\\\\allowbreak{}", body)
        body = body.replace(".", ".\\allowbreak{}").replace("(", "(\\allowbreak{}")
        body = body.replace("\\ ", "\\ \\allowbreak{}")
        out.append(body + "}")
        i = k


def fit_tables(s):
    """Колонки «l» не переносят текст и вылезают в поле. Делим полосу
    пропорционально самой длинной ячейке столбца, шапку — рубленым."""
    def one(m):
        spec, body = m.group(1), m.group(0)
        nc = len(spec)
        w = [1] * nc
        for r in re.findall(r"^(.*?)\\\\$", body, re.M):
            cells = r.split("&")
            if len(cells) == nc:
                for i, c in enumerate(cells):
                    w[i] = max(w[i], len(re.sub(r"\\[a-zA-Z]+|[{}\\]", "", c).strip()))
        tot = sum(w)
        cols = "".join(
            r">{\raggedright\arraybackslash}p{(\linewidth - %d\tabcolsep) * \real{%.4f}}"
            % (2 * nc, 0.96 * x / tot) for x in w)
        body = body.replace("{@{}%s@{}}" % spec, "{@{}%s@{}}" % cols, 1)

        def head(hm):
            cells = hm.group(1).split("&")
            return ("\n" + "&".join(r"{\sffamily\bfseries\scriptsize\MakeUppercase{%s}}"
                                    % c.strip() for c in cells) + r"\\")
        return re.sub(r"\n(.*?)\\\\(?=\s*\\midrule)", head, body, count=1)

    return re.sub(r"\\begin\{longtable\}\[\]\{@\{\}([lcr]{2,})@\{\}\}.*?\\end\{longtable\}",
                  one, s, flags=re.S)


def rubrics(s):
    """Канонические рубрики — прописными с линейкой; у «Упражнений» метка,
    чтобы ответы могли сослаться на страницу."""
    cur = {"n": None}

    def one(m):
        kind, title = m.group(1), " ".join(m.group(2).split())
        if kind == "section":
            k = re.match(r"§\s*(\d+\.\d+)", title)
            if k:
                cur["n"] = k.group(1)
                return "\\section{%s}\\label{par:%s}" % (title, k.group(1))
            return "\\section{%s}" % title
        if any(title.startswith(r) for r in RUBRICS):
            lab = "\\label{ex:%s}" % cur["n"] if title.startswith("Упражнения") and cur["n"] else ""
            return "\\rubric{%s}%s" % (title, lab)
        if title.startswith("§"):
            return "\\rubric{%s}" % title
        return "\\subsection{%s}" % title

    return TEXHEAD.sub(one, s)


def answer_groups(s):
    def one(m):
        t = " ".join(m.group(1).split())
        k = re.match(r"§\s*(\d+\.\d+)", t)
        return "\\answergroup{%s}{%s}" % (t, k.group(1)) if k else m.group(0)
    return re.sub(r"\\rubric\{(§[^}]*)\}", one, s, flags=re.S)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--filter", default=None, choices=["ready", "review", "all"])
    ap.add_argument("--keep", action="store_true", help="оставить .tex и дерево сборки")
    args = ap.parse_args()

    name, cmd = engine()
    if not name:
        sys.exit("не найден ни tectonic, ни xelatex, ни lualatex — печатный PDF пропущен")

    meta = yaml.safe_load((ROOT / "metadata.yaml").read_text(encoding="utf-8"))
    pdf = meta.get("pdf") or {}
    flt = args.filter or meta.get("release_filter") or "review"

    global LISTINGS
    LISTINGS, chapters_qr = {}, {}
    if REG.exists():
        reg = yaml.safe_load(REG.read_text(encoding="utf-8")) or {}
        for code, v in (reg.get("codes") or {}).items():
            if v.get("retired"):
                continue
            if v["kind"] == "песочница":
                LISTINGS[(v["file"], v["ord"])] = code
            elif v["kind"] == "глава":
                chapters_qr[os.path.basename(v["file"])] = code

    order, nchap = stage(meta, flt, chapters_qr)
    if not order:
        sys.exit("нет файлов для сборки с выбранным фильтром")
    order.append(colophon(meta))
    print(f"глав: {nchap}, файлов: {len(order)}")

    OUT.mkdir(exist_ok=True)
    slug = meta.get("slug") or ROOT.name
    tex = OUT / f"{slug}_print.tex"
    geom = pdf.get("print_geometry") or (
        "paperwidth=170mm,paperheight=240mm,textwidth=110mm,textheight=192mm,"
        "inner=22mm,top=22mm,marginparwidth=27mm,marginparsep=4mm,twoside")
    subprocess.run([
        "pandoc", *[str(p) for p in order],
        "--metadata-file", str(ROOT / "metadata.yaml"),
        "--top-level-division=chapter", "--toc", "--toc-depth=2",
        "--standalone", "--strip-comments",
        "-V", "documentclass=book", "-V", "classoption=twoside",
        "-V", "classoption=openright", "-V", f"geometry:{geom}",
        "-V", f"mainfont={pdf.get('font_main', 'PT Serif')}",
        "-V", f"sansfont={pdf.get('font_sans', 'PT Sans')}",
        "-V", f"monofont={pdf.get('font_mono', 'PT Mono')}",
        "-V", f"fontsize={pdf.get('font_size', '11pt')}",
        "-V", "indent=true", "-V", "lang=ru", "-V", "colorlinks=false",
        "-H", str(HEADER), "-o", str(tex),
    ], check=True)

    tex.write_text(answer_groups(rubrics(fit_tables(breakable_tt(tex.read_text())))))

    # картинки меток лежат рядом с реестром, а движок ищет их рядом с .tex
    if IMG.is_dir():
        link = OUT / "qr"
        if not link.exists():
            os.symlink(IMG, link)

    run = cmd + ([str(tex), "--outdir", str(OUT), "--keep-logs"] if name == "tectonic"
                 else ["-interaction=nonstopmode", f"-output-directory={OUT}", str(tex)])
    r = subprocess.run(run, capture_output=True, text=True)
    pdfout = tex.with_suffix(".pdf")
    if not pdfout.exists():
        sys.stderr.write((r.stderr or r.stdout)[-2000:])
        sys.exit(f"{name} не собрал PDF")

    log = tex.with_suffix(".log")
    if log.exists():
        t = log.read_text(errors="replace")
        pages = re.search(r"\((\d+) pages", t)
        over = len(re.findall(r"Overfull \\hbox \((\d+)", t))
        print(f"страниц: {pages.group(1) if pages else '?'}, "
              f"вылетов за полосу: {over}")
    print(f"→ {pdfout}")

    if not args.keep:
        shutil.rmtree(STAGE, ignore_errors=True)
        for ext in (".tex", ".log", ".aux", ".toc", ".out", ".xdv"):
            p = tex.with_suffix(ext)
            if p.exists() and ext != ".pdf":
                p.unlink()


if __name__ == "__main__":
    main()
