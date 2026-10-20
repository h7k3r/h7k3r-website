"""Build one page per gear product: /gear/<slug>/ (good for Google: each product can rank).

    python3 scripts/build_gear_pages.py

Products, prices and copy live in scripts/gear_data.py. Run build_pages.py too,
so sitemap.xml lists these pages.
There is no online checkout: each page has an order enquiry form (Formspree),
and we confirm availability, payment and delivery or collection by email.
"""
import html
import json
from pathlib import Path

from build_pages import CSS, FORM
from gear_data import PRODUCTS

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://h7k3r.com"

EXTRA_CSS = """
.ph{display:grid;gap:28px;align-items:center;padding:48px 0 36px}
@media(min-width:900px){.ph{grid-template-columns:1.05fr 1fr;gap:44px}}
.ph figure{margin:0;min-width:0}
.ph img{display:block;width:100%;height:auto;border-radius:18px;border:1px solid var(--line);background:#070912}
.ph figcaption{margin-top:8px;font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.ph h1{max-width:none}
.price{font-family:'JetBrains Mono',monospace;font-size:28px;color:#fff;margin:6px 0 4px}
.price small{display:block;font-size:12px;letter-spacing:.06em;color:var(--muted);margin-top:4px}
.checks{margin:0;padding-left:1.2em;color:#c7cee3;max-width:70ch}
.checks li{margin:8px 0}
.gear-more{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,210px),1fr));gap:12px}
.gear-more a{display:block;padding:14px 16px;border:1px solid var(--line);border-radius:14px;background:var(--panel);color:#fff;text-decoration:none}
.gear-more a span{display:block;font-family:'JetBrains Mono',monospace;font-size:13px;color:var(--muted);margin-top:4px}
.gear-more a:hover{border-color:var(--cyan)}
"""


def page(p):
    e = html.escape
    url = f"{BASE}/gear/{p['slug']}/"
    img = f"/gear/p/{p['img']}"
    title = f"{p['title']} | H7K3R Systems"
    graph = [
        {"@type": "Product", "name": p["name"], "description": p["desc"], "image": f"{BASE}{img}-1280.webp",
         "brand": {"@type": "Brand", "name": "H7K3R Systems"}, "url": url,
         "offers": {"@type": "Offer", "price": p["price"], "priceCurrency": "GBP", "url": url,
                    "seller": {"@id": BASE + "/#business"}}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "H7K3R Systems", "item": BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Privacy gear", "item": BASE + "/#gear"},
            {"@type": "ListItem", "position": 3, "name": p["name"], "item": url}]},
    ]
    uses = "".join(f'<div class="card"><h3>{e(a)}</h3><p>{e(b)}</p></div>' for a, b in p["uses"])
    checks = "".join(f"<li>{e(c)}</li>" for c in p["check"])
    check_block = (f'<section><div class="wrap"><h2>Good to know</h2><ul class="checks">{checks}</ul></div></section>'
                   if checks else "")
    others = "".join(f'<a href="/gear/{o["slug"]}/">{e(o["name"])}<span>£{o["price"]}</span></a>'
                     for o in PRODUCTS if o["slug"] != p["slug"])
    note = f'<p class="note">{e(p["note"])}</p>' if p["note"] else ""
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(p['desc'])}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(p['desc'])}">
<meta property="og:url" content="{url}">
<meta property="og:type" content="product">
<meta property="og:locale" content="en_GB">
<meta property="og:site_name" content="H7K3R Systems">
<meta property="og:image" content="{BASE}{img}-1280.webp">
<meta property="og:image:width" content="1280">
<meta property="og:image:height" content="768">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#05060c">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&family=Inter:wght@400;600;700&family=JetBrains+Mono:wght@400&display=swap" rel="stylesheet">
<script type="application/ld+json">{json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)}</script>
<style>{CSS}{EXTRA_CSS}</style>
</head>
<body>
<header><div class="wrap hd">
  <a class="brand" href="/"><svg width="22" height="22" viewBox="0 0 24 24" aria-hidden="true"><path d="M13 2 4 14h6l-1 8 9-12h-6z" fill="none" stroke="#22d3ee" stroke-width="1.9" stroke-linejoin="round"/></svg><b>H7K3R</b><span>SYSTEMS</span></a>
  <a class="btn btn-p" href="#order">Order</a>
</div></header>
<main>
<div class="wrap ph">
  <figure>
    <img src="{img}-800.webp" srcset="{img}-480.webp 480w, {img}-800.webp 800w, {img}-1280.webp 1280w" sizes="(min-width:900px) 52vw, 100vw" width="1280" height="768" alt="{e(p['name'])} (illustration)">
    <figcaption>Illustration</figcaption>
  </figure>
  <div>
    <div class="kick"><a href="/#gear" style="color:inherit;text-decoration:none">Privacy gear</a> · H7K3R Systems</div>
    <h1>{e(p['name'])}</h1>
    <p class="lead">{e(p['line'])} {e(p['intro'])}</p>
    <div class="price">£{p['price']}<small>Order by email · collection in Croydon or Kingston, or we arrange delivery</small></div>
    <div class="ctas"><a class="btn btn-p" href="#order">Order this</a><a class="btn btn-g" href="/#gear">All gear</a></div>
  </div>
</div>
<section><div class="wrap"><h2>What it's for</h2><div class="grid">{uses}</div>{note}</div></section>
{check_block}
<section id="order"><div class="wrap"><h2>Order the {e(p['name'])}</h2>
  <p class="note" style="margin:-6px 0 18px">There's no online checkout yet. Send this and we reply by email to confirm availability, payment and delivery or collection.</p>
  <form class="quote" id="qf" action="{FORM}" method="POST">
    <input type="hidden" name="_subject" value="H7K3R gear order: {e(p['name'])} (£{p['price']})">
    <input type="hidden" name="interest" value="PRIVACY_GEAR">
    <input type="hidden" name="product" value="{e(p['name'])}">
    <input type="hidden" name="page" value="/gear/{p['slug']}/">
    <input type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:-9999px;width:1px;height:1px;opacity:0">
    <label>Your name<input name="name" required autocomplete="name"></label>
    <label>Email<input type="email" name="email" required autocomplete="email"></label>
    <label class="full">Phone (optional)<input type="tel" name="phone" autocomplete="tel"></label>
    <label class="full">Quantity, size or colour, and delivery or collection<textarea name="msg" placeholder="e.g. 2 pouches, collection in Croydon"></textarea></label>
    <div class="full"><button class="btn btn-p" type="submit" id="qs">Send order request</button> <span class="err" id="qe">Sorry, that didn't send. Check your connection and try again in a moment.</span></div>
  </form>
  <p class="note">We only use your details to reply to this order. <a href="/privacy/">Privacy notice</a></p>
  <div class="ok" id="qo"><h3>Order request received</h3><p>Thanks, we'll reply by email within 24 hours.</p></div>
</div></section>
<section><div class="wrap"><h2>More privacy gear</h2><div class="gear-more">{others}</div></div></section>
</main>
<footer><div class="wrap">H7K3R Systems · Croydon &amp; Kingston upon Thames · <a href="/">h7k3r.com</a> · <a href="/privacy/">Privacy notice</a></div></footer>
<script>
(function(){{var f=document.getElementById('qf');f.addEventListener('submit',function(e){{e.preventDefault();var b=document.getElementById('qs'),er=document.getElementById('qe');er.style.display='none';b.disabled=true;
fetch(f.action,{{method:'POST',body:new FormData(f),headers:{{Accept:'application/json'}}}}).then(function(r){{if(!r.ok)throw 0;f.style.display='none';document.getElementById('qo').style.display='block';}})
.catch(function(){{er.style.display='inline';}}).then(function(){{b.disabled=false;}});}});}})();
</script>
</body>
</html>
"""


if __name__ == "__main__":
    for p in PRODUCTS:
        d = ROOT / "gear" / p["slug"]
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(page(p), encoding="utf-8")
        print("wrote gear/%s/" % p["slug"])
