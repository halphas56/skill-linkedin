#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
md2pdf - turn the skill's markdown deliverables into a structured, client-ready A4 PDF.

Pipeline:  markdown -> HTML (+print CSS) -> headless Chrome -> page numbers stamped on

Why Chrome and not ReportLab: these deliverables are table-heavy and the tables are the
argument, not decoration. CSS gives real control over column behaviour, repeated headers
across page breaks, and callouts. ReportLab's built-in fonts also have no Cyrillic, and
every deliverable here may be Russian.

Usage
-----
    python tools/md2pdf.py INPUT.md [MORE.md ...] -o OUT.pdf
           --title "..." [--subtitle "..."] [--date "..."]
           [--stats "Балл=18/33;Ворота=2 провала"]
           [--lang ru|en] [--no-toc] [--keep-html]

Each additional INPUT starts on a new page, so a set of related documents can be bound
into one report in the order given.
"""

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    import markdown
except ImportError:
    sys.exit(
        "Missing dependency 'markdown'.\n"
        "  pip install -r tools/requirements.txt   (or: pip install markdown)\n"
        "Optional, for page numbers: pypdf, reportlab."
    )

def _optional_import(loader, what):
    """Run `loader`, returning None if the dependency is missing OR broken.

    `except ImportError` is not enough. A native dependency can be installed
    but unusable - pypdf pulls in `cryptography`, and a mismatched build makes
    pyo3 raise PanicException, which derives from BaseException directly and
    slips straight through `except Exception`. pyo3_runtime is not importable
    until such an extension has loaded, so the class cannot be named up front.

    Hence BaseException, with the two that must never be swallowed re-raised.
    """
    try:
        return loader()
    except (KeyboardInterrupt, SystemExit):
        raise
    except BaseException as exc:
        print("  (%s unavailable - %s: %s)" % (what, type(exc).__name__, exc))
        return None


# ---------------------------------------------------------------- Chrome

CHROME_CANDIDATES = [
    # Windows
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    # Linux
    "/usr/bin/google-chrome",
    "/usr/bin/google-chrome-stable",
    "/opt/google/chrome/chrome",
    "/usr/bin/chromium",
    "/usr/bin/chromium-browser",
    "/snap/bin/chromium",
    "/usr/bin/microsoft-edge",
    # macOS
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
]

# Containers and CI images often ship a browser that is on no standard path and
# not on PATH either - Playwright images are the common case. Look there too.
BROWSER_ROOTS_ENV = ("PLAYWRIGHT_BROWSERS_PATH", "PUPPETEER_CACHE_DIR")
BROWSER_GLOBS = (
    "chromium*/chrome-linux/chrome",
    "chromium*/chrome-linux/headless_shell",
    "chromium*",
    "chrome/*/chrome-linux64/chrome",
)


def find_chrome():
    """Locate a Chromium-family binary, or return None.

    Order: explicit override, known install paths, PATH, browser caches.
    Returns None rather than exiting so the caller can still deliver the HTML.
    """
    # An explicit override always wins - the escape hatch for odd setups.
    for var in ("CHROME_PATH", "CHROME_BIN", "MD2PDF_CHROME"):
        p = os.environ.get(var)
        if p and os.path.exists(p):
            return p

    for p in CHROME_CANDIDATES:
        if os.path.exists(p):
            return p

    for name in ("chrome", "google-chrome", "google-chrome-stable",
                 "chromium", "chromium-browser", "msedge", "microsoft-edge"):
        found = shutil.which(name)
        if found:
            return found

    roots = [os.environ[v] for v in BROWSER_ROOTS_ENV if os.environ.get(v)]
    roots += [os.path.expanduser("~/.cache/ms-playwright"),
              os.path.expanduser("~/.cache/puppeteer")]
    for root in roots:
        if not os.path.isdir(root):
            continue
        for pattern in BROWSER_GLOBS:
            for hit in sorted(Path(root).glob(pattern), reverse=True):
                if hit.is_file() and os.access(hit, os.X_OK):
                    return str(hit)
    return None


# ---------------------------------------------------------------- CSS
#
# Font stacks are chosen for guaranteed Cyrillic coverage on Windows and sane
# fallbacks elsewhere. Georgia/Cambria for body: a serif reads better than sans
# at report length and both carry a full Cyrillic set.

CSS = """
@page { size: A4; margin: 19mm 16mm 20mm 16mm; }

:root{
  --ink:#1a1d24; --muted:#5c6472; --rule:#d9dde4; --rule-soft:#eef0f4;
  --accent:#1f4e79; --accent-soft:#eef4fa;
  --ok:#1a7f47; --ok-bg:#e8f5ed;
  --bad:#b3261e; --bad-bg:#fdeceb;
  --warn:#8a5a00; --warn-bg:#fdf3e0;
}

*{ box-sizing:border-box; }

body{
  font-family:Georgia,Cambria,"Times New Roman",serif;
  font-size:9.9pt; line-height:1.52; color:var(--ink);
  margin:0; -webkit-print-color-adjust:exact; print-color-adjust:exact;
}

/* ---------------- cover ---------------- */
.cover{ break-after:page; padding-top:52mm; }
.cover .kicker{
  font-family:"Segoe UI",Arial,sans-serif; font-size:8.6pt; font-weight:600;
  letter-spacing:.16em; text-transform:uppercase; color:var(--accent); margin-bottom:9mm;
}
.cover h1{
  font-family:"Segoe UI",Arial,sans-serif; font-size:27pt; line-height:1.16;
  font-weight:700; color:var(--ink); margin:0 0 5mm; border:0; padding:0;
}
.cover .sub{ font-size:12.5pt; color:var(--muted); line-height:1.45; margin:0 0 11mm; max-width:150mm; }
.cover .rule{ height:3px; width:34mm; background:var(--accent); margin-bottom:9mm; }
.cover .date{ font-family:"Segoe UI",Arial,sans-serif; font-size:9.5pt; color:var(--muted); }

.stats{ display:flex; flex-wrap:wrap; gap:4mm; margin-top:13mm; }
.stat{
  border:1px solid var(--rule); border-left:3px solid var(--accent);
  padding:3.2mm 5mm; min-width:38mm; background:#fbfcfd;
}
.stat .k{
  font-family:"Segoe UI",Arial,sans-serif; font-size:7.6pt; font-weight:600;
  letter-spacing:.09em; text-transform:uppercase; color:var(--muted); margin-bottom:1.4mm;
}
.stat .v{ font-family:"Segoe UI",Arial,sans-serif; font-size:15pt; font-weight:700; color:var(--ink); }

/* ---------------- contents ---------------- */
.toc{ break-after:page; }
.toc > h2{ margin-top:0; }
.toc ul{ list-style:none; padding-left:0; margin:0; }
.toc ul ul{ padding-left:7mm; }
.toc li{ margin:.9mm 0; }
.toc a{ color:var(--ink); text-decoration:none; }
.toc > ul > li > a{ font-family:"Segoe UI",Arial,sans-serif; font-weight:600; }
.toc ul ul a{ color:var(--muted); font-size:9.2pt; }

/* ---------------- headings ---------------- */
h1,h2,h3,h4{ font-family:"Segoe UI",Arial,sans-serif; break-after:avoid; color:var(--ink); }
h1{ font-size:17pt; font-weight:700; margin:0 0 6mm; padding-bottom:2.6mm; border-bottom:2px solid var(--accent); }
h2{ font-size:12.6pt; font-weight:700; margin:8mm 0 3mm; padding-bottom:1.6mm; border-bottom:1px solid var(--rule); }
h3{ font-size:10.6pt; font-weight:700; margin:6mm 0 2mm; color:var(--accent); }
h4{ font-size:9.8pt; font-weight:600; margin:4.5mm 0 1.5mm; color:var(--muted); }
.pagebreak{ break-before:page; }

p{ margin:0 0 3mm; orphans:3; widows:3; }
ul,ol{ margin:0 0 3mm; padding-left:6mm; }
li{ margin:.9mm 0; }
strong{ font-weight:700; }
a{ color:var(--accent); text-decoration:none; }
hr{ border:0; border-top:1px solid var(--rule-soft); margin:6mm 0; }

/* ---------------- tables ---------------- */
table{
  width:100%; border-collapse:collapse; margin:3mm 0 5mm;
  font-family:"Segoe UI",Arial,sans-serif; font-size:8.6pt; line-height:1.4;
}
thead{ display:table-header-group; }
tr{ break-inside:avoid; }
th{
  background:var(--accent); color:#fff; font-weight:600; text-align:left;
  padding:2.2mm 2.6mm; border:1px solid var(--accent);
  font-size:8.2pt; letter-spacing:.02em;
}
td{ padding:2mm 2.6mm; border:1px solid var(--rule); vertical-align:top; }
tbody tr:nth-child(even) td{ background:#f7f9fb; }

/* status badges, injected into table cells */
.badge{
  display:inline-block; font-weight:700; font-size:7.6pt; letter-spacing:.05em;
  padding:.7mm 1.8mm; border-radius:2px; white-space:nowrap;
}
.b-ok{ background:var(--ok-bg); color:var(--ok); border:1px solid #bfe0cd; }
.b-bad{ background:var(--bad-bg); color:var(--bad); border:1px solid #f2c4c1; }
.b-warn{ background:var(--warn-bg); color:var(--warn); border:1px solid #ecd9a8; }

/* ---------------- callouts ---------------- */
blockquote{
  margin:4mm 0; padding:3.2mm 5mm; background:var(--accent-soft);
  border-left:3px solid var(--accent); break-inside:avoid;
}
blockquote p{ margin:0 0 2mm; }
blockquote p:last-child{ margin-bottom:0; }

/* ---------------- code ---------------- */
code{
  font-family:Consolas,"Courier New",monospace; font-size:8.6pt;
  background:#f2f4f7; padding:.4mm 1.1mm; border-radius:2px; color:#0f2b46;
}
pre{
  background:#f7f9fb; border:1px solid var(--rule); border-left:3px solid var(--muted);
  padding:3mm 4mm; margin:3mm 0; overflow-wrap:anywhere; white-space:pre-wrap;
  break-inside:avoid;
}
pre code{ background:none; padding:0; font-size:8.4pt; }

/* footer band drawn by the stamping pass sits below this */
"""


# ---------------------------------------------------------------- helpers

BADGE_MAP = [
    (r"\bPASS\b", "b-ok"),
    (r"\bFAIL\b", "b-bad"),
    (r"\bPARTIAL\b", "b-warn"),
    (r"\bОК\b", "b-ok"),
]


def badge_cells(html):
    """Wrap PASS / FAIL / PARTIAL in coloured badges, but only inside table cells.

    Scoped to cells on purpose: the same words appear in running prose, where a
    badge would be noise rather than signal.
    """

    def one_cell(m):
        cell = m.group(0)
        for pattern, cls in BADGE_MAP:
            cell = re.sub(pattern, lambda w: '<span class="badge %s">%s</span>' % (cls, w.group(0)), cell)
        return cell

    return re.sub(r"<t[dh][^>]*>.*?</t[dh]>", one_cell, html, flags=re.S)


def render_markdown(paths):
    """Convert all inputs in a single pass so the table of contents is unified.

    Converting file-by-file would leave `md.toc` holding only the last document.
    Documents are separated by a raw page-break div, which markdown passes through
    untouched.
    """
    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "sane_lists", "attr_list", "toc"],
        extension_configs={"toc": {"toc_depth": "1-3"}},
    )
    sep = '\n\n<div class="pagebreak"></div>\n\n'
    combined = sep.join(Path(p).read_text(encoding="utf-8") for p in paths)
    return md.convert(combined), md.toc


def build_html(body, toc, args):
    stats_html = ""
    if args.stats:
        cells = []
        for pair in args.stats.split(";"):
            if "=" not in pair:
                continue
            k, v = pair.split("=", 1)
            cells.append('<div class="stat"><div class="k">%s</div><div class="v">%s</div></div>'
                         % (k.strip(), v.strip()))
        if cells:
            stats_html = '<div class="stats">%s</div>' % "".join(cells)

    toc_label = "Содержание" if args.lang == "ru" else "Contents"
    toc_html = ""
    if toc and not args.no_toc:
        toc_html = '<section class="toc"><h2>%s</h2>%s</section>' % (toc_label, toc)

    sub = '<p class="sub">%s</p>' % args.subtitle if args.subtitle else ""
    kicker = args.kicker or ("Отчёт" if args.lang == "ru" else "Report")

    return """<!doctype html>
<html lang="%s"><head><meta charset="utf-8"><title>%s</title>
<style>%s</style></head><body>
<section class="cover">
  <div class="kicker">%s</div>
  <div class="rule"></div>
  <h1>%s</h1>
  %s
  <div class="date">%s</div>
  %s
</section>
%s
<main>%s</main>
</body></html>""" % (
        args.lang, args.title, CSS, kicker, args.title, sub, args.date or "", stats_html,
        toc_html, body,
    )


def chrome_to_pdf(html_path, out_pdf, chrome):
    """Render through a temp dir with no spaces - Chrome's CLI path handling is fussy."""
    with tempfile.TemporaryDirectory() as td:
        tmp_pdf = os.path.join(td, "out.pdf")
        profile = os.path.join(td, "prof")
        cmd = [
            chrome, "--headless=new", "--disable-gpu", "--no-sandbox",
            "--no-pdf-header-footer", "--run-all-compositor-stages-before-draw",
            "--virtual-time-budget=12000", "--user-data-dir=" + profile,
            "--print-to-pdf=" + tmp_pdf, Path(html_path).as_uri(),
        ]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
        if not os.path.exists(tmp_pdf):
            sys.exit("Chrome produced no PDF.\n%s\n%s" % (r.stdout[-2000:], r.stderr[-2000:]))
        shutil.move(tmp_pdf, out_pdf)


STAMP_FONTS = [
    r"C:\Windows\Fonts\arial.ttf",
    r"C:\Windows\Fonts\segoeui.ttf",
    r"C:\Windows\Fonts\calibri.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
]


def _register_stamp_font():
    """Return a font name for the footer that can actually draw Cyrillic."""
    def _load():
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
        return pdfmetrics, TTFont

    mods = _optional_import(_load, "reportlab fonts")
    if mods is None:
        return "Helvetica"
    pdfmetrics, TTFont = mods
    for path in STAMP_FONTS:
        if os.path.exists(path):
            try:
                pdfmetrics.registerFont(TTFont("StampFont", path))
                return "StampFont"
            except Exception:
                continue
    return "Helvetica"


def stamp_page_numbers(pdf_path, label=""):
    """Chrome cannot draw custom page numbers, so overlay them afterwards.

    Page 1 is the cover and is left clean.
    """
    def _load():
        from pypdf import PdfReader, PdfWriter
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.colors import HexColor
        return PdfReader, PdfWriter, canvas, A4, HexColor

    # Page numbers are optional; the PDF is not.
    mods = _optional_import(_load, "page numbers")
    if mods is None:
        return
    PdfReader, PdfWriter, canvas, A4, HexColor = mods

    # ReportLab's built-in Helvetica has NO Cyrillic glyphs - a Russian footer
    # renders as solid black boxes. Register a real TrueType face, and fall back
    # to stripping non-ASCII rather than printing boxes.
    font = _register_stamp_font()
    if font == "Helvetica":
        label = label.encode("ascii", "ignore").decode("ascii").strip(" ·-")

    reader = PdfReader(pdf_path)
    total = len(reader.pages)
    if total < 2:
        return

    overlay_path = pdf_path + ".num.pdf"
    c = canvas.Canvas(overlay_path, pagesize=A4)
    w, h = A4
    for i in range(1, total + 1):
        if i > 1:
            c.setStrokeColor(HexColor("#d9dde4"))
            c.setLineWidth(0.5)
            c.line(45, 34, w - 45, 34)
            c.setFont(font, 7.5)
            c.setFillColor(HexColor("#5c6472"))
            c.drawRightString(w - 45, 24, "%d / %d" % (i, total))
            if label:
                c.drawString(45, 24, label)
        c.showPage()
    c.save()

    numbers = PdfReader(overlay_path)
    writer = PdfWriter()
    for i, page in enumerate(reader.pages):
        page.merge_page(numbers.pages[i])
        writer.add_page(page)
    with open(pdf_path, "wb") as fh:
        writer.write(fh)
    os.remove(overlay_path)


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description="Markdown -> structured A4 PDF")
    ap.add_argument("inputs", nargs="+", help="markdown file(s), in binding order")
    ap.add_argument("-o", "--out", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--subtitle", default="")
    ap.add_argument("--kicker", default="")
    ap.add_argument("--date", default="")
    ap.add_argument("--stats", default="", help='cover stat strip: "Балл=18/33;Ворота=2 провала"')
    ap.add_argument("--lang", default="ru", choices=["ru", "en"])
    ap.add_argument("--footer", default="", help="text in the bottom-left of every page")
    ap.add_argument("--no-toc", action="store_true")
    ap.add_argument("--keep-html", action="store_true")
    args = ap.parse_args()

    for p in args.inputs:
        if not os.path.exists(p):
            sys.exit("No such file: %s" % p)

    body, toc = render_markdown(args.inputs)
    body = badge_cells(body)
    html = build_html(body, toc, args)

    out = os.path.abspath(args.out)
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)

    # Absolute: Path.as_uri() below refuses a relative path.
    html_path = os.path.splitext(out)[0] + ".html"
    Path(html_path).write_text(html, encoding="utf-8")

    # No browser is not a reason to lose the work. The HTML is already the
    # fully styled deliverable - keep it, say so, and exit non-zero so a
    # caller can tell a PDF was not produced.
    chrome = find_chrome()
    if chrome is None:
        sys.exit(
            "No Chrome/Chromium/Edge found, so no PDF was produced.\n"
            "The styled HTML was kept and opens in any browser:\n"
            "  %s\n"
            "Print it to PDF from there, or point the script at a browser:\n"
            "  CHROME_PATH=/path/to/chrome python tools/md2pdf.py ...\n"
            "Searched: standard install paths, PATH, $PLAYWRIGHT_BROWSERS_PATH, "
            "~/.cache/ms-playwright." % html_path
        )

    chrome_to_pdf(html_path, out, chrome)
    stamp_page_numbers(out, args.footer)

    if not args.keep_html:
        os.remove(html_path)

    print("%s  (%.1f KB)" % (out, os.path.getsize(out) / 1024.0))


if __name__ == "__main__":
    main()
