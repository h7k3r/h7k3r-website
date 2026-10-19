"""Build the standalone service pages for h7k3r.com (good for Google: one page per job and area).

    python3 scripts/build_pages.py

Writes repair/croydon/, repair/kingston/, data-recovery/ and custom-pc/ (index.html each)
and refreshes sitemap.xml. Edit the PAGES list below and run again.

Honesty rules (same as the main site): no review stars or computed ratings, no
Review/AggregateRating schema, proof lines are quoted exactly as on the main page,
and nothing is promised that the business does not do.
"""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://h7k3r.com"
FORM = "https://formspree.io/f/mnjblgln"
GOOGLE = ("https://www.google.com/maps/place/Game+On/@51.3736532,-0.0998115,17z/data=!3m1!4b1!4m6!3m5!1s0x4876073151b74c2f"
          ":0xebac085c7d7653ff!8m2!3d51.3736532!4d-0.0998115!16s%2Fg%2F11c45tfxzj")
EBAY = "https://www.ebay.co.uk/fdbk/feedback_profile/h7k3r-0"
TODAY = "2026-10-20"

PROOF = [
    ("37 five-star Google reviews name me personally.", GOOGLE, "Read them on Google"),
    ("10 years running the repair desk at Game On, Croydon.", None, None),
    ("670 repair technicians trained for the WeFix network in France.", None, None),
    ("100% positive on eBay since 2017.", EBAY, "eBay feedback profile"),
]

REPAIR_FIXES = [
    ("Phones", "iPhone, Samsung Galaxy and Google Pixel: cracked screens, tired batteries, charging ports, cameras, speakers and water damage."),
    ("Laptops and MacBooks", "Screens, hinges, keyboards, batteries, slow machines, virus removal, Windows reinstalls, SSD and memory upgrades."),
    ("Tablets", "iPad and Android tablets: glass, LCD, battery and charging faults."),
    ("Consoles and controllers", "PlayStation, Xbox and Switch: HDMI ports, overheating, discs, stick drift and buttons."),
    ("Board-level repair", "Devices that won't turn on: shorts and burnt components found and replaced under a stereo microscope."),
    ("Data rescue", "Dead phones and clicking drives: we get your photos and files back when other shops say it's gone."),
]

FAQ_REPAIR = [
    ("How fast is a repair?",
     "Cracked screens, dying batteries and broken charging ports are typically completed within 24 to 48 hours. "
     "Board-level and data recovery jobs take longer; you get a time frame with your quote."),
    ("Do I have to come to a shop?",
     "No. We collect from you or visit you in {area}, or you can post the device to us. You get the posting details when you book."),
    ("How much will it cost?",
     "Every device and fault is different, so you get a free, fixed quote before any work starts. If you say no, you pay nothing."),
    ("Who will repair my device?",
     "The same engineer who ran the repair desk at Game On in Croydon for ten years and trained 670 repair technicians for the WeFix network in France. "
     "Your device isn't passed around a chain."),
]


def page_repair(area, slug, intro, places, extra):
    faq = [(q, a.format(area=area)) for q, a in FAQ_REPAIR]
    return dict(
        path=f"repair/{slug}/",
        title=f"Phone & Laptop Repair in {area} | H7K3R Systems",
        desc=(f"Phone, laptop, tablet and console repair in {area}. Collection, home visits or post-in, "
              f"free fixed quote, most screens and batteries in 24 to 48 hours. Free quote online."),
        h1=f"Phone &amp; laptop repair in {html.escape(area)}",
        kicker=f"{html.escape(area)} · collection, visits or post-in",
        lead=intro,
        service="REPAIR_EVERYDAY",
        how=[
            ("Tell us what's wrong", "Send the form. You get a free, fixed quote, usually the same day."),
            ("We collect or you post it", f"We collect from home or work in {html.escape(area)}, visit you, or you post the device to us."),
            ("Fixed and returned", "Most screens, batteries and ports are done in 24 to 48 hours, then it comes straight back to you."),
        ],
        blocks=[("What we fix", REPAIR_FIXES)],
        places=places,
        extra=extra,
        faq=faq,
        area=area,
        schema_service="Phone, laptop, tablet and console repair",
    )


PAGES = [
    page_repair(
        "Croydon", "croydon",
        "For ten years I ran the device repair desk at Game On in Croydon. H7K3R Systems is that same bench, now coming to you: "
        "we collect your phone, laptop or console, fix it properly and bring it back, or you post it in.",
        ["Croydon town centre", "South Croydon", "Addiscombe", "Shirley", "Selsdon", "Sanderstead", "Purley", "Coulsdon",
         "Thornton Heath", "Norbury", "Norwood", "New Addington", "Waddon", "Wallington"],
        "Croydon has been home to this bench since Game On: phones, MacBook boards and consoles, including the jobs other shops had already turned away.",
    ),
    page_repair(
        "Kingston upon Thames", "kingston",
        "Phone, laptop, tablet and console repair for Kingston and the surrounding area, from the engineer who ran the Game On repair desk in Croydon for a decade. "
        "We collect, visit or you post it in, and you get a free fixed quote first.",
        ["Kingston town centre", "Surbiton", "Norbiton", "New Malden", "Tolworth", "Berrylands", "Chessington",
         "Kingston Vale", "Coombe", "Hook", "Ham", "Teddington"],
        "No queue at a counter and no device left in a back room for a week: you deal with the engineer who does the repair.",
    ),
    dict(
        path="data-recovery/",
        title="Data Recovery: Dead Drives & Water-Damaged Phones | H7K3R Systems",
        desc=("Laboratory data recovery for clicking hard drives, dead SSDs and water-damaged phones. Clean bench, board-level "
              f"repair under a microscope, UK-wide post-in, collection in Croydon and Kingston. Free quote online."),
        h1="Data recovery for drives and phones others gave up on",
        kicker="Croydon · Kingston · post-in from anywhere in the UK",
        lead=("When a hard drive clicks or a phone is completely dead from water damage, software isn't enough. We take devices apart on a "
              "dust-free bench, rebuild what's broken and extract your photos, documents and work."),
        service="DATA_RECOVERY",
        how=[
            ("Stop using it", "Power the device off. Every extra minute on a failing drive can make recovery harder."),
            ("Send it or we collect", "Post it to us from anywhere in the UK, or we collect in Croydon and Kingston."),
            ("Diagnosis, then your data", "You get a diagnosis and a fixed price before recovery starts, then your files back on a new drive."),
        ],
        blocks=[("What we recover from", [
            ("Clicking or silent hard drives", "Heads, motors and firmware faults handled on a clean bench."),
            ("Dead SSDs and memory", "Controller and power faults, including drives that are no longer detected."),
            ("Water-damaged phones", "Boards cleaned and repaired so the phone boots long enough to extract your data."),
            ("Phones that won't turn on", "Shorts and burnt chips found and replaced under a stereo microscope."),
            ("Laptops and MacBooks", "Data pulled from failed boards and soldered storage."),
            ("Memory cards and USB sticks", "Photos and files recovered from cards cameras and phones can no longer read."),
        ])],
        places=["Croydon", "Kingston upon Thames", "Sutton", "Bromley", "Merton", "Wandsworth", "anywhere in the UK by post"],
        extra="Your data stays private: one engineer handles your device from start to finish, and recovered files are only returned to you.",
        faq=[
            ("Can you recover data from a phone that won't turn on?",
             "Often, yes. Many dead phones have a board fault rather than dead storage. We repair the board enough to boot it and extract your data."),
            ("How much does data recovery cost?",
             "It depends on the fault. You get a diagnosis and a fixed price before any recovery work, so there are no surprises."),
            ("Should I try recovery software first?",
             "Not on a clicking or failing drive. Running it can cause more damage. Switch it off and get it looked at."),
            ("Do you work with businesses?",
             "Yes. We recover data for sole traders and companies, and can also set up backups so it doesn't happen again."),
        ],
        area="Croydon and Kingston upon Thames",
        schema_service="Data recovery",
    ),
    dict(
        path="custom-pc/",
        title="Custom Gaming PCs Built in Croydon | H7K3R Systems",
        desc=("Custom gaming and workstation PCs designed and built by hand in Croydon, from £449. Tuned, stress-tested and ready to play. "
              "Send your spec for a free quote."),
        h1="Custom gaming PCs, built by hand in Croydon",
        kicker="From £449 · tuned and stress-tested",
        lead=("Every build is planned around what you play or render, assembled by the same engineer who ranks on the HWBOT overclocking boards, "
              "and stress-tested before it leaves the bench."),
        service="CUSTOM_RIG",
        how=[
            ("Tell us what it's for", "Games, resolution, software, budget. Or pick one of the builds below."),
            ("We spec and quote", "You get a parts list and a fixed price. Nothing is ordered until you agree."),
            ("Built, tested, handed over", "Assembled, cable-managed, stress-tested and set up. Collection or delivery is agreed when you order."),
        ],
        blocks=[("Starting points", [
            ("VENO_KILLER · £449", "A budget-friendly powerhouse designed to outperform off-the-shelf market PCs without the e-waste."),
            ("PROJECT_P · £850", "Built for solid 1440p gaming and reliable multi-threaded productivity tasks."),
            ("XPROTO_STEALTH · £1,850", "A stunning, open-air miniature build prioritizing aesthetics and raw airflow."),
            ("APEX_NODE · £2,100", "Zero bottlenecks. Optimized for competitive high-refresh-rate esports titles."),
            ("TRIDENT APEX · £8,610", "Our flagship rig. Engineered for massive CAD rendering, AI generation, and uncompromised 4K fidelity."),
            ("Your own spec", "Have a parts list already? We'll check it, build it and tune it."),
        ])],
        places=["Croydon", "Kingston upon Thames", "South London", "Surrey"],
        extra="Upgrades and rebuilds too: we can take your current PC, keep what's still good and replace the rest.",
        faq=[
            ("Why not just buy a prebuilt PC?",
             "Prebuilts often save money on the parts you don't see: power supply, motherboard and cooling. We pick every part for your use and tune it."),
            ("Can I bring my own parts?",
             "Yes. We'll build with them, check everything works together and tell you honestly if a part is holding the system back."),
            ("Do you upgrade existing PCs?",
             "Yes: graphics cards, storage, memory, cooling, and full rebuilds into a new case."),
            ("Is the build tested?",
             "Every PC is stress-tested and checked for temperatures and stability before it is handed over."),
        ],
        area="Croydon",
        schema_service="Custom PC building",
    ),
]

CSS = """
:root{--bg:#05060c;--panel:rgba(18,21,34,.72);--line:rgba(120,140,190,.16);--ink:#eef2ff;--muted:#9aa6c4;--cyan:#22d3ee;--violet:#8b74ff}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:radial-gradient(1100px 600px at 80% -10%,rgba(139,116,255,.16),transparent 60%),radial-gradient(900px 500px at 0% 10%,rgba(34,211,238,.10),transparent 60%),var(--bg);color:var(--ink);font:16px/1.65 Inter,system-ui,sans-serif;-webkit-font-smoothing:antialiased}
a{color:var(--cyan)}
.wrap{width:min(1100px,100% - 32px);margin:0 auto}
header{position:sticky;top:0;z-index:20;background:rgba(5,6,12,.82);backdrop-filter:blur(14px);border-bottom:1px solid var(--line)}
.hd{display:flex;align-items:center;gap:14px;height:64px}
.brand{display:flex;align-items:center;gap:9px;color:#fff;text-decoration:none;font-family:Orbitron,sans-serif;letter-spacing:.16em;font-size:15px;margin-right:auto}
.brand b{background:linear-gradient(90deg,#7defe6,#8b74ff);-webkit-background-clip:text;background-clip:text;color:transparent}
.brand span{color:#a1a1aa;font-weight:400}
.call{color:#fff;text-decoration:none;font-family:'JetBrains Mono',monospace;font-size:13px;padding:9px 12px;border:1px solid var(--line);border-radius:10px;white-space:nowrap}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;padding:13px 20px;border-radius:12px;font-weight:700;text-decoration:none;border:0;cursor:pointer;font-size:15px}
.btn-p{background:var(--cyan);color:#04121a;box-shadow:0 10px 30px -10px rgba(34,211,238,.7)}
.btn-g{background:transparent;color:#fff;border:1px solid var(--line)}
.hero{padding:64px 0 40px}
.kick{font-family:'JetBrains Mono',monospace;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--cyan)}
h1{font-family:Orbitron,sans-serif;font-size:clamp(28px,5vw,48px);line-height:1.12;letter-spacing:.02em;margin:14px 0 16px;max-width:18ch}
.lead{color:#c7cee3;font-size:clamp(16px,2vw,18.5px);max-width:62ch}
.ctas{display:flex;flex-wrap:wrap;gap:12px;margin-top:26px}
section{padding:40px 0;border-top:1px solid var(--line)}
h2{font-family:Orbitron,sans-serif;font-size:clamp(20px,3vw,26px);letter-spacing:.06em;margin:0 0 20px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));gap:14px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:20px}
.card h3{margin:0 0 6px;font-size:17px}.card p{margin:0;color:var(--muted);font-size:15px}
.steps{counter-reset:s;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,260px),1fr));gap:14px}
.steps .card{position:relative;padding-top:46px}
.steps .card::before{counter-increment:s;content:counter(s,decimal-leading-zero);position:absolute;top:16px;left:20px;font-family:'JetBrains Mono',monospace;color:var(--cyan);font-size:13px}
.proof{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,240px),1fr));gap:14px}
.proof .card p{color:#e4e8f5;font-size:16px}.proof .card a{display:inline-block;margin-top:10px;font-size:13px}
.places{display:flex;flex-wrap:wrap;gap:8px;list-style:none;padding:0;margin:0}
.places li{padding:7px 12px;border:1px solid var(--line);border-radius:99px;color:#c7cee3;font-size:14px}
.note{color:#c7cee3;margin-top:16px}
details{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:16px 18px;margin-bottom:10px}
summary{cursor:pointer;font-weight:600}details p{color:var(--muted);margin:10px 0 0}
.quote{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.quote label{display:flex;flex-direction:column;gap:6px;font-size:13px;color:#c7cee3;font-weight:600}
.quote .full{grid-column:1/-1}
.quote input,.quote textarea,.quote select{background:#0b0e18;border:1px solid #2a3150;border-radius:10px;padding:12px;color:#fff;font:inherit}
.quote textarea{min-height:110px;resize:vertical}
.quote input:focus,.quote textarea:focus{outline:none;border-color:var(--cyan)}
.ok{display:none;padding:22px;border-radius:14px;border:1px solid rgba(34,211,238,.4);background:rgba(34,211,238,.06)}
.err{display:none;color:#fca5a5}
.links{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,220px),1fr));gap:10px}
.links a{display:block;padding:14px 16px;border:1px solid var(--line);border-radius:12px;color:#fff;text-decoration:none;background:var(--panel)}
footer{padding:30px 0 60px;color:#71717a;font-size:13px;border-top:1px solid var(--line)}
@media (max-width:640px){.quote{grid-template-columns:1fr}.call{display:none}.hero{padding-top:40px}}
"""

ALL_LINKS = [
    ("repair/croydon/", "Phone & laptop repair in Croydon"),
    ("repair/kingston/", "Phone & laptop repair in Kingston"),
    ("data-recovery/", "Data recovery"),
    ("custom-pc/", "Custom gaming PCs"),
]


def render(p):
    e = html.escape
    url = BASE + "/" + p["path"]
    biz = {
        "@type": "LocalBusiness", "@id": BASE + "/#business", "name": "H7K3R Systems", "url": BASE + "/",
        "image": BASE + "/og-image.jpg", "logo": BASE + "/apple-touch-icon.png",
        "areaServed": [{"@type": "City", "name": "Croydon"}, {"@type": "City", "name": "Kingston upon Thames"},
                       {"@type": "Country", "name": "United Kingdom"}],
    }
    graph = [
        biz,
        {"@type": "Service", "name": p["schema_service"], "provider": {"@id": BASE + "/#business"},
         "areaServed": p["area"], "url": url},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "H7K3R Systems", "item": BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": p["h1"].replace("&amp;", "&"), "item": url}]},
    ]
    blocks = "".join(
        f'<section><div class="wrap"><h2>{e(t)}</h2><div class="grid">'
        + "".join(f'<div class="card"><h3>{e(a)}</h3><p>{e(b)}</p></div>' for a, b in items)
        + "</div></div></section>" for t, items in p["blocks"])
    how = "".join(f'<div class="card"><h3>{e(a)}</h3><p>{b}</p></div>' for a, b in p["how"])
    proof = "".join(f'<div class="card"><p>{e(t)}</p>' + (f'<a href="{e(u)}" target="_blank" rel="noopener">{e(l)} &#8599;</a>' if u else "") + "</div>"
                    for t, u, l in PROOF)
    places = "".join(f"<li>{e(x)}</li>" for x in p["places"])
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in p["faq"])
    others = "".join(f'<a href="/{u}">{e(l)} &rarr;</a>' for u, l in ALL_LINKS if u != p["path"]) + '<a href="/">Everything H7K3R does &rarr;</a>'
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(p['title'])}</title>
<meta name="description" content="{e(p['desc'])}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{e(p['title'])}">
<meta property="og:description" content="{e(p['desc'])}">
<meta property="og:url" content="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="en_GB">
<meta property="og:site_name" content="H7K3R Systems">
<meta property="og:image" content="{BASE}/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#05060c">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&family=Inter:wght@400;600;700&family=JetBrains+Mono:wght@400&display=swap" rel="stylesheet">
<script type="application/ld+json">{json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)}</script>
<style>{CSS}</style>
</head>
<body>
<header><div class="wrap hd">
  <a class="brand" href="/"><svg width="22" height="22" viewBox="0 0 24 24" aria-hidden="true"><path d="M13 2 4 14h6l-1 8 9-12h-6z" fill="none" stroke="#22d3ee" stroke-width="1.9" stroke-linejoin="round"/></svg><b>H7K3R</b><span>SYSTEMS</span></a>
  <a class="btn btn-p" href="#quote">Free quote</a>
</div></header>
<main>
<div class="wrap hero">
  <div class="kick">{p['kicker']}</div>
  <h1>{p['h1']}</h1>
  <p class="lead">{e(p['lead'])}</p>
  <div class="ctas"><a class="btn btn-p" href="#quote">Get a free quote</a><a class="btn btn-g" href="#how">How it works</a></div>
</div>
<section id="how"><div class="wrap"><h2>How it works</h2><div class="steps">{how}</div></div></section>
{blocks}
<section><div class="wrap"><h2>Why people choose us</h2><div class="proof">{proof}</div><p class="note">{e(p['extra'])}</p></div></section>
<section><div class="wrap"><h2>Areas we cover</h2><ul class="places">{places}</ul></div></section>
<section><div class="wrap"><h2>Questions</h2>{faq}</div></section>
<section id="quote"><div class="wrap"><h2>Get a free quote</h2>
  <form class="quote" id="qf" action="{FORM}" method="POST">
    <input type="hidden" name="_subject" value="H7K3R enquiry: {e(p['schema_service'])} ({e(p['area'])})">
    <input type="hidden" name="interest" value="{p['service']}">
    <input type="hidden" name="page" value="/{p['path']}">
    <input type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:-9999px;width:1px;height:1px;opacity:0">
    <label>Your name<input name="name" required autocomplete="name"></label>
    <label>Email<input type="email" name="email" required autocomplete="email"></label>
    <label class="full">Phone (optional)<input type="tel" name="phone" autocomplete="tel"></label>
    <label class="full">What's going on?<textarea name="msg" placeholder="Device, model and what happened"></textarea></label>
    <div class="full"><button class="btn btn-p" type="submit" id="qs">Send</button> <span class="err" id="qe">Sorry, that didn't send. Check your connection and try again in a moment.</span></div>
  </form>
  <p class="note">We only use your details to reply to this enquiry. <a href="/privacy/">Privacy notice</a></p>
  <div class="ok" id="qo"><h3>Message received</h3><p>Thanks, we'll reply by email within 24 hours.</p></div>
</div></section>
<section><div class="wrap"><h2>More from H7K3R</h2><div class="links">{others}</div></div></section>
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


def sitemap():
    rows = [
        ("/", True), ("/fr/", True),
    ] + [("/" + p["path"], False) for p in PAGES]
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for loc, alt in rows:
        out.append("  <url>")
        out.append(f"    <loc>{BASE}{loc}</loc>")
        out.append(f"    <lastmod>{TODAY}</lastmod>")
        if alt:
            for lang, href in (("en", "/"), ("fr", "/fr/"), ("x-default", "/")):
                out.append(f'    <xhtml:link rel="alternate" hreflang="{lang}" href="{BASE}{href}"/>')
        out.append("  </url>")
    out.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    for p in PAGES:
        d = ROOT / p["path"]
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(render(p), encoding="utf-8")
        print("wrote", p["path"])
    sitemap()
    print("sitemap.xml updated")
