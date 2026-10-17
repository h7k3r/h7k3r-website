#!/usr/bin/env python3
"""Line-art banner illustrations for the 4 Consulting cards. 400x150."""
import os, math

HEAD = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 150" role="img" aria-label="{alt}">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0c1120"/><stop offset="1" stop-color="#06090f"/></linearGradient>
<radialGradient id="gl" cx="0.5" cy="0.28" r="0.7"><stop offset="0" stop-color="#22d3ee" stop-opacity="0.15"/><stop offset="1" stop-color="#22d3ee" stop-opacity="0"/></radialGradient>
<linearGradient id="ink" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#7defe6"/><stop offset="0.5" stop-color="#22d3ee"/><stop offset="1" stop-color="#8b74ff"/></linearGradient>
</defs>
<rect width="400" height="150" fill="url(#bg)"/>
<g stroke="#5a7bb0" stroke-opacity="0.09" stroke-width="1"><path d="M0 50H400M0 100H400M80 0V150M160 0V150M240 0V150M320 0V150"/></g>
<rect width="400" height="150" fill="url(#gl)"/>
<g fill="none" stroke="url(#ink)" stroke-linecap="round" stroke-linejoin="round">
'''
FOOT = '''</g>
<text x="14" y="138" fill="#9aa6c4" fill-opacity="0.4" font-family="'JetBrains Mono',monospace" font-size="9" letter-spacing="3">H7K3R</text>
<text x="386" y="138" text-anchor="end" fill="#22d3ee" fill-opacity="0.5" font-family="'JetBrains Mono',monospace" font-size="9" letter-spacing="2">{tag}</text>
</svg>
'''
def M(d,w=2.6): return '<path stroke-width="%s" d="%s"/>'%(w,d)
def D(d,o=0.6,w=1.4): return '<path stroke-width="%s" stroke-opacity="%s" d="%s"/>'%(w,o,d)
def R(x,y,w,h,rx=0,sw=2.4,extra=''): return '<rect stroke-width="%s" x="%s" y="%s" width="%s" height="%s" rx="%s" %s/>'%(sw,x,y,w,h,rx,extra)
def C(cx,cy,r,sw=2,o=1): return '<circle stroke-width="%s" stroke-opacity="%s" cx="%s" cy="%s" r="%s"/>'%(sw,o,cx,cy,r)
def dot(cx,cy,r=2.4): return '<circle fill="url(#ink)" stroke="none" cx="%s" cy="%s" r="%s"/>'%(cx,cy,r)

B={}

# Hardware Assembly & Sourcing — a fleet of towers + a mounting bracket / screwdriver
B["consult-assembly"]=("Hardware assembly and sourcing","ASSEMBLY · SOURCING","".join([
 R(60,44,42,70,4),  R(112,44,42,70,4),  R(164,44,42,70,4),           # three identical towers (fleet)
 D("M68 56 L94 56"), D("M120 56 L146 56"), D("M172 56 L198 56"),      # top panels
 C(90,66,2.4,1.8), C(142,66,2.4,1.8), C(194,66,2.4,1.8),             # power buttons
 D("M68 100 L94 100",0.5), D("M120 100 L146 100",0.5), D("M172 100 L198 100",0.5),
 # screwdriver / tool over the right
 M("M250 56 L300 106",2.6), M("M296 94 L312 110 L306 116 L290 100 Z",2.2),
 R(244,48,14,14,2,2.2),                                               # screw head
 dot(252,55),
 # sourcing arrows into the fleet
 D("M330 60 Q300 50 210 62",0.45), D("M330 60 L322 56 M330 60 L324 66",0.45),
]))

# Node Deployment & OS Imaging — a master disk imaging out to multiple screens
B["consult-imaging"]=("Node deployment and OS imaging","DEPLOY · IMAGING","".join([
 R(50,52,56,54,4),                                                    # master image source
 D("M58 64 L98 64",0.6), D("M58 74 L98 74",0.5), D("M58 84 L90 84",0.5),  # OS layers
 C(78,96,5,2),  M("M75 96 L80 96 M78 93 L78 99"),                     # disk core
 # fan-out lines to 3 target nodes
 D("M106 79 Q150 60 196 56",0.5), D("M106 79 Q150 79 196 86",0.5), D("M106 79 Q150 98 196 116",0.5),
 R(196,44,46,34,3), R(196,74,46,34,3), R(196,104,46,34,3),           # target screens
 dot(219,61),dot(219,91),dot(219,121),
 # progress ticks far right
 M("M300 62 L312 74 L336 48",2.6), C(318,70,26,1.6,0.5),
]))

# Network Infrastructure — topology mesh + rack
B["consult-network"]=("Network infrastructure design","NETWORK · ZERO-TRUST","".join([
 # rack on the left
 R(52,42,46,72,4), D("M60 54 L90 54",0.6), D("M60 66 L90 66",0.6), D("M60 78 L90 78",0.6), D("M60 90 L90 90",0.6),
 C(86,60,1.8,1.6),C(86,72,1.8,1.6),C(86,84,1.8,1.6),
 # mesh topology
 D("M150 50 L214 44",0.5),D("M150 50 L198 92",0.5),D("M214 44 L270 70",0.5),
 D("M198 92 L270 70",0.5),D("M198 92 L252 116",0.5),D("M270 70 L326 52",0.5),D("M252 116 L326 52",0.4),
 C(150,50,7,2.2),C(214,44,7,2.2),C(198,92,7,2.2),C(270,70,7,2.2),C(252,116,7,2.2),C(326,52,7,2.2),
 dot(150,50),dot(214,44),dot(198,92),dot(270,70),dot(252,116),dot(326,52),
]))

# Cyber-Security Auditing — shield + magnifier scanning
B["consult-audit"]=("Cyber-security auditing and pen-testing","AUDIT · PEN-TEST","".join([
 M("M150 36 L204 52 L204 92 Q204 118 150 132 Q96 118 96 92 L96 52 Z",2.8),  # shield
 M("M128 82 L144 100 L176 60",2.6),                                   # check
 # magnifier scanning over it
 C(276,66,24,2.6), M("M294 84 L320 112",3),
 D("M266 60 L286 60 M276 50 L276 70",0.6),                            # crosshair in lens
 dot(276,66,1.6),
 # scan lines
 D("M240 100 L330 100",0.3),D("M240 108 L330 108",0.25),
]))

os.makedirs("gear", exist_ok=True)
for name,(alt,tag,body) in B.items():
    open("gear/%s.svg"%name,"w").write(HEAD.format(alt=alt)+body+FOOT.format(tag=tag))
print("wrote", ", ".join(sorted(B)))
