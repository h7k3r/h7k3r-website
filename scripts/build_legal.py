"""Build the privacy notice (EN + FR) and the 404 page for h7k3r.com.

    python3 scripts/build_legal.py

Writes privacy/index.html, fr/privacy/index.html and 404.html.
404.html also stops Cloudflare Pages from serving the homepage for every
unknown address (with no top-level 404.html it assumes a single-page app,
which Google reports as "soft 404" duplicates).
Edit the text below and run again.
"""
import html
from pathlib import Path

from build_pages import CSS

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://h7k3r.com"
UPDATED_EN = "20 October 2026"
UPDATED_FR = "20 octobre 2026"

EXTRA_CSS = """
.legal{padding:56px 0 40px}
.legal h1{max-width:none}
.legal h2{font-size:clamp(17px,2.4vw,20px);margin:36px 0 10px}
.legal p,.legal li{color:#c7cee3;max-width:70ch}
.legal ul{padding-left:1.2em}
.legal li{margin:6px 0}
.legal .upd{font-family:'JetBrains Mono',monospace;font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
.nf{padding:90px 0 70px;text-align:left}
.nf .code{font-family:Orbitron,sans-serif;font-size:clamp(64px,14vw,120px);line-height:1;background:linear-gradient(90deg,#7defe6,#8b74ff);-webkit-background-clip:text;background-clip:text;color:transparent}
.nf .links{display:flex;flex-wrap:wrap;gap:12px;margin-top:26px}
"""

PRIVACY_EN = [
    ("Who we are",
     "<p>H7K3R Systems is a device repair, data recovery and custom PC business run by a sole trader in the United Kingdom, "
     "serving Croydon, Kingston upon Thames and customers across the UK who post their devices in. "
     "H7K3R Systems is the controller of the personal data described here.</p>"
     "<p>To ask anything about your data, send a message through the enquiry form on "
     "<a href=\"/\">h7k3r.com</a> (any service, and say it is about your data) or reply to any email we have sent you.</p>"),
    ("What we collect",
     "<ul>"
     "<li><b>When you send an enquiry:</b> your name, email address, phone number if you give one, the service you need and what you tell us about your device.</li>"
     "<li><b>When you book a repair or send a device:</b> the address we collect from or return to, the device's make, model and fault, and what we find and do.</li>"
     "<li><b>Payments:</b> the amount, date and method. We never see or keep full card details.</li>"
     "</ul>"),
    ("The data on your device",
     "<p>We only access what is on your device as far as the repair or recovery needs. We don't browse, copy or keep your photos, messages or files. "
     "For a screen or battery job we normally don't need your passcode. For a data recovery you asked for, the recovered files are handed back to you, "
     "and our working copy is deleted once you confirm you have them.</p>"),
    ("Why we use it",
     "<ul>"
     "<li>To reply to you, give a quote and carry out the work you ask for: this is needed to take steps at your request and to perform our agreement with you.</li>"
     "<li>To keep records of jobs and payments: we have a legal duty to keep accounting records.</li>"
     "<li>To honour warranties and deal with any problem afterwards: our legitimate interest in standing behind our work.</li>"
     "</ul>"
     "<p>We never sell your details, never add you to a mailing list and never use them for advertising.</p>"),
    ("Who else sees it",
     "<ul>"
     "<li><b>Formspree</b>, which delivers the website's enquiry forms to us and stores the submissions on our behalf. It is based in the United States; its data processing terms cover international transfers.</li>"
     "<li><b>Our email provider</b>, when we write back to you.</li>"
     "<li><b>Royal Mail or a courier</b>, only your name and address, when a device is posted to us or back to you.</li>"
     "<li><b>Website services</b>: Cloudflare delivers and protects this site, and fonts and some page code load from Google Fonts and Tailwind's CDN. These see your device's IP address, as any website does.</li>"
     "</ul>"),
    ("Cookies and tracking",
     "<p>We don't use advertising or analytics cookies, and we don't track you across other sites. "
     "Your browser stores a few small settings on your own device, such as your language choice and your initials on the arcade leaderboard. "
     "They never leave your device.</p>"),
    ("How long we keep it",
     "<ul>"
     "<li>Enquiries that don't lead to a job: deleted within 12 months.</li>"
     "<li>Job records and invoices: as long as UK tax law requires, normally six years.</li>"
     "<li>Recovered data: deleted once you confirm you have your files, and at the latest 30 days after we hand them back.</li>"
     "</ul>"),
    ("Your rights",
     "<p>You can ask for a copy of your data, ask us to correct or delete it, object to how we use it or ask us to limit it, "
     "and ask for data you gave us in a portable format. We reply within one month.</p>"
     "<p>If you're unhappy with how we've handled your data, you can complain to the Information Commissioner's Office: "
     "<a href=\"https://ico.org.uk/make-a-complaint/\" target=\"_blank\" rel=\"noopener\">ico.org.uk/make-a-complaint</a>, 0303 123 1113.</p>"),
]

PRIVACY_FR = [
    ("Qui sommes-nous",
     "<p>H7K3R Systems est une activité de réparation d'appareils, de récupération de données et de PC sur mesure, exercée par un entrepreneur individuel au Royaume-Uni. "
     "Nous intervenons à Croydon, à Kingston upon Thames et partout au Royaume-Uni pour les appareils envoyés par la poste. "
     "H7K3R Systems est responsable du traitement des données personnelles décrites ici.</p>"
     "<p>Pour toute question sur vos données, écrivez-nous via le formulaire de contact de "
     "<a href=\"/fr/\">h7k3r.com</a> (n'importe quel service, en précisant que cela concerne vos données) ou répondez à l'un de nos e-mails.</p>"),
    ("Ce que nous collectons",
     "<ul>"
     "<li><b>Quand vous nous écrivez :</b> votre nom, votre e-mail, votre numéro de téléphone si vous le donnez, le service souhaité et ce que vous nous dites de votre appareil.</li>"
     "<li><b>Quand vous réservez une réparation ou envoyez un appareil :</b> l'adresse de collecte ou de retour, la marque, le modèle et la panne de l'appareil, et ce que nous constatons et faisons.</li>"
     "<li><b>Paiements :</b> le montant, la date et le moyen de paiement. Nous ne voyons ni ne conservons jamais les numéros de carte complets.</li>"
     "</ul>"),
    ("Les données de votre appareil",
     "<p>Nous n'accédons au contenu de votre appareil que dans la mesure nécessaire à la réparation ou à la récupération. Nous ne parcourons, ne copions et ne conservons ni vos photos, ni vos messages, ni vos fichiers. "
     "Pour un écran ou une batterie, nous n'avons normalement pas besoin de votre code. Pour une récupération de données que vous avez demandée, les fichiers récupérés vous sont remis "
     "et notre copie de travail est supprimée dès que vous confirmez les avoir.</p>"),
    ("Pourquoi nous les utilisons",
     "<ul>"
     "<li>Pour vous répondre, établir un devis et réaliser le travail demandé : c'est nécessaire pour agir à votre demande et exécuter notre accord.</li>"
     "<li>Pour tenir le registre des interventions et des paiements : la loi nous oblige à conserver une comptabilité.</li>"
     "<li>Pour honorer la garantie et traiter un éventuel problème : notre intérêt légitime à assumer notre travail.</li>"
     "</ul>"
     "<p>Nous ne vendons jamais vos données, ne vous inscrivons à aucune liste de diffusion et ne les utilisons jamais à des fins publicitaires.</p>"),
    ("Qui d'autre y a accès",
     "<ul>"
     "<li><b>Formspree</b>, qui nous transmet les formulaires du site et conserve les envois pour notre compte. Formspree est basé aux États-Unis ; ses conditions de traitement des données encadrent les transferts internationaux.</li>"
     "<li><b>Notre fournisseur de messagerie</b>, lorsque nous vous répondons.</li>"
     "<li><b>Royal Mail ou un transporteur</b>, uniquement votre nom et votre adresse, quand un appareil nous est envoyé ou vous est retourné.</li>"
     "<li><b>Services du site</b> : Cloudflare diffuse et protège ce site, et les polices et une partie du code proviennent de Google Fonts et du CDN de Tailwind. Ces services voient l'adresse IP de votre appareil, comme pour tout site web.</li>"
     "</ul>"),
    ("Cookies et pistage",
     "<p>Nous n'utilisons aucun cookie publicitaire ou de mesure d'audience, et nous ne vous suivons pas sur d'autres sites. "
     "Votre navigateur garde quelques petits réglages sur votre propre appareil, comme la langue choisie ou vos initiales dans le classement de l'arcade. "
     "Ils ne quittent jamais votre appareil.</p>"),
    ("Durée de conservation",
     "<ul>"
     "<li>Demandes sans suite : supprimées sous 12 mois.</li>"
     "<li>Dossiers d'intervention et factures : aussi longtemps que l'exige le droit fiscal britannique, en général six ans.</li>"
     "<li>Données récupérées : supprimées dès que vous confirmez avoir vos fichiers, et au plus tard 30 jours après leur remise.</li>"
     "</ul>"),
    ("Vos droits",
     "<p>Vous pouvez demander une copie de vos données, leur rectification ou leur suppression, vous opposer à leur utilisation ou en demander la limitation, "
     "et recevoir les données que vous nous avez fournies dans un format réutilisable. Nous répondons sous un mois.</p>"
     "<p>Si vous n'êtes pas satisfait de la façon dont nous avons traité vos données, vous pouvez saisir l'autorité britannique de protection des données, l'ICO : "
     "<a href=\"https://ico.org.uk/make-a-complaint/\" target=\"_blank\" rel=\"noopener\">ico.org.uk/make-a-complaint</a>, +44 303 123 1113.</p>"),
]


def head(lang, title, desc, url, alt=None, noindex=False):
    e = html.escape
    links = ""
    if alt:
        links = "".join(f'<link rel="alternate" hreflang="{l}" href="{BASE}{p}">' for l, p in alt)
    robots = '<meta name="robots" content="noindex">' if noindex else ""
    canon = f'<link rel="canonical" href="{BASE}{url}">' if url else ""
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
{robots}{canon}{links}
<meta name="theme-color" content="#05060c">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&family=Inter:wght@400;600;700&family=JetBrains+Mono:wght@400&display=swap" rel="stylesheet">
<style>{CSS}{EXTRA_CSS}</style>
</head>
<body>
<header><div class="wrap hd">
  <a class="brand" href="{'/fr/' if lang == 'fr' else '/'}"><svg width="22" height="22" viewBox="0 0 24 24" aria-hidden="true"><path d="M13 2 4 14h6l-1 8 9-12h-6z" fill="none" stroke="#22d3ee" stroke-width="1.9" stroke-linejoin="round"/></svg><b>H7K3R</b><span>SYSTEMS</span></a>
</div></header>
<main>
"""


FOOT = """</main>
<footer><div class="wrap">H7K3R Systems · Croydon &amp; Kingston upon Thames · <a href="{home}">h7k3r.com</a></div></footer>
</body>
</html>
"""


def privacy(lang, sections, updated, title, h1, desc, upd_label, url):
    alt = [("en", "/privacy/"), ("fr", "/fr/privacy/"), ("x-default", "/privacy/")]
    body = "".join(f"<h2>{html.escape(t)}</h2>{b}" for t, b in sections)
    return (head(lang, title, desc, url, alt)
            + f'<div class="wrap legal"><div class="upd">{upd_label} {updated}</div><h1>{h1}</h1>{body}</div>\n'
            + FOOT.format(home="/fr/" if lang == "fr" else "/"))


def not_found():
    return (head("en", "Page not found | H7K3R Systems", "This page doesn't exist.", None, noindex=True)
            + """<div class="wrap nf">
  <div class="code">404</div>
  <h1>This page doesn't exist.</h1>
  <p class="lead">The link may be old or mistyped. Here's where you can go instead.</p>
  <p class="lead" lang="fr">Cette page n'existe pas. <a href="/fr/">Version française du site</a></p>
  <div class="links">
    <a class="btn btn-p" href="/">Go to the homepage</a>
    <a class="btn btn-g" href="/repair/croydon/">Repair in Croydon</a>
    <a class="btn btn-g" href="/repair/kingston/">Repair in Kingston</a>
    <a class="btn btn-g" href="/data-recovery/">Data recovery</a>
  </div>
</div>
""" + FOOT.format(home="/"))


if __name__ == "__main__":
    out = {
        "privacy/index.html": privacy("en-GB", PRIVACY_EN, UPDATED_EN, "Privacy notice | H7K3R Systems", "Privacy notice",
                                      "How H7K3R Systems uses the details you give us and the data on your device.", "Updated", "/privacy/"),
        "fr/privacy/index.html": privacy("fr", PRIVACY_FR, UPDATED_FR, "Politique de confidentialité | H7K3R Systems",
                                         "Politique de confidentialité",
                                         "Comment H7K3R Systems utilise vos coordonnées et les données de votre appareil.", "Mise à jour :", "/fr/privacy/"),
        "404.html": not_found(),
    }
    for rel, text in out.items():
        p = ROOT / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
        print("wrote", rel)
