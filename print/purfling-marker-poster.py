"""Build the A4 purfling marker poster for in-person sales.

Needs Pillow and cairosvg, plus the Playfair Display and Inter fonts
installed. Uses the product images from src/assets/shop, so re-run it
after changing those. Writes the PDF next to this file.

    python print/purfling-marker-poster.py
"""
import base64, io, pathlib, cairosvg
from PIL import Image
HERE=pathlib.Path(__file__).parent
A=str(HERE.parent)+'/'
S=A+'src/assets/shop/'
def uri(path, crop=None, maxw=1600, fmt='JPEG'):
    im=Image.open(path).convert('RGB')
    if crop: im=im.crop(crop)
    if im.width>maxw: im=im.resize((maxw, round(im.height*maxw/im.width)))
    b=io.BytesIO(); im.save(b,fmt,**({'quality':90} if fmt=='JPEG' else {}))
    return f'data:image/{fmt.lower()};base64,'+base64.b64encode(b.getvalue()).decode(), im.size
logo,(lw,lh)=uri(A+'public/assets/images/chellilogo.png',crop=(60,60,2296,820))
case,(cw,ch)=uri(S+'purfling-marker-case.jpg')
adj,(aw,ah)=uri(S+'purfling-marker-adjustments.png',fmt='PNG')
b1,(bw,bh)=uri(S+'purfling-marker-blades-supplied.png',fmt='PNG')
b2,_=uri(S+'purfling-marker-blades-purfling.png',fmt='PNG')

W,H=2100,2970; L,R=150,1950
G='#b8860b'; C='#1a1a1a'; T='#4b5563'
out=[]
def img(x,y,w,h,u): out.append(f'<image x="{x}" y="{y}" width="{w}" height="{h}" xlink:href="{u}"/>')

# Row 1: case photo, adjustments diagram, key
y1=600; rh=650
pw=round(rh*cw/ch); img(L,y1,pw,rh,case)
ax=L+pw+40; aw2=round(rh*aw/ah); img(ax,y1,aw2,rh,adj)
kx=ax+aw2+30
keys=['Working face','Blades','Thumbwheel','Locking knob','Blade clamp screw']
ky=y1+rh/2-2*95
for i,k in enumerate(keys):
    yy=ky+i*95
    out.append(f'<circle cx="{kx+24}" cy="{yy}" r="24" fill="{C}"/>'
               f'<text x="{kx+24}" y="{yy+11}" text-anchor="middle" font-size="30" font-weight="600" fill="#fff">{i+1}</text>'
               f'<text x="{kx+64}" y="{yy+12}" font-size="34" fill="{C}">{k}</text>')

# Row 2: features in three columns
feats=[["Thumbwheel adjustment,","0.5 mm per turn, with","locking knob"],
       ["Set for 1.5 mm purfling;","reverse the blades for","any other width"],
       ["Solid brass, hand","assembled in Britain"]]
y2=y1+rh+90; colw=(R-L)/3
for c,f in enumerate(feats):
    x=L+c*colw
    out.append(f'<circle cx="{x+12}" cy="{y2-13}" r="10" fill="{G}"/>')
    for j,line in enumerate(f):
        out.append(f'<text x="{x+45}" y="{y2+j*48}" font-size="38" fill="{C}">{line}</text>')

# Row 3: blade diagrams + instructions
y3=y2+3*48+120
dw=500; dh=round(dw*bh/bw)
img(L,y3,dw,dh,b1); img(L+dw+30,y3,dw,dh,b2)
bx=L+2*dw+30+40; bwid=R-bx
out.append(f'<rect x="{bx}" y="{y3}" width="{bwid}" height="{dh}" fill="#f5f5f0"/>'
           f'<rect x="{bx}" y="{y3}" width="10" height="{dh}" fill="{G}"/>'
           f'<text x="{bx+50}" y="{y3+85}" font-family="Playfair Display" font-size="50" fill="{C}">Using the marker</text>')
steps=[(["Sharpen the blades first: they", "are supplied unsharpened."],False),
       (["Always undo the locking knob", "before turning the thumbwheel."],True),
       (["Set the margin with the", "thumbwheel (0.5 mm per turn),", "then tighten the locking knob."],False),
       (["Test on scrap wood before", "marking the instrument."],False)]
yy=y3+165
for i,(lines,bold) in enumerate(steps):
    out.append(f'<circle cx="{bx+68}" cy="{yy-11}" r="20" fill="{G}"/>'
               f'<text x="{bx+68}" y="{yy-1}" text-anchor="middle" font-size="26" font-weight="600" fill="#fff">{i+1}</text>')
    for line in lines:
        out.append(f'<text x="{bx+105}" y="{yy}" font-size="33" fill="{C}"{" font-weight=\"600\"" if bold else ""}>{line}</text>'); yy+=44
    yy+=26
yn=y3+dh+120
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Inter">
<rect width="{W}" height="{H}" fill="#ffffff"/>
<image x="{(W-640)/2}" y="70" width="640" height="{640*lh/lw:.0f}" xlink:href="{logo}"/>
<text x="{W/2}" y="440" text-anchor="middle" font-family="Playfair Display" font-size="150" fill="{C}">Purfling Marker</text>
<text x="{W/2}" y="530" text-anchor="middle" font-size="50" fill="{T}">A double-blade purfling marker in solid brass</text>
{''.join(out)}
<text x="{W/2}" y="{yn}" text-anchor="middle" font-size="34" fill="{T}">Based on the original design by Brian Hart and Shem Mackey.</text>
<text x="{W/2}" y="{yn+50}" text-anchor="middle" font-size="34" fill="{T}">Supplied in a fitted case with a 2 mm hex key.</text>
<rect x="0" y="2580" width="{W}" height="390" fill="#f5f5f0"/>
<text x="150" y="2810" font-family="Playfair Display" font-size="220" fill="{G}">£99</text>
<text x="{R}" y="2700" text-anchor="end" font-family="Playfair Display" font-size="64" fill="{C}">Paul Fremantle</text>
<text x="{R}" y="2790" text-anchor="end" font-size="48" fill="{C}">paul@fremantle.org</text>
<text x="{R}" y="2870" text-anchor="end" font-size="48" fill="{C}">+44 7740 199 729</text>
</svg>'''
cairosvg.svg2pdf(bytestring=svg.encode(), write_to=str(HERE/'purfling-marker-poster.pdf'), output_width=595.28, output_height=841.89)
