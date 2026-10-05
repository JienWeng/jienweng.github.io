"""Render the public CryptoRails deposit flow as exact-text PNG artwork.

Requires Pillow, fonttools, brotli and cairosvg. Run from the repository root.
Sources: docs.cryptorails.tech/guide and /documentation/overview (2026-10-06).
"""
import os
from pathlib import Path
from tempfile import TemporaryDirectory
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'static/img/projects'
PAPER, INK, MUTED, ORANGE, RULE = '#f6f3ec', '#20201e', '#494944', '#b83e12', '#a6a49d'
STAGES = [
    ('Receive', 'Customer deposit address', ['Generate an address per customer.', 'Store it in the merchant backend.']),
    ('Detect', 'Browser watches the chain', ['The customer sends funds.', 'onDeposit gives immediate feedback.']),
    ('Consolidate', 'Backend calls the gateway', ['Validate funds server-side.', 'Sweep to the consolidation wallet.']),
    ('Settle', 'Verified webhook to backend', ['Confirm the sweep on-chain.', 'Verify the signature; credit once.']),
]

with TemporaryDirectory() as temp:
    fonts = {}
    for weight in (400, 600, 800):
        font = TTFont(ROOT / 'static/fonts/archivo-variable.woff2')
        font.flavor = None
        font = instantiateVariableFont(font, {'wght': weight}, inplace=True)
        path = Path(temp) / f'archivo-{weight}.ttf'
        font.save(path)
        fonts[weight] = str(path)

    def render(mobile=False):
        scale = 2
        width, height = (720, 1760) if mobile else (1800, 1030)
        im = Image.new('RGB', (width * scale, height * scale), PAPER)
        d = ImageDraw.Draw(im)
        def text(x, y, value, size=28, weight=400, color=INK):
            f = ImageFont.truetype(fonts[weight], size * scale)
            d.text((x * scale, y * scale), value, font=f, fill=color)
            assert x * scale + d.textlength(value, font=f) <= width * scale - 20 * scale, value
        def line(points, color=RULE, thick=2):
            d.line([(x * scale, y * scale) for x,y in points], fill=color, width=thick * scale)
        def box(x,y,w,h,fill=None):
            d.rectangle((x*scale,y*scale,(x+w)*scale,(y+h)*scale),fill=fill,outline=RULE,width=scale)
        def arrow(x,y,endx,endy):
            line([(x,y),(endx,endy)],ORANGE,3)
            if endx==x:
                line([(endx-7,endy-9),(endx,endy),(endx+7,endy-9)],ORANGE,3)
            else:
                line([(endx-9,endy-7),(endx,endy),(endx-9,endy+7)],ORANGE,3)
        pad = 44 if mobile else 56
        text(pad, 36, 'CryptoRails', 34 if mobile else 40, 800, ORANGE)
        text(pad, 91, 'Deposit to settlement', 44 if mobile else 68, 800)
        text(pad, 159 if mobile else 183, 'Two signals. One authority to settle.', 28 if mobile else 32)
        line([(pad,215 if mobile else 248),(width-pad,215 if mobile else 248)])
        if mobile:
            for i,(verb,title,body) in enumerate(STAGES):
                y=254+i*218
                box(pad,y,width-2*pad,180, '#eee9df' if i==3 else None)
                text(pad+22,y+17,f'{i+1:02}  {verb}',26,600,ORANGE)
                text(pad+22,y+57,title,32,800)
                for j,s in enumerate(body):text(pad+22,y+105+j*33,s,26)
                if i<3:arrow(width//2,y+184,width//2,y+209)
            y=1160
            text(pad,y,'Detect ≠ settle',36,800)
            text(pad,y+60,'onDeposit → immediate feedback',28,600)
            text(pad,y+98,'Client-side signal. Do not credit yet.',26)
            line([(pad,y+147),(width-pad,y+147)])
            text(pad,y+171,'Signed webhook → credit the ledger',28,600,ORANGE)
            text(pad,y+213,'Authoritative after confirmation.',26)
            text(pad,y+251,'Verify HMAC; prevent duplicate credit.',26)
            text(pad,1570,'Gateway transaction states',28,800)
            text(pad,1617,'pending → wait_for_confirmation',26)
            text(pad,1655,'→ confirmed  /  failed on error',26)
            text(pad,1716,'Redrawn from the public integration documentation.',19,color=MUTED)
        else:
            gap=32; bw=(width-2*pad-3*gap)//4
            for i,(verb,title,body) in enumerate(STAGES):
                x=pad+i*(bw+gap);y=298
                box(x,y,bw,270,'#eee9df' if i==3 else None)
                text(x+22,y+23,f'{i+1:02}  {verb}',28,600,ORANGE)
                # Deliberate line breaks preserve readable type at portfolio width.
                titles=[['Customer','deposit address'],['Browser watches','the chain'],['Backend calls','the gateway'],['Verified webhook','to backend']][i]
                for j,s in enumerate(titles):text(x+22,y+75+j*42,s,36,800)
                bodies=[['Generate per customer.','Store in your backend.'],['Customer sends funds.','onDeposit detects them.'],['Validate server-side.','Sweep to tenant wallet.'],['Confirm on-chain.','Verify; credit once.']][i]
                for j,s in enumerate(bodies):text(x+22,y+186+j*36,s,28)
                if i<3:arrow(x+bw+3,y+135,x+bw+gap-4,y+135)
            text(pad,624,'Funds detected',38,800)
            text(pad,682,'onDeposit → immediate feedback',30,600)
            text(pad,726,'Client-side signal. Do not credit the ledger yet.',28,color=MUTED)
            line([(865,624),(865,779)])
            text(925,624,'Funds settled',38,800,ORANGE)
            text(925,682,'Signed webhook → credit the ledger',30,600)
            text(925,726,'Verify HMAC and prevent duplicate credit.',28,color=MUTED)
            line([(pad,815),(width-pad,815)])
            text(pad,851,'Gateway transaction states',28,800)
            text(pad,902,'pending → wait_for_confirmation → confirmed',30,600)
            text(1090,902,'On error → failed',30,600,ORANGE)
            text(pad,981,'Redrawn from the public integration documentation · API key stays in the merchant backend.',22,color=MUTED)
        file=OUT / ('cryptorails-deposit-flow-mobile.png' if mobile else 'cryptorails-deposit-flow.png')
        im.save(file,optimize=True)
        print(file)
    render()
    render(True)

    # Rasterize the authored CRM vectors without changing their wording or geometry.
    config = Path(temp) / 'fonts.conf'
    config.write_text(f'<fontconfig><dir>{temp}</dir></fontconfig>')
    os.environ['FONTCONFIG_FILE'] = str(config)
    import cairosvg
    for name in ('deal-to-cash-mobile', 'project-to-cash', 'project-to-cash-mobile', 'o2c-p2p', 'o2c-p2p-mobile'):
        source = ROOT / 'static/img/blog/quandatics' / f'{name}.svg'
        # The original desktop PNGs remain archived under their existing names.
        target = source.with_name(f'{name}-portfolio.png')
        cairosvg.svg2png(url=str(source), write_to=str(target), scale=2)
        print(target)
