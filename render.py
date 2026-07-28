#!/usr/bin/env python3
"""
Render resume.md -> dist/Young_CV.pdf with the styling defined in render.css.

Usage:
    python render.py [resume.md] [dist/Young_CV.pdf] [render.css]

With no arguments, resume.md and render.css beside this script are used and the
PDF is written to dist/Young_CV.pdf.

Dependencies:
    pip install -r requirements.txt
    weasyprint also needs native pango/gdk-pixbuf (macOS: brew install pango gdk-pixbuf libffi)

Markdown conventions understood by this renderer:
    * A paragraph tagged `{: .contact-label}` / `{: .contact}` becomes the
      top-right contact block (needs the `attr_list` extension).
    * A line `### Title @ Company | Dates` becomes a three-column entry header
      (title left, company middle, dates right-aligned).
    * The first table (the Technical Summary) is given class `tech`; its header
      row is hidden by CSS, so use an empty header row in the markdown.
"""
import re
import sys
from pathlib import Path

import markdown
from weasyprint import HTML


ENTRY_RE = re.compile(r'^###\s+(?P<title>.+?)\s+@\s+(?P<org>.+?)\s+\|\s+(?P<dates>.+?)\s*$')


def preprocess(md_text: str) -> str:
    """Turn `### Title @ Company | Dates` lines into raw-HTML entry rows.

    Emitted as block-level HTML (blank lines around it) so python-markdown
    passes it through untouched.
    """
    out = []
    for line in md_text.splitlines():
        m = ENTRY_RE.match(line)
        if m:
            out.append("")
            out.append(
                '<div class="entry">'
                f'<span class="e-title">{m["title"]}</span>'
                f'<span class="e-org">{m["org"]}</span>'
                f'<span class="e-dates">{m["dates"]}</span>'
                '</div>'
            )
            out.append("")
        else:
            out.append(line)
    return "\n".join(out)


def tag_tech_table(html: str) -> str:
    """Add class="tech" to the first <table> (the Technical Summary)."""
    return html.replace("<table>", '<table class="tech">', 1)


def build_html(md_path: Path, css_path: Path) -> str:
    md_text = md_path.read_text(encoding="utf-8")
    body = markdown.markdown(
        preprocess(md_text),
        # nl2br keeps the multi-line contact block from collapsing onto one line.
        extensions=["tables", "attr_list", "sane_lists", "nl2br"],
        output_format="html5",
    )
    body = tag_tech_table(body)
    css = css_path.read_text(encoding="utf-8")
    return (
        "<!DOCTYPE html><html><head><meta charset='utf-8'>"
        f"<style>{css}</style></head><body>{body}</body></html>"
    )


HERE = Path(__file__).resolve().parent
DEFAULT_MD = HERE / "resume.md"
DEFAULT_CSS = HERE / "render.css"
DEFAULT_PDF = HERE / "dist" / "Young_CV.pdf"


def main() -> None:
    md_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_MD
    css_path = Path(sys.argv[3]) if len(sys.argv) > 3 else DEFAULT_CSS
    pdf_path = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_PDF

    for p, kind in ((md_path, "markdown"), (css_path, "css")):
        if not p.is_file():
            sys.exit(f"{kind} file not found: {p}")

    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    html = build_html(md_path, css_path)
    HTML(string=html, base_url=str(md_path.resolve().parent)).write_pdf(str(pdf_path))
    print(f"Wrote {pdf_path}")


if __name__ == "__main__":
    main()
