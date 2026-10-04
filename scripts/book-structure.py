#!/usr/bin/env python3
"""Структура книги для сборки: вводная часть, шмуцтитулы глав, порядок файлов.

Параграф в исходнике начинается с заголовка первого уровня — «# § 1.1. …».
Если отдать такие файлы pandoc как есть, каждый параграф станет главой: в
EPUB — отдельным разделом оглавления, в PDF — шмуцтитулом. Глав при этом не
будет вовсе, потому что их названия живут только в `metadata.yaml`.

Скрипт готовит дерево для сборки:

- файлы из `front/` идут первыми, ненумерованными главами — это вводная
  часть книги, а не параграф;
- перед каждой папкой главы кладётся шмуцтитул с названием из `modules:`;
- заголовки внутри параграфов опускаются на уровень, чтобы «# § 1.1»
  стал разделом главы, а не главой;
- `chapters/index.md` в книгу не идёт: это страница сайта, и при сортировке
  по путям она к тому же оказывается в самом конце.

Оригиналы не трогаются — всё пишется в `.build-structure/`. На выход идёт
список путей по порядку чтения, по одному в строке.

Книга без блока `modules:` обрабатывается по-старому: без шмуцтитулов и
без сдвига заголовков.
"""
import argparse
import os
import pathlib
import re
import shutil
import sys

import yaml

STAGE = pathlib.Path(".build-structure")
FENCE = re.compile(r"^\s*(```|~~~)")
HEAD = re.compile(r"^#{1,5}\s")
FRONT = re.compile(r"\A---\n.*?\n---\n", re.S)


def status_of(text):
    m = re.search(r"^---.*?status:\s*(\w+).*?---", text, re.S)
    return m.group(1) if m else "ready"


def keep(status, flt):
    if flt == "all":
        return True
    if flt == "review":
        return status in ("ready", "review")
    return status == "ready"


def shift(text):
    """Опустить заголовки на уровень, не трогая содержимое блоков кода."""
    out, fence = [], False
    for line in text.split("\n"):
        if FENCE.match(line):
            fence = not fence
        if not fence and HEAD.match(line):
            line = "#" + line
        out.append(line)
    return "\n".join(out)


def title_of(text):
    m = re.search(r"^#\s+(.+)$", text, re.M)
    return m.group(1).strip() if m else ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--filter", default="review", choices=["ready", "review", "all"])
    args = ap.parse_args()

    meta = yaml.safe_load(pathlib.Path("metadata.yaml").read_text(encoding="utf-8"))
    modules = meta.get("modules") or {}

    chapters = pathlib.Path("chapters")
    dirs = sorted(d for d in chapters.iterdir() if d.is_dir()) if chapters.is_dir() else []

    # Книга без объявленных глав собирается как раньше: плоским списком.
    if not modules or not dirs:
        for f in sorted(chapters.rglob("*.md")):
            if f.name.startswith("_"):
                continue
            if keep(status_of(f.read_text(encoding="utf-8")), args.filter):
                print(f)
        return

    shutil.rmtree(STAGE, ignore_errors=True)
    STAGE.mkdir()
    order = []
    n = 0

    for f in sorted(pathlib.Path("front").glob("*.md")) if pathlib.Path("front").is_dir() else []:
        text = f.read_text(encoding="utf-8")
        if not keep(status_of(text), args.filter):
            continue
        body = FRONT.sub("", text)
        head = title_of(body)
        body = re.sub(r"^#\s+.+$", "", body, count=1, flags=re.M)
        n += 1
        p = STAGE / f"{n:03d}_0_front_{f.name}"
        # Ненумерованная глава: вводная часть — не параграф и не глава N.
        p.write_text(f"# {head} {{.unnumbered}}\n{shift(body)}", encoding="utf-8")
        order.append(p)

    for d in dirs:
        files = [f for f in sorted(d.glob("*.md")) if not f.name.startswith("_")]
        files = [f for f in files if keep(status_of(f.read_text(encoding="utf-8")), args.filter)]
        if not files:
            continue
        n += 1
        title = re.sub(r"^(Модуль|Глава|Часть|Раздел)\s+\d+\.\s*", "",
                       str(modules.get(d.name, d.name))).strip()
        p = STAGE / f"{n:03d}_0_chapter.md"
        p.write_text(f"# {title}\n\n", encoding="utf-8")
        order.append(p)
        for i, f in enumerate(files, 1):
            q = STAGE / f"{n:03d}_{i:02d}_{f.name}"
            q.write_text(shift(FRONT.sub("", f.read_text(encoding="utf-8"))), encoding="utf-8")
            order.append(q)

    if not order:
        sys.exit(0)
    for p in order:
        print(p)


if __name__ == "__main__":
    main()
