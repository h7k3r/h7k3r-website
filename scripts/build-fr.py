"""Build fr/index.html (French h7k3r.com) and add the EN/FR switcher + hreflang
to the English index.html.

    python3 scripts/build-fr.py

Every English string in fr_map.py must be found the expected number of times,
or the build stops and names the one that is wrong — so after editing
index.html, run this again and fix whatever it reports.
"""
import sys
from pathlib import Path

import fr_map as M

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "index.html"
OUT_DIR = ROOT / "fr"
BASE_URL = "https://h7k3r.com"

GROUPS = [M.HEAD, M.MODAL, M.HEADER, M.HOME, M.HARDWARE, M.GEAR,
          M.REPAIR, M.GALLERY, M.CONSULTING, M.FILES, M.GAMES]

HREFLANG = (
    '\n<link rel="alternate" hreflang="en" href="%s/">'
    '\n<link rel="alternate" hreflang="fr" href="%s/fr/">'
    '\n<link rel="alternate" hreflang="x-default" href="%s/">' % (BASE_URL, BASE_URL, BASE_URL)
)

# Language switcher pill, dropped in just before </nav>.
SWITCH = ('<a href="%s" class="nav-btn" id="lang-switch" aria-label="%s" '
          'style="border-color:#3f3f46;color:#fff">%s</a>\n            </nav>')


def apply_pairs(html, pairs):
    for pair in pairs:
        en, fr = pair[0], pair[1]
        want = pair[2] if len(pair) > 2 else 1
        got = html.count(en)
        if got != want:
            sys.exit("STOP: expected %d of %r, found %d" % (want, en[:60], got))
        html = html.replace(en, fr)
    return html


def add_hreflang(html):
    if "hreflang" in html:
        return html
    marker = "</title>"
    return html.replace(marker, marker + HREFLANG, 1)


def main():
    en = SRC.read_text(encoding="utf-8")

    # 1. French page.
    fr = en
    for g in GROUPS:
        fr = apply_pairs(fr, g)
    fr = add_hreflang(fr)
    # Assets are referenced relatively; <base> makes them resolve from the root
    # so /fr/ loads the same images, game and downloads as the English page.
    fr = fr.replace('<meta charset="UTF-8">',
                    '<meta charset="UTF-8">\n    <base href="/">', 1)
    fr = fr.replace("</nav>", SWITCH % ("/", "English version", "EN"), 1)
    OUT_DIR.mkdir(exist_ok=True)
    (OUT_DIR / "index.html").write_text(fr, encoding="utf-8")

    # 2. English page: hreflang + a switcher that points at /fr/.
    en2 = add_hreflang(en)
    if "lang-switch" not in en2:
        en2 = en2.replace("</nav>", SWITCH % ("/fr/", "Version française", "FR"), 1)
    SRC.write_text(en2, encoding="utf-8")

    print("fr/index.html: %d bytes" % len(fr))
    print("index.html updated with hreflang + FR switcher")
    # Leftover English in the French <body>, ignoring scripts/styles, is worth a look.


if __name__ == "__main__":
    main()
