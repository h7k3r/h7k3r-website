#!/usr/bin/env python3
"""Accurate per-tier PC sketches for the Hardware build cards. 400x230."""
import os, math

HEAD = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 230" role="img" aria-label="{alt}">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0c1120"/><stop offset="1" stop-color="#06090f"/></linearGradient>
<radialGradient id="gl" cx="0.5" cy="0.24" r="0.64"><stop offset="0" stop-color="#22d3ee" stop-opacity="0.16"/><stop offset="1" stop-color="#22d3ee" stop-opacity="0"/></radialGradient>
<linearGradient id="ink" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#7defe6"/><stop offset="0.5" stop-color="#22d3ee"/><stop offset="1" stop-color="#8b74ff"/></linearGradient>
</defs>
<rect width="400" height="230" fill="url(#bg)"/>
<g stroke="#5a7bb0" stroke-opacity="0.09" stroke-width="1"><path d="M0 46H400M0 92H400M0 138H400M0 184H400M54 0V230M108 0V230M162 0V230M216 0V230M270 0V230M324 0V230"/></g>
<rect width="400" height="230" fill="url(#gl)"/>
<g fill="none" stroke="url(#ink)" stroke-linecap="round" stroke-linejoin="round">
'''
FOOT = '''</g>
<text x="16" y="214" fill="#9aa6c4" fill-opacity="0.4" font-family="'JetBrains Mono',monospace" font-size="10" letter-spacing="3">H7K3R</text>
<text x="384" y="214" text-anchor="end" fill="#22d3ee" fill-opacity="0.55" font-family="'JetBrains Mono',monospace" font-size="10" letter-spacing="2">{tag}</text>
</svg>
'''
def M(d,w=3): return '<path stroke-width="%s" d="%s"/>'%(w,d)
def D(d,o=0.6): return '<path stroke-width="1.5" stroke-opacity="%s" d="%s"/>'%(o,d)
def R(x,y,w,h,rx=0,sw=3,extra=''):
    return '<rect stroke-width="%s" x="%s" y="%s" width="%s" height="%s" rx="%s" %s/>'%(sw,x,y,w,h,rx,extra)
def circ(cx,cy,r,sw=2,o=1):
    return '<circle stroke-width="%s" stroke-opacity="%s" cx="%s" cy="%s" r="%s"/>'%(sw,o,cx,cy,r)
def fan(cx,cy,r,o=1):
    s=circ(cx,cy,r,2.2,o)+circ(cx,cy,max(2.4,r*0.26),1.6,0.7*o)
    for a in range(0,360,60):
        x2=cx+r*0.8*math.cos(math.radians(a)); y2=cy+r*0.8*math.sin(math.radians(a))
        s+='<path stroke-width="1.3" stroke-opacity="%s" d="M%.0f %.0f Q%.0f %.0f %.0f %.0f"/>'%(0.5*o,cx,cy,cx+r*0.42*math.cos(math.radians(a-30)),cy+r*0.42*math.sin(math.radians(a-30)),x2,y2)
    return s
def mesh(x,y,w,h):
    s=''
    for yy in range(int(y)+4,int(y+h),8):
        for xx in range(int(x)+4,int(x+w),8):
            s+='<circle fill="url(#ink)" stroke="none" opacity="0.5" cx="%d" cy="%d" r="1"/>'%(xx,yy)
    return s

B={}

# VENO_KILLER £449 — stealth solid-panel micro tower (no window)
B["build-veno"]=("VENO_KILLER stealth case sketch","FROM £449","".join([
 R(166,54,68,122,8),                       # solid tower, clean
 D("M166 70 L234 70"),                      # top seam
 circ(224,62,2.5,2),                        # power button
 D("M176 160 L224 160"), D("M176 166 L224 166"), D("M176 172 L224 172"),  # discreet bottom vents
 D("M176 64 L176 166",0.4),                 # faint front-panel edge
]))

# PROJECT_P £850 — gaming rig, tempered-glass panel + RGB fans visible
B["build-projectp"]=("PROJECT_P RGB gaming rig sketch","FROM £850","".join([
 R(158,48,96,132,8),                        # tower
 R(170,60,72,108,4,2),                      # glass side panel
 D("M176 164 L236 72",0.35),                # glass reflection
 fan(190,80,10), fan(190,104,10), fan(190,128,10),  # RGB intake fans
 R(206,70,34,8,1,2.2), R(206,82,34,8,1,2.2),        # RAM
 R(176,150,60,16,2),                        # GPU
 circ(220,158,4,1.6,0.7),
]))

# XPROTO_STEALTH £1,850 — XTIA Xproto upright OPEN frame (stands vertically, exposed)
B["build-xproto"]=("XPROTO (XTIA Xproto) open upright frame sketch","FROM £1,850","".join([
 M("M150 176 L250 176"),                    # base foot
 M("M160 176 L160 60 M240 176 L240 60"),    # two vertical rails
 M("M160 60 L240 60"),                      # top bar
 R(172,74,42,70,2,2.6),                     # vertical motherboard
 R(182,88,22,22,1,2.2),                     # CPU cooler block
 D("M172 120 L214 120"),                    # mobo detail
 M("M222 78 L234 78 L234 150 L222 150 Z"),  # vertical GPU
 fan(228,96,5,0.9), fan(228,118,5,0.9),
 R(170,150,70,20,2,2.4),                    # PSU at base
 D("M176 160 L204 160"),
]))

# APEX_NODE £2,100 — high-airflow esports (mesh front + fan stack)
B["build-apex"]=("APEX_NODE high-airflow tower sketch","FROM £2,100","".join([
 R(150,46,100,134,8),                       # tower
 R(156,52,20,122,2,2),                      # mesh front panel
 mesh(156,52,20,122),
 fan(186,70,10), fan(186,96,10), fan(186,122,10),  # fan stack behind mesh
 R(206,64,38,8,1,2.2), R(206,76,38,8,1,2.2),       # RAM
 R(182,150,62,20,2),                        # GPU
 fan(216,160,7,0.8),
]))

# TRIDENT APEX £8,610 — flagship 4-GPU workstation
B["build-trident"]=("TRIDENT APEX 4-GPU flagship sketch","FLAGSHIP · 4x GPU","".join([
 R(146,40,108,150,8),                       # big chassis
 R(154,48,92,20,2,2),                       # top radiator
 fan(172,58,6), fan(200,58,6), fan(228,58,6),
 R(160,80,26,14,1,2.2),                     # CPU/VRM block
 R(192,80,50,6,1,2), R(192,90,50,6,1,2),    # RAM bank
 # four stacked GPUs
 R(156,104,86,15,2,2.4), R(156,122,86,15,2,2.4), R(156,140,86,15,2,2.4), R(156,158,86,15,2,2.4),
 circ(166,111,2.4,1.4,0.7), circ(166,129,2.4,1.4,0.7), circ(166,147,2.4,1.4,0.7), circ(166,165,2.4,1.4,0.7),
 D("M236 104 L236 173",0.4),
]))

os.makedirs("gear", exist_ok=True)
for name,(alt,tag,body) in B.items():
    open("gear/%s.svg"%name,"w").write(HEAD.format(alt=alt)+body+FOOT.format(tag=tag))
print("wrote", ", ".join(sorted(B)))
