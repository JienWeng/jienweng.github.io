#!/usr/bin/env python3
"""Build the downloadable public CV from the same TOML collections as the website."""
import re
from html import escape
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether
from generate_llms import ROOT, SECTIONS, read


def markup(text):
    value = escape(text)
    return re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)',
                  r'<link href="\2" color="#875b43">\1</link>', value)


def main():
    config = read('config.toml')
    extra = config['extra']
    ink = colors.HexColor('#35342f')
    styles = {
        'name': ParagraphStyle('name', fontName='Helvetica', fontSize=24, leading=28, textColor=ink, spaceAfter=5),
        'role': ParagraphStyle('role', fontName='Helvetica', fontSize=12, leading=16, textColor=ink, spaceAfter=7),
        'body': ParagraphStyle('body', fontName='Helvetica', fontSize=9.5, leading=13, textColor=ink, spaceAfter=4),
        'section': ParagraphStyle('section', fontName='Helvetica-Bold', fontSize=13, leading=17, textColor=ink, spaceBefore=14, spaceAfter=8, keepWithNext=True),
        'title': ParagraphStyle('title', fontName='Helvetica-Bold', fontSize=10, leading=14, textColor=ink, spaceAfter=3, keepWithNext=True),
        'meta': ParagraphStyle('meta', fontName='Helvetica', fontSize=8.5, leading=12, textColor=colors.HexColor('#5f5c54'), spaceAfter=3),
    }
    story = [Paragraph('Jien Weng Lai', styles['name']),
             Paragraph('Product Manager &amp; Researcher', styles['role']),
             Paragraph(markup(config['description']), styles['body']),
             Paragraph(f'<link href="mailto:{extra["email"]}">{extra["email"]}</link> | '
                       f'<link href="{config["base_url"]}/cv/">jienweng.github.io/cv</link>', styles['body'])]
    profiles = [('LinkedIn', 'linkedin'), ('GitHub', 'github'), ('X', 'x'), ('Google Scholar', 'scholar'), ('ORCID', 'orcid')]
    story.append(Paragraph(' | '.join(f'<link href="{escape(extra[key])}" color="#875b43">{label}</link>' for label, key in profiles), styles['body']))
    for label, name in SECTIONS:
        for index, item in enumerate(read(f'content/cv/{name}.toml')['collection']):
            entry = [Paragraph(markup(item['title']), styles['title'])]
            meta = [item[key] for key in ('date', 'subtitle', 'issuer') if item.get(key)]
            if meta:
                entry.append(Paragraph(markup(' | '.join(meta)), styles['meta']))
            for key in ('authors', 'venue', 'status', 'content'):
                if item.get(key):
                    prefix = {'authors': 'Authors: ', 'venue': 'Venue: ', 'status': 'Status: '}.get(key, '')
                    entry.append(Paragraph(markup(prefix + item[key]), styles['body']))
            if item.get('link'):
                url = escape(item['link'])
                label_link = 'View credential' if name == 'certifications' else 'View reference'
                entry.append(Paragraph(f'<link href="{url}" color="#875b43">{label_link}</link>', styles['meta']))
            if index == 0:
                entry.insert(0, Paragraph(label, styles['section']))
            entry.append(Spacer(1, 6))
            story.append(KeepTogether(entry))
    path = ROOT / 'static/cv/jien-weng-lai-public-cv.pdf'
    def footer(canvas, doc):
        canvas.setFont('Helvetica', 8)
        canvas.setFillColor(colors.HexColor('#5f5c54'))
        canvas.drawString(42, 25, 'Jien Weng Lai | Public curriculum vitae | jienweng.github.io/cv/')
        canvas.drawRightString(A4[0] - 42, 25, str(doc.page))
    doc = SimpleDocTemplate(str(path), pagesize=A4, rightMargin=42, leftMargin=42,
                            topMargin=40, bottomMargin=44, title='Jien Weng Lai - Public Curriculum Vitae',
                            author='Jien Weng Lai', invariant=1)
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(f'Generated {path.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
