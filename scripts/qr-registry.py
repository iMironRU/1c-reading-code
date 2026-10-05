#!/usr/bin/env python3
"""Реестр коротких кодов для qr.imiron.ru.

Код печатается на бумаге и живёт вечно: присваивается объекту один раз и
никогда не переиспользуется. Цель, на которую он ведёт, меняться может
сколько угодно — адрес остаётся.

    ./book.sh qr            присвоить коды новым объектам, обновить цели
    ./book.sh qr --check    ничего не писать; выйти с ошибкой, если разошлось

Формат кода — шесть знаков: буква книги, четыре знака тела и контрольный.

    K7M2QX
    │└──┬─┘│
    │   │  └ контрольный знак, алгоритм Дамма
    │   └─── тело, 31^4 ≈ 923 тысячи значений на книгу
    └─────── буква книги

Алфавит — 31 знак: без I, L, O, U (путают с 1, 1, 0, V) и без Z (путают с 2).
Тридцать один — простое число, и это не ради красоты: на простом порядке
квазигруппа Дамма строится точной формулой, без таблицы и без перебора.

    x * y = 7·(x − y) mod 31

Операция образует квазигруппу с нулевой диагональю и вполне антисимметрична
при любом множителе, кроме 0 и 1. Проверено перебором всех 29 791 тройки.
Отсюда гарантия Дамма: ловятся ВСЕ одиночные замены знаков и ВСЕ перестановки
соседних — без исключений. Проверено на 36 миллионах замен и миллионе
перестановок, пропущено ноль.

Что получает код: исполнимые листинги (кучка «песочница»), иллюстрации и
схемы — чтобы с бумаги открыть цветную версию или видео, — и главы.
"""
import argparse
import base64
import hashlib
import os
import random
import re
import sys
import urllib.parse

import yaml

ALPHABET = "0123456789ABCDEFGHJKMNPQRSTVWXY"      # 31 знак: без I, L, O, U, Z
P, MUL = 31, 7                                      # x*y = MUL·(x−y) mod P
REGISTRY = "assets/qr/registry.yaml"
IMGDIR = "assets/qr/img"
TRAINER = "https://imironru.github.io/BSLexicon/"
DOMAIN = "qr.imiron.ru"
FENCE = re.compile(r"^```([^\n]*)\n(.*?)^```[ \t]*$", re.S | re.M)


def _fold(text: str) -> int:
    i = 0
    for ch in text:
        i = (MUL * (i - ALPHABET.index(ch))) % P
    return i


def check_char(body: str) -> str:
    """Контрольный знак по Дамму: им становится итоговое промежуточное число."""
    return ALPHABET[_fold(body)]


def valid(code: str) -> bool:
    """Код верен, когда свёртка всей шестёрки, вместе с контрольным, даёт нуль."""
    code = normalize(code)
    return len(code) == 6 and all(c in ALPHABET for c in code) and _fold(code) == 0


def normalize(code: str) -> str:
    """Прощаем читателю то, что путается на бумаге: регистр, пробелы, дефисы
    и четыре буквы, которых в алфавите нет."""
    code = code.strip().upper().replace(" ", "").replace("-", "")
    return code.translate(str.maketrans("ILOUZ", "110V2"))


def mint(letter: str, taken: set, rnd: random.Random) -> str:
    for _ in range(10000):
        body = letter + "".join(rnd.choice(ALPHABET) for _ in range(4))
        code = body + check_char(body)
        if code not in taken:
            return code
    raise SystemExit("не удалось выдать код — тело алфавита исчерпано")


def b64url(text: str) -> str:
    return base64.urlsafe_b64encode(text.encode()).decode().rstrip("=")


def paragraph_title(text: str) -> str:
    m = re.search(r"^#\s+(.+)$", text, re.M)
    return m.group(1).strip() if m else ""


def page_url(site: str, path: str) -> str:
    return site.rstrip("/") + "/" + path.replace(".md", ".html")


def scan(meta):
    """Что в книге заслуживает кода, в порядке чтения."""
    site = meta.get("site_url", "")
    found = []
    # Глава — своя точка входа: метка на шмуцтитуле ведёт на посадочную
    # страницу главы, откуда читатель с бумаги продолжает в любом формате.
    mods = meta.get("modules") or {}
    for slug in sorted(mods):
        first = sorted(p for p in os.listdir(os.path.join("chapters", slug))
                       if p.endswith(".md"))
        if not first:
            continue
        found.append({
            "kind": "глава",
            "file": os.path.join("chapters", slug),
            "ord": 1,
            "fp": hashlib.sha256(slug.encode()).hexdigest()[:12],
            "title": mods[slug],
            "target": page_url(site, os.path.join("chapters", slug, first[0])),
        })
    for root, _, files in sorted(os.walk("chapters")):
        for name in sorted(files):
            if not name.endswith(".md"):
                continue
            path = os.path.join(root, name)
            text = open(path, encoding="utf-8").read()
            title = paragraph_title(text)
            kinds = {}
            for m in FENCE.finditer(text):
                info = m.group(1)
                if "песочница" not in info:
                    continue
                kind = "песочница"
                kinds[kind] = kinds.get(kind, 0) + 1
                body = m.group(2)
                found.append({
                    "kind": kind,
                    "file": path,
                    "ord": kinds[kind],
                    "fp": hashlib.sha256(body.strip().encode()).hexdigest()[:12],
                    "title": title,
                    "target": (TRAINER + "?code=" + b64url(body.strip())
                               + "&source=" + urllib.parse.quote(page_url(site, path), safe="")
                               + "&title=" + urllib.parse.quote(title, safe="")),
                })
            for m in re.finditer(r"!\[[^\]]*\]\(([^)]+)\)", text):
                kinds["иллюстрация"] = kinds.get("иллюстрация", 0) + 1
                found.append({
                    "kind": "иллюстрация",
                    "file": path,
                    "ord": kinds["иллюстрация"],
                    "fp": hashlib.sha256(m.group(1).encode()).hexdigest()[:12],
                    "title": title,
                    "target": page_url(site, path) + "#" + os.path.basename(m.group(1)),
                })
    return found


def draw(codes):
    """Картинки меток кладём рядом с реестром и держим в репозитории:
    тогда печатная сборка не зависит от библиотеки, которой может не быть
    на машине сборки."""
    try:
        import segno
    except ImportError:
        print("  segno не установлен — картинки меток не перерисованы "
              "(pip install segno)")
        return
    os.makedirs(IMGDIR, exist_ok=True)
    made = 0
    for code in codes:
        path = os.path.join(IMGDIR, code + ".png")
        if os.path.exists(path):
            continue
        segno.make(DOMAIN + "/" + code, error="q").save(path, scale=16, border=2)
        made += 1
    if made:
        print(f"  нарисовано картинок меток: {made} → {IMGDIR}/")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    meta = yaml.safe_load(open("metadata.yaml", encoding="utf-8"))
    reg = {}
    if os.path.exists(REGISTRY):
        reg = yaml.safe_load(open(REGISTRY, encoding="utf-8")) or {}
    letter = (reg.get("letter") or meta.get("qr_letter") or "").upper()
    if letter not in ALPHABET:
        sys.exit(f"{REGISTRY}: нет поля letter — буква книги из алфавита {ALPHABET}")

    codes = reg.get("codes") or {}
    taken = set(codes)
    rnd = random.SystemRandom()

    # Сопоставляем сначала по отпечатку (листинг могли передвинуть),
    # потом по месту (листинг могли поправить).
    by_fp = {(v["file"], v["kind"], v["fp"]): k for k, v in codes.items()}
    by_pos = {(v["file"], v["kind"], v["ord"]): k for k, v in codes.items()}

    out, used, new = {}, set(), []
    for item in scan(meta):
        key = by_fp.get((item["file"], item["kind"], item["fp"]))
        if key in used:
            key = None
        if key is None:
            key = by_pos.get((item["file"], item["kind"], item["ord"]))
            if key in used:
                key = None
        if key is None:
            key = mint(letter, taken, rnd)
            taken.add(key)
            new.append(key)
        used.add(key)
        out[key] = {"kind": item["kind"], "file": item["file"], "ord": item["ord"],
                    "fp": item["fp"], "title": item["title"], "target": item["target"]}

    # Коды, объект которых исчез, остаются в реестре: бумага с ними уже ушла.
    retired = []
    for k, v in codes.items():
        if k not in out:
            v = dict(v)
            v["retired"] = True
            out[k] = v
            retired.append(k)

    doc = {"book": meta.get("book_id") or os.path.basename(os.getcwd()),
           "letter": letter,
           "codes": {k: out[k] for k in sorted(out)}}
    text = yaml.safe_dump(doc, allow_unicode=True, sort_keys=False, width=100)

    old = open(REGISTRY, encoding="utf-8").read() if os.path.exists(REGISTRY) else ""
    if args.check:
        if text != old:
            sys.exit("реестр разошёлся с книгой — запустите ./book.sh qr")
        print(f"реестр в порядке: {len(out)} кодов")
        return
    os.makedirs(os.path.dirname(REGISTRY), exist_ok=True)
    open(REGISTRY, "w", encoding="utf-8").write(text)
    draw(sorted(k for k, v in out.items() if not v.get("retired")))
    print(f"кодов всего: {len(out)}, выдано новых: {len(new)}, выведено из обращения: {len(retired)}")
    kinds = {}
    for v in out.values():
        kinds[v["kind"]] = kinds.get(v["kind"], 0) + 1
    for k, n in sorted(kinds.items()):
        print(f"  {k}: {n}")


if __name__ == "__main__":
    main()
