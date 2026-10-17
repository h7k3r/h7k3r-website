#!/usr/bin/env python3
"""Generate detailed hand-drawn-style outline illustrations for h7k3r.com gear.
Cyan->violet gradient line art on a dark branded tile. viewBox 400x230."""
import os

HEAD = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 230" role="img" aria-label="{alt}">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0c1120"/><stop offset="1" stop-color="#06090f"/></linearGradient>
<radialGradient id="gl" cx="0.5" cy="0.24" r="0.64"><stop offset="0" stop-color="#22d3ee" stop-opacity="0.18"/><stop offset="1" stop-color="#22d3ee" stop-opacity="0"/></radialGradient>
<linearGradient id="ink" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#7defe6"/><stop offset="0.5" stop-color="#22d3ee"/><stop offset="1" stop-color="#8b74ff"/></linearGradient>
</defs>
<rect width="400" height="230" fill="url(#bg)"/>
<g stroke="#5a7bb0" stroke-opacity="0.09" stroke-width="1"><path d="M0 46H400M0 92H400M0 138H400M0 184H400M54 0V230M108 0V230M162 0V230M216 0V230M270 0V230M324 0V230"/></g>
<rect width="400" height="230" fill="url(#gl)"/>
<g fill="none" stroke="url(#ink)" stroke-linecap="round" stroke-linejoin="round">
'''
FOOT = '''</g>
<text x="16" y="214" fill="#9aa6c4" fill-opacity="0.4" font-family="'JetBrains Mono',monospace" font-size="10" letter-spacing="3">H7K3R</text>
<text x="384" y="214" text-anchor="end" fill="#22d3ee" fill-opacity="0.5" font-family="'JetBrains Mono',monospace" font-size="10" letter-spacing="2">{tag}</text>
</svg>
'''

def M(d): return '<path stroke-width="3" d="%s"/>' % d          # main line
def D(d): return '<path stroke-width="1.6" stroke-opacity="0.65" d="%s"/>' % d  # detail
def DD(d): return '<path stroke-width="1.6" stroke-opacity="0.55" stroke-dasharray="2 6" d="%s"/>' % d

ICONS = {}

# ---- HOODIE ----
ICONS["hoodie"] = ("Plain hoodie outline illustration", "GEAR", "".join([
 M("M160 92 q-20 10 -28 34 q-3 9 2 12 l18 8 q4 2 5 -3 l6 -20"),            # left sleeve
 M("M240 92 q20 10 28 34 q3 9 -2 12 l-18 8 q-4 2 -5 -3 l-6 -20"),          # right sleeve
 M("M163 90 q37 26 74 0 l0 2 q6 50 2 92 q-39 10 -78 0 q-4 -42 2 -94 z"),   # body
 M("M163 90 q-6 -22 18 -30 q19 7 38 0 q24 8 18 30 q-37 26 -74 0 z"),       # hood
 D("M181 60 q19 7 38 0"),                                                   # hood inner
 M("M192 64 q8 6 16 0 l-2 26 q-6 4 -12 0 z"),                               # hood opening
 D("M190 92 q10 6 20 0"),                                                   # neck seam
 M("M184 128 q16 10 32 0 l-4 30 q-12 7 -24 0 z"),                          # kangaroo pocket
 M("M186 70 l-3 40"), M("M214 70 l3 40"),                                   # drawstrings
 D("M181 112 l-6 2"), D("M219 112 l6 2"),
 DD("M150 176 q50 10 100 0"),                                               # hem rib
]))

# ---- PARKA / JACKET ----
ICONS["parka"] = ("Faraday parka jacket outline illustration", "GEAR", "".join([
 M("M158 94 q-18 8 -24 40 q-2 8 3 10 l16 6 q4 1 5 -3 l6 -22"),             # left sleeve
 M("M242 94 q18 8 24 40 q2 8 -3 10 l-16 6 q-4 1 -5 -3 l-6 -22"),           # right sleeve
 M("M162 92 q10 -22 38 -22 q28 0 38 22 l-6 96 q-32 9 -64 0 z"),            # body (long)
 M("M184 72 q16 12 32 0 l-6 14 q-10 7 -20 0 z"),                           # collar
 M("M200 86 l0 92"),                                                        # center zip
 DD("M200 92 l0 84"),
 M("M196 92 l8 0 l-2 10 l-4 0 z"),                                          # zip pull
 M("M170 120 l20 0 l0 20 l-20 0 z"), M("M210 120 l20 0 l0 20 l-20 0 z"),   # pockets
 D("M170 124 l20 0"), D("M210 124 l20 0"),                                  # pocket flaps
 D("M150 148 l8 2"), D("M250 148 l-8 2"),                                   # cuffs
]))

# ---- FARADAY POUCH ----
ICONS["pouch"] = ("Faraday signal-blocking pouch outline illustration", "GEAR", "".join([
 M("M150 96 q0 -10 10 -10 l80 0 q10 0 10 10 l0 60 q0 10 -10 10 l-80 0 q-10 0 -10 -10 z"),  # body
 M("M150 108 q50 -26 100 0"),                                               # top flap seam
 D("M156 120 l88 0"),                                                        # fold line
 DD("M158 100 q42 -18 84 0"),                                                # stitching
 M("M186 126 l28 0 l0 26 l-28 0 z"),                                         # phone inside
 D("M186 148 l28 0"),
 M("M258 74 a16 16 0 0 1 24 0"), M("M264 68 a24 24 0 0 1 34 0"),            # signal waves
 M("M252 62 l46 30", ),                                                      # block slash (violet via ink)
]))

# ---- USB DATA BLOCKER ----
ICONS["usb-blocker"] = ("USB data blocker outline illustration", "GEAR", "".join([
 M("M150 92 l66 0 q8 0 8 8 l0 30 q0 8 -8 8 l-66 0 z"),                      # housing
 M("M134 100 l16 0 l0 30 l-16 0 z"),                                        # metal tip
 D("M138 108 l8 0 l0 6 l-8 0 z"), D("M138 120 l8 0 l0 6 l-8 0 z"),          # contacts
 M("M224 104 l18 0 q6 0 6 6 l0 18 q0 6 -6 6 l-18 0"),                       # cable boot
 M("M260 76 l24 9 l0 16 q0 22 -24 30 q-24 -8 -24 -30 l0 -16 z"),           # shield
 M("M250 102 l8 9 14 -18"),                                                 # check
]))

# ---- FARADAY SLEEVE ----
ICONS["sleeve"] = ("Faraday laptop sleeve outline illustration", "GEAR", "".join([
 M("M150 92 q0 -6 6 -6 l108 0 q6 0 6 6 l0 72 q0 6 -6 6 l-108 0 q-6 0 -6 -6 z"),  # sleeve
 DD("M150 104 l120 0"),                                                     # top zip
 M("M262 98 l8 0 l-2 10 l-4 0 z"),                                          # zip pull
 M("M172 70 q0 -4 4 -4 l78 0 q4 0 4 4 l0 30 l-86 0 z"),                     # laptop inserting
 D("M176 70 l74 0"),
 DD("M158 150 l104 0"),                                                     # bottom stitch
]))

# ---- SIGNAL-PROOF HAT (cap) ----
ICONS["hat"] = ("Signal-proof cap outline illustration", "GEAR", "".join([
 M("M156 124 q0 -50 46 -50 q44 0 44 48"),                                   # crown
 M("M156 124 q-6 2 -4 8 q2 6 50 6 q48 0 46 -8"),                            # band
 M("M244 122 q28 0 30 14 q1 8 -14 8 l-20 0 z"),                             # brim
 D("M180 80 q0 40 0 42"), D("M202 74 l0 50"), D("M224 80 q0 38 0 40"),      # panel seams
 M("M202 72 q4 -2 4 2"),                                                     # top button
 M("M260 70 a16 16 0 0 1 24 0"), M("M266 64 a24 24 0 0 1 34 0"),            # signal
 M("M254 58 l46 30"),                                                        # slash
]))

# ---- STEALTH BACKPACK ----
ICONS["backpack"] = ("Stealth backpack outline illustration", "GEAR", "".join([
 M("M166 86 q0 -16 34 -16 q34 0 34 16 l0 86 q0 8 -8 8 l-52 0 q-8 0 -8 -8 z"),  # body
 M("M188 72 q12 -16 24 0"),                                                 # top handle
 M("M176 120 q24 -10 48 0 l0 36 q-24 8 -48 0 z"),                           # front pocket
 D("M176 138 q24 8 48 0"),                                                   # pocket zip
 M("M233 132 l6 2"),                                                         # pocket pull
 M("M170 94 q-16 26 -2 70"), M("M230 94 q16 26 2 70"),                      # straps
 DD("M200 90 l0 78"),                                                        # center seam
]))

# ---- PRECISION BIT SET ----
ICONS["bits"] = ("Precision bit set outline illustration", "GEAR", "".join([
 M("M150 92 q-6 0 -6 8 l0 14 q0 8 6 8 l34 0 l0 -30 z"),                     # driver handle
 D("M152 100 l0 20"), D("M160 100 l0 20"), D("M168 100 l0 20"),             # grip ridges
 M("M184 100 l28 0 l0 10 l-28 0 z"),                                        # shaft
 M("M212 98 l10 7 l-10 7 z"),                                               # magnetic tip
 M("M236 90 q-4 0 -4 4 l0 44 q0 4 4 4 l34 0 q4 0 4 -4 l0 -44 q0 -4 -4 -4 z"),  # bit tray
 D("M232 108 l42 0"), D("M232 124 l42 0"),
 M("M242 98 l0 6"), M("M253 98 l-3 6 l6 0 z"), M("M264 98 l0 6 m-3 -3 l6 0"),  # bit tips (slot/tri/plus)
]))

# ---- USB SURGE TESTER (restricted) ----
ICONS["usb-tester"] = ("USB surge tester outline illustration", "RESTRICTED", "".join([
 M("M158 96 l76 0 q6 0 6 6 l0 26 q0 6 -6 6 l-76 0 z"),                      # body
 M("M142 104 l16 0 l0 22 l-16 0 z"), M("M234 104 l16 0 l0 22 l-16 0 z"),    # two USB ends
 M("M170 104 l22 0 l0 20 l-22 0 z"),                                        # readout
 D("M176 114 l10 0"),
 M("M210 100 l-8 15 l10 0 l-8 15"),                                         # lightning
]))

# ---- RED-TEAM ASSESSMENT CABLE (restricted) ----
ICONS["cable"] = ("Red-team assessment cable outline illustration", "RESTRICTED", "".join([
 M("M146 108 l14 0 l0 22 l-14 0 z"),                                        # USB-A
 M("M160 114 l12 0 l0 10 l-12 0 z"),                                        # neck
 M("M172 119 q44 0 60 -24 q16 -24 48 -20"),                                 # cable curve
 M("M278 70 l16 10 l-10 16 l-16 -10 z"),                                    # USB-C end
 M("M212 96 q-4 0 -4 4 l0 14 q0 4 4 4 l22 0 q4 0 4 -4 l0 -14 q0 -4 -4 -4 z"),  # inline module
 D("M216 104 l14 0"), D("M216 110 l14 0"),
]))

# ---- REPAIR: DEVICE ----
ICONS["repair-device"] = ("Device repair outline illustration", "REPAIR", "".join([
 M("M156 70 q0 -6 6 -6 l44 0 q6 0 6 6 l0 100 q0 6 -6 6 l-44 0 q-6 0 -6 -6 z"),  # phone
 D("M174 70 l20 0"), M("M182 162 l4 0"),                                     # speaker / home
 M("M232 92 l20 -8 q4 5 0 9 l-12 12 l18 26 q4 6 -3 10 q-6 4 -10 -2 l-18 -26 l-12 8 q-5 -4 -2 -9 z"),  # wrench/driver
]))

# ---- REPAIR: CYBER ----
ICONS["cyber"] = ("Cyber security outline illustration", "REPAIR", "".join([
 M("M200 62 l46 17 l0 30 q0 46 -46 61 q-46 -15 -46 -61 l0 -30 z"),          # shield
 D("M200 70 l38 14 l0 26 q0 38 -38 51 q-38 -13 -38 -51 l0 -26 z"),          # inner shield
 M("M188 108 q0 -12 12 -12 q12 0 12 12 l-4 0 q0 -8 -8 -8 q-8 0 -8 8 z"),    # lock shackle
 M("M184 108 l32 0 q3 0 3 3 l0 22 q0 3 -3 3 l-32 0 q-3 0 -3 -3 l0 -22 q0 -3 3 -3 z"),  # lock body
 M("M200 118 l0 10"),
]))

# ---- REPAIR: LAB ----
ICONS["lab"] = ("Laboratory data recovery outline illustration", "REPAIR", "".join([
 M("M184 72 a20 20 0 1 0 0.1 0 z"),                                         # scope lens
 D("M184 80 a12 12 0 1 0 0.1 0 z"),
 M("M198 86 l34 34"),                                                        # arm
 M("M226 112 l20 20 q10 10 0 20 q-10 10 -20 0 l-20 -20 z"),                 # body
 M("M172 150 l44 0 q4 0 4 4 l0 6 l-52 0 l0 -6 q0 -4 4 -4 z"),               # base
 M("M160 170 l72 0"),                                                        # bench
]))

os.makedirs("gear", exist_ok=True)
for name, (alt, tag, body) in ICONS.items():
    svg = HEAD.format(alt=alt) + body + FOOT.format(tag=tag)
    open("gear/%s.svg" % name, "w").write(svg)
print("wrote", len(ICONS), "illustrations:", ", ".join(sorted(ICONS)))
