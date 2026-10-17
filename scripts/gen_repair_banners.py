#!/usr/bin/env python3
"""Wide full-bleed banner illustrations for the Repair card headers. 720x210.
Overwrites the square repair-device/cyber/lab tiles so background-size:cover fills cleanly."""
import os, math

HEAD = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 210" role="img" aria-label="{alt}">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0c1120"/><stop offset="1" stop-color="#06090f"/></linearGradient>
<radialGradient id="gl" cx="0.5" cy="0.3" r="0.75"><stop offset="0" stop-color="#22d3ee" stop-opacity="0.16"/><stop offset="1" stop-color="#22d3ee" stop-opacity="0"/></radialGradient>
<linearGradient id="ink" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#7defe6"/><stop offset="0.5" stop-color="#22d3ee"/><stop offset="1" stop-color="#8b74ff"/></linearGradient>
</defs>
<rect width="720" height="210" fill="url(#bg)"/>
<g stroke="#5a7bb0" stroke-opacity="0.08" stroke-width="1"><path d="M0 52H720M0 105H720M0 158H720M90 0V210M180 0V210M270 0V210M360 0V210M450 0V210M540 0V210M630 0V210"/></g>
<rect width="720" height="210" fill="url(#gl)"/>
<g fill="none" stroke="url(#ink)" stroke-linecap="round" stroke-linejoin="round">
'''
FOOT = '''</g>
<text x="20" y="196" fill="#9aa6c4" fill-opacity="0.38" font-family="'JetBrains Mono',monospace" font-size="11" letter-spacing="4">H7K3R</text>
<text x="700" y="196" text-anchor="end" fill="#22d3ee" fill-opacity="0.5" font-family="'JetBrains Mono',monospace" font-size="11" letter-spacing="2">{tag}</text>
</svg>
'''
def M(d,w=3): return '<path stroke-width="%s" d="%s"/>'%(w,d)
def D(d,o=0.6,w=1.5): return '<path stroke-width="%s" stroke-opacity="%s" d="%s"/>'%(w,o,d)
def R(x,y,w,h,rx=0,sw=3): return '<rect stroke-width="%s" x="%s" y="%s" width="%s" height="%s" rx="%s"/>'%(sw,x,y,w,h,rx)
def C(cx,cy,r,sw=2.4,o=1): return '<circle stroke-width="%s" stroke-opacity="%s" cx="%s" cy="%s" r="%s"/>'%(sw,o,cx,cy,r)
def dot(cx,cy,r=2.6): return '<circle fill="url(#ink)" stroke="none" cx="%s" cy="%s" r="%s"/>'%(cx,cy,r)

B={}

# DEVICE REPAIR — phone (left) + crossed screwdriver & spanner (centre) + laptop (right)
B["repair-device"]=("Device repair — phone, tools and laptop","REPAIR","".join([
 # phone
 R(86,54,86,108,12), D("M104 54 l50 0"), C(129,150,3,2), R(96,66,66,78,5)+'',
 D("M96 66 l66 0",0.4),
 # crossed tools centre
 M("M300 150 L372 78",3.2),                                   # screwdriver shaft
 M("M290 160 l22 22 l12 -12 l-22 -22 z",2.8),                 # handle
 M("M372 78 l10 -10 l8 8 l-10 10 z",2.6),                     # tip
 M("M300 78 L366 144",3.2),                                   # spanner bar
 M("M292 70 a14 14 0 1 0 2 -2 l-10 -10 l10 -2 l2 10 z",2.6),  # spanner open head
 dot(333,111),
 # laptop right
 R(520,66,128,80,5), D("M536 80 l96 0",0.5), D("M536 92 l70 0",0.35),
 M("M502 150 l164 0 l-16 16 l-132 0 z",3),                    # keyboard wedge
 D("M548 158 l72 0",0.5),
]))

# CYBER — big shield+lock (left) + scan mesh / waves (right)
B["cyber"]=("Personal cyber security — shield and network sweep","REPAIR","".join([
 # shield
 M("M150 40 L236 70 L236 120 Q236 162 150 184 Q64 162 64 120 L64 70 Z",3.2),
 D("M150 52 L222 77 L222 118 Q222 152 150 170 Q78 152 78 118 L78 77 Z",0.5),
 # lock in shield
 M("M134 108 q0 -18 16 -18 q16 0 16 18",2.6),
 R(126,108,48,34,5), M("M150 120 l0 12",2.4),
 # scanning mesh right
 D("M330 60 L430 50",0.5),D("M330 60 L402 118",0.5),D("M430 50 L520 92",0.5),
 D("M402 118 L520 92",0.5),D("M402 118 L486 156",0.5),D("M520 92 L612 66",0.5),D("M486 156 L612 66",0.4),
 C(330,60,8,2.4),C(430,50,8,2.4),C(402,118,8,2.4),C(520,92,8,2.4),C(486,156,8,2.4),C(612,66,8,2.4),
 dot(330,60),dot(430,50),dot(402,118),dot(520,92),dot(486,156),dot(612,66),
 # radar sweep arc far right
 D("M648 150 a44 44 0 0 1 -44 -44",0.3,2),
]))

# LAB — microscope/scope (left) + HDD platter (centre) + NAND chip (right) on a bench
B["lab"]=("Laboratory data recovery — microscope, drive and chip","REPAIR","".join([
 M("M150 166 l420 0",2.4),                                    # bench line
 # microscope (left)
 C(150,70,24,3), C(150,70,13,1.6,0.6),                        # objective lens
 M("M166 86 l40 40",3),                                       # arm
 M("M198 118 l26 26 q12 12 0 24 q-12 12 -24 0 l-26 -26 z",3), # body
 M("M150 150 l52 0 q5 0 5 5 l0 9 l-62 0 l0 -9 q0 -5 5 -5 z",2.8), # stage/base
 # HDD platter (centre)
 C(360,98,52,3), C(360,98,15,2,0.7), C(360,98,4,2,0.8),
 M("M396 70 q22 20 10 52",2.6),                               # read-head arm
 dot(406,122),
 D("M360 46 a52 52 0 0 1 44 26",0.35,1.6),
 # NAND chip (right)
 R(520,74,96,56,6),
 D("M520 90 l96 0",0.4),D("M520 108 l96 0",0.4),
 *[ '<path stroke-width="2" d="M%d 130 l0 12"/>'%x for x in range(534,610,14) ],
 *[ '<path stroke-width="2" d="M%d 62 l0 12"/>'%x for x in range(534,610,14) ],
 M("M548 96 l10 9 18 -18",2.6),                               # check mark on chip
]))

os.makedirs("gear", exist_ok=True)
for name,(alt,tag,body) in B.items():
    open("gear/%s.svg"%name,"w").write(HEAD.format(alt=alt)+body+FOOT.format(tag=tag))
print("wrote wide banners:", ", ".join(sorted(B)))
