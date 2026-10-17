#!/usr/bin/env python3
"""Repair card header banners. 1200x240 canvas, artwork as a tight centred emblem
(x 440-780, y 50-192) so background-size:cover only ever crops empty grid —
at phone width (~2.2:1), half-width cards (~3.7:1) and the full-width lab card (~6:1)."""
import os

HEAD = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 240" preserveAspectRatio="xMidYMid slice" role="img" aria-label="{alt}">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0c1120"/><stop offset="1" stop-color="#06090f"/></linearGradient>
<radialGradient id="gl" cx="0.5" cy="0.52" r="0.32"><stop offset="0" stop-color="{glow}" stop-opacity="0.22"/><stop offset="1" stop-color="{glow}" stop-opacity="0"/></radialGradient>
<linearGradient id="ink" gradientUnits="userSpaceOnUse" x1="440" y1="50" x2="780" y2="192"><stop offset="0" stop-color="#7defe6"/><stop offset="0.5" stop-color="#22d3ee"/><stop offset="1" stop-color="#8b74ff"/></linearGradient>
<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#5a7bb0" stroke-opacity="0.08" stroke-width="1"/></pattern>
</defs>
<rect width="1200" height="240" fill="url(#bg)"/>
<rect width="1200" height="240" fill="url(#grid)"/>
<rect width="1200" height="240" fill="url(#gl)"/>
<g fill="none" stroke="url(#ink)" stroke-linecap="round" stroke-linejoin="round">
'''
FOOT = '</g>\n</svg>\n'
def M(d,w=3): return '<path stroke-width="%s" d="%s"/>'%(w,d)
def D(d,o=0.55,w=1.6): return '<path stroke-width="%s" stroke-opacity="%s" d="%s"/>'%(w,o,d)
def R(x,y,w,h,rx=0,sw=3,o=1): return '<rect stroke-width="%s" stroke-opacity="%s" x="%s" y="%s" width="%s" height="%s" rx="%s"/>'%(sw,o,x,y,w,h,rx)
def C(cx,cy,r,sw=2.6,o=1): return '<circle stroke-width="%s" stroke-opacity="%s" cx="%s" cy="%s" r="%s"/>'%(sw,o,cx,cy,r)
def dot(cx,cy,r=3): return '<circle fill="url(#ink)" stroke="none" cx="%s" cy="%s" r="%s"/>'%(cx,cy,r)

B = {}

# DEVICE REPAIR — phone · crossed driver & spanner · laptop, centred on x=600
B["repair-device"] = ("Device repair: phone, tools and laptop", "#22d3ee", "".join([
    # phone
    R(446,60,60,114,11), R(454,74,44,84,3,1.6,0.5), M("M464 67 l24 0",2), C(476,166,2.6,2),
    # crossed tools
    M("M568 156 L630 94",3.2), M("M560 164 l16 16 l11 -11 l-16 -16 z",2.8), M("M630 94 l8 -8 l6 6 l-8 8 z",2.6),
    M("M582 104 L632 154",3.2), C(572,94,12,2.8), M("M566 88 l8 8",2.4), C(636,158,6,2.4),
    dot(600,126,3.4),
    # laptop
    R(686,74,92,60,5), D("M700 88 l64 0"), D("M700 100 l44 0",0.35),
    M("M670 142 l124 0 l-12 15 l-100 0 z",3), D("M712 150 l40 0",0.5),
]))

# CYBER — shield + lock, flanked by mirrored node meshes
B["cyber"] = ("Personal cyber security: shield with network sweep", "#38bdf8", "".join([
    M("M600 48 L658 68 L658 118 Q658 168 600 192 Q542 168 542 118 L542 68 Z",3.2),
    D("M600 62 L646 78 L646 117 Q646 157 600 177 Q554 157 554 117 L554 78 Z",0.45),
    M("M586 118 q0 -17 14 -17 q14 0 14 17",2.6), R(577,118,46,32,5,2.8), M("M600 128 l0 11",2.6),
    # left mesh
    D("M468 88 L506 126"), D("M452 150 L506 126"), D("M468 88 L452 150",0.35), D("M506 126 L542 118",0.3),
    C(468,88,7), C(452,150,7), C(506,126,7), dot(468,88), dot(452,150), dot(506,126),
    # right mesh
    D("M732 88 L694 126"), D("M748 150 L694 126"), D("M732 88 L748 150",0.35), D("M694 126 L658 118",0.3),
    C(732,88,7), C(748,150,7), C(694,126,7), dot(732,88), dot(748,150), dot(694,126),
]))

# LAB — microscope · hard-drive platter · NAND chip on one bench, centred
B["lab"] = ("Laboratory data recovery: microscope, drive platter and memory chip", "#f87171", "".join([
    M("M436 182 L770 182",2.4),
    # microscope
    C(470,80,18,3), C(470,80,8,1.6,0.6), M("M482 93 l26 28",3),
    M("M502 115 l18 18 q8 8 0 16 q-8 8 -16 0 l-18 -18 z",2.8),
    R(450,166,70,10,3,2.6), M("M486 166 l0 -14",2.6),
    # HDD platter
    C(600,124,44,3), C(600,124,13,2,0.7), dot(600,124,3.4),
    M("M638 92 q18 18 2 46",2.6), dot(640,138,3), D("M600 80 a44 44 0 0 1 36 18",0.3),
    # NAND chip
    R(682,98,78,54,6), D("M682 114 l78 0",0.35), D("M682 136 l78 0",0.35),
    *['<path stroke-width="2" d="M%d 152 l0 10"/>' % x for x in range(694, 752, 13)],
    *['<path stroke-width="2" d="M%d 88 l0 10"/>' % x for x in range(694, 752, 13)],
    M("M706 124 l9 9 l18 -18",2.8),
]))

os.makedirs("gear", exist_ok=True)
for name, (alt, glow, body) in B.items():
    open("gear/%s.svg" % name, "w").write(HEAD.format(alt=alt, glow=glow) + body + FOOT)
print("wrote centred banners:", ", ".join(sorted(B)))
