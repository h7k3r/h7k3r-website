"""Build fr/index.html (French h7k3r.com) and keep the English index.html's
EN/FR switcher, hreflang and language auto-detect in place.

    python3 scripts/build-fr.py

English stays the default. A visitor whose browser is set to French is sent
to /fr/ automatically, unless they have picked a language with the switcher
(that choice is remembered and always wins).

Every English string in fr_map.py must be found the expected number of times,
or the build stops and names the one that is wrong — so after editing
index.html, run this again and fix whatever it reports.
"""
import re
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

# Same snippet on every page of every site: English by default, French for
# French browsers, never against a choice made with the switcher.
LANGJS = (
    "<script>(function(){try{var K='h7k_lang',p=location.pathname,onFr=/^\\/fr(\\/|$)/.test(p),s=null;"
    "try{s=localStorage.getItem(K)}catch(e){}"
    "document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('[data-lang]');"
    "if(a){try{localStorage.setItem(K,a.getAttribute('data-lang'))}catch(e){}}});"
    "if(onFr||s)return;var L=(navigator.languages||[navigator.language||'']).join(',').toLowerCase();"
    "if(/(^|,)fr(-[a-z]+)?(,|$)/.test(L)){location.replace((p==='/'?'/fr/':'/fr'+p)+location.search+location.hash)}}catch(e){}})();</script>"
)

SWITCH = ('<a href="%s" class="nav-btn" id="lang-switch" data-lang="%s" aria-label="%s" '
          'style="border-color:#3f3f46;color:#fff">%s</a>\n            </nav>')
OLD_SWITCH = re.compile(r'<a href="[^"]*" class="nav-btn" id="lang-switch"[^>]*>[A-Z]{2}</a>\n\s*</nav>')
OLD_JS = re.compile(r"<script>\(function\(\)\{try\{var K='h7k_lang'.*?</script>\n?", re.S)


def apply_pairs(html, pairs):
    for pair in pairs:
        en, fr = pair[0], pair[1]
        want = pair[2] if len(pair) > 2 else 1
        got = html.count(en)
        if got != want:
            sys.exit("STOP: expected %d of %r, found %d" % (want, en[:60], got))
        html = html.replace(en, fr)
    return html


def clean_source(html):
    """English page without its switcher or language script, so both pages are
    built from the same base and each gets exactly one switcher."""
    html = OLD_SWITCH.sub("</nav>", html)
    html = OLD_JS.sub("", html)
    if "hreflang" not in html:
        html = html.replace("</title>", "</title>" + HREFLANG, 1)
    return html


def with_lang_js(html):
    return html.replace("</head>", LANGJS + "\n</head>", 1)


def main():
    src = clean_source(SRC.read_text(encoding="utf-8"))

    # 1. French page.
    fr = src
    for g in GROUPS:
        fr = apply_pairs(fr, g)
    # Assets are referenced relatively; <base> makes them resolve from the root
    # so /fr/ loads the same images, game and downloads as the English page.
    fr = fr.replace('<meta charset="UTF-8">', '<meta charset="UTF-8">\n    <base href="/">', 1)
    fr = fr.replace("</nav>", SWITCH % ("/", "en", "English version", "EN"), 1)
    fr = with_lang_js(fr)
    OUT_DIR.mkdir(exist_ok=True)
    (OUT_DIR / "index.html").write_text(fr, encoding="utf-8")

    # 2. English page: one FR switcher + the language script.
    en = src.replace("</nav>", SWITCH % ("/fr/", "fr", "Version française", "FR"), 1)
    en = with_lang_js(en)
    SRC.write_text(en, encoding="utf-8")

    for name, html in (("index.html", en), ("fr/index.html", fr)):
        n = html.count('id="lang-switch"')
        if n != 1:
            sys.exit("STOP: %s has %d language switchers" % (name, n))
    print("fr/index.html: %d bytes; one switcher per page; auto-detect added" % len(fr))


if __name__ == "__main__":
    main()
