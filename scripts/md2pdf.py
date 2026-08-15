#!/usr/bin/env python3
"""Render a Markdown strategy document to a print-ready PDF.

Usage:  python3 scripts/md2pdf.py <input.md> [output.pdf]

Uses Liberation Sans / DejaVu Sans Mono so Cyrillic renders correctly.
"""

import re
import sys
from pathlib import Path

import markdown
from weasyprint import HTML

CSS = """
@page {
    size: A4;
    margin: 18mm 16mm 20mm 16mm;
    @bottom-center {
        content: counter(page);
        font-family: "Liberation Sans";
        font-size: 8pt;
        color: #8a8a8a;
    }
}
@page :first { margin-top: 26mm; }

html { font-size: 10pt; }
body {
    font-family: "Liberation Sans", "DejaVu Sans", sans-serif;
    font-size: 9.6pt;
    line-height: 1.5;
    color: #1a1a1a;
    hyphens: none;
}

h1, h2, h3, h4 {
    font-family: "Liberation Sans", "DejaVu Sans", sans-serif;
    line-height: 1.25;
    break-after: avoid;
    break-inside: avoid;
}
h1 {
    font-size: 20pt;
    margin: 0 0 4mm 0;
    padding-bottom: 3mm;
    border-bottom: 2.5pt solid #1a1a1a;
    letter-spacing: -0.3pt;
}
h2 {
    font-size: 13.5pt;
    margin: 9mm 0 3mm 0;
    padding-top: 2.5mm;
    border-top: 0.6pt solid #cfcfcf;
    color: #000;
}
h3 { font-size: 10.8pt; margin: 6mm 0 2mm 0; color: #222; }
h4 { font-size: 9.8pt; margin: 4mm 0 1.5mm 0; color: #444; }

p { margin: 0 0 2.6mm 0; orphans: 2; widows: 2; }

ul, ol { margin: 0 0 3mm 0; padding-left: 5.5mm; }
li { margin-bottom: 1.2mm; }

strong { font-weight: 700; }
em { font-style: italic; }

a { color: #16457a; text-decoration: none; border-bottom: 0.4pt solid #b8cbe0; }

code {
    font-family: "DejaVu Sans Mono", monospace;
    font-size: 8.2pt;
    background: #f2f2f0;
    padding: 0.3mm 0.9mm;
    border-radius: 1pt;
}

pre {
    font-family: "DejaVu Sans Mono", monospace;
    font-size: 7.9pt;
    line-height: 1.32;
    background: #f7f7f5;
    border: 0.5pt solid #dcdcd8;
    border-left: 2pt solid #999;
    padding: 2.5mm 3mm;
    margin: 0 0 3.5mm 0;
    white-space: pre;
    break-inside: avoid;
}
pre code { background: none; padding: 0; font-size: inherit; }

blockquote {
    margin: 0 0 3.5mm 0;
    padding: 2.5mm 3.5mm;
    background: #f4f6f8;
    border-left: 2.5pt solid #16457a;
    break-inside: avoid;
}
blockquote p { margin-bottom: 1.5mm; }
blockquote p:last-child { margin-bottom: 0; }

table {
    width: 100%;
    border-collapse: collapse;
    margin: 0 0 4mm 0;
    font-size: 8.5pt;
    line-height: 1.35;
}
thead { display: table-header-group; }
th {
    background: #ececea;
    text-align: left;
    font-weight: 700;
    padding: 1.5mm 2mm;
    border: 0.5pt solid #c8c8c4;
}
td {
    padding: 1.5mm 2mm;
    border: 0.5pt solid #d8d8d4;
    vertical-align: top;
}
tr { break-inside: avoid; }
tbody tr:nth-child(even) { background: #fafaf9; }

hr {
    border: none;
    border-top: 0.6pt solid #d0d0cc;
    margin: 6mm 0;
}

/* Document header block */
.doc-meta {
    font-size: 9pt;
    color: #555;
    margin: 0 0 7mm 0;
}
"""


def build(src: Path, out: Path) -> None:
    text = src.read_text(encoding="utf-8")

    html_body = markdown.markdown(
        text,
        extensions=["tables", "fenced_code", "sane_lists", "attr_list"],
    )

    title = "Strategy"
    m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    if m:
        title = m.group(1).strip()

    doc = (
        "<!doctype html><html lang='ru'><head><meta charset='utf-8'>"
        f"<title>{title}</title><style>{CSS}</style></head>"
        f"<body>{html_body}</body></html>"
    )
    HTML(string=doc, base_url=str(src.parent)).write_pdf(str(out))
    print(f"{out}  ({out.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: md2pdf.py <input.md> [output.pdf]")
    source = Path(sys.argv[1])
    target = Path(sys.argv[2]) if len(sys.argv) > 2 else source.with_suffix(".pdf")
    build(source, target)
