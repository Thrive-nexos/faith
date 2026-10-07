"""Build the portfolio-matched CV. Original supplied CV is preserved in Downloads."""
from pathlib import Path
from xml.sax.saxutils import escape
import shutil

from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'output/pdf/OJO_OLUWATOBI_FAITH_CV.pdf'
OUT.parent.mkdir(parents=True, exist_ok=True)
FONT = Path('C:/Windows/Fonts')
for name, filename in [('Body','calibri.ttf'),('BodyBold','calibrib.ttf'),('Display','georgia.ttf'),('DisplayItalic','georgiai.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(FONT / filename)))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='BodyBold',italic='Body',boldItalic='BodyBold')

GREEN = HexColor('#0B2B26')
DARK = HexColor('#071C18')
CREAM = HexColor('#F6F1E7')
GOLD = HexColor('#C6A15B')
INK = HexColor('#263B33')
MUTED = HexColor('#5E685F')
LINE = HexColor('#D9DCCD')
W,H = A4
LEFT = 45
RIGHT = W-45
WIDTH = RIGHT-LEFT

c = canvas.Canvas(str(OUT), pagesize=A4)
c.setTitle('Ojo Oluwatobi Faith | Management, Storekeeping & Operations CV')
c.setAuthor('Ojo Oluwatobi Faith')
c.setSubject('Management, storekeeping, operations, education and national service')

STYLES = {
    'body': ParagraphStyle('body',fontName='Body',fontSize=11,leading=15,textColor=INK),
    'small': ParagraphStyle('small',fontName='Body',fontSize=9.5,leading=13,textColor=MUTED),
    'job': ParagraphStyle('job',fontName='Display',fontSize=17,leading=21,textColor=GREEN),
    'org': ParagraphStyle('org',fontName='BodyBold',fontSize=10.5,leading=14,textColor=GREEN),
    'white': ParagraphStyle('white',fontName='Body',fontSize=10.5,leading=15,textColor=CREAM),
}

def text(value,x,top,width=WIDTH,style='body'):
    p=Paragraph(value,STYLES[style]); _,height=p.wrap(width,H)
    p.drawOn(c,x,H-top-height)
    return top+height

def rule(top,x=LEFT,width=WIDTH,color=LINE):
    c.setStrokeColor(color);c.setLineWidth(.55);c.line(x,H-top,x+width,H-top)

def label(value,top):
    c.setStrokeColor(GOLD);c.setLineWidth(1);c.line(LEFT,H-top-5,LEFT+20,H-top-5)
    c.setFillColor(GREEN);c.setFont('BodyBold',9)
    c.drawString(LEFT+30,H-top-8,value.upper())
    return top+24

def bullet(value,top):
    c.setFillColor(GOLD);c.circle(LEFT+2,H-top-7,1.5,fill=1,stroke=0)
    return text(escape(value),LEFT+13,top,WIDTH-13)+3

def job(role,company,dates,top,bullets=(),location=None):
    rule(top)
    top+=12
    # Dates are separate metadata, never forced against a long title.
    top=text(escape(role),LEFT,top,WIDTH,'job')
    top=text(escape(company)+(f' | {escape(location)}' if location else ''),LEFT,top+3,WIDTH,'org')
    top=text(escape(dates),LEFT,top+2,WIDTH,'small')+8
    for entry in bullets:
        top=bullet(entry,top)
    return top+12

def footer(page):
    rule(H-42)
    c.setFillColor(MUTED);c.setFont('Body',8.5)
    c.drawString(LEFT,27,'OJO OLUWATOBI FAITH  /  MANAGEMENT & OPERATIONS')
    c.drawRightString(RIGHT,27,f'{page} / 2')

def page_background():
    c.setFillColor(CREAM);c.rect(0,0,W,H,fill=1,stroke=0)

# PAGE 1: management and storekeeping take precedence over specialist experience.
page_background()
c.setFillColor(GREEN);c.rect(0,H-182,W,182,fill=1,stroke=0)
c.setStrokeColor(GOLD);c.setLineWidth(1);c.line(LEFT,H-31,LEFT+25,H-31)
c.setFillColor(CREAM);c.setFont('BodyBold',8.7)
c.drawString(LEFT+36,H-34,'MANAGEMENT  /  STOREKEEPING  /  OPERATIONS')
c.setFont('Display',29);c.drawString(LEFT,H-80,'Ojo Oluwatobi')
c.setFont('DisplayItalic',30);c.drawString(LEFT,H-115,'Faith')
text('Manager | Storekeeper | Operations Professional',LEFT,132,390,'white')
c.setFont('Body',9.5)
c.drawString(LEFT,H-164,'tobet4rate@gmail.com  |  +234 815 041 1425  |  +234 902 665 5823')
c.linkURL('mailto:tobet4rate@gmail.com',(LEFT,H-169,LEFT+112,H-155),relative=0)
image=ROOT/'public/images/profile/profile-studio.png'
if image.exists():
    c.setFillColor(GOLD);c.rect(RIGHT-80,H-143,81,109,fill=1,stroke=0)
    c.drawImage(ImageReader(str(image)),RIGHT-78,H-141,width=77,height=105,preserveAspectRatio=True,anchor='c',mask='auto')

y=205
y=label('Professional profile',y)
y=text('Management and operations professional with experience in storekeeping, farm management, hospitality management and institutional coordination. Worked in stockkeeping at Olorumlami in Ogbomoso, Oyo State, in 2024. Brings practical experience in supervising labour, maintaining records, monitoring activities and preparing documentation. Seeking opportunities in management, storekeeping and operational support.',LEFT,y)
y+=23
y=label('Management & storekeeping experience',y)
y=job('Storekeeper','Olorumlami','2024',y,[
    'Gained stockkeeping experience in a storekeeping role.'
],location='Ogbomoso, Oyo State')
y=job('Farm Manager','Big Tobex Farm Limited','January 2021 - December 2024',y,[
    'Oversaw daily farm operations across crop production and livestock management.',
    'Maintained records and supervised labour for adherence to safety standards.',
    'Diagnosed livestock ailments and supported farm productivity.'
])
y=job('Bar Manager','Officers Mess','2022 - 2024',y,[
    'Held a management role in a hospitality setting.'
],location='Niger State')
y+=3
y=label('Core capabilities',y)
y=text('Operations management | Stockkeeping | Team supervision | Record keeping<br/>Coordination | Activity monitoring | Documentation | Reporting | Safety standards',LEFT,y)
assert y < H-60, f'Page 1 content exceeds safe boundary: {y}'
footer(1);c.showPage()

# PAGE 2: complementary experience and the supplied credentials.
page_background()
c.setFillColor(GREEN);c.rect(0,H-95,W,95,fill=1,stroke=0)
c.setFillColor(CREAM);c.setFont('Display',23);c.drawString(LEFT,H-45,'Ojo Oluwatobi Faith')
c.setFont('Body',10);c.drawString(LEFT,H-69,'Experience, education & service')
c.setStrokeColor(GOLD);c.line(RIGHT-36,H-47,RIGHT,H-47)
y=119
y=label('Additional professional experience',y)
y=job('Planning & Monitoring Officer','National Centre for Agricultural Mechanization (NCAM)','Dates not specified',y,[
    'Coordinated and monitored official visits and activities within the centre.',
    'Supported institutional protocols and prepared visitor documentation and reports.'
],location='Nigeria')
y=job('Veterinary Officer','Judif Farm','July 2025 - Present',y,[
    'Provide veterinary care, diagnose and treat livestock ailments.',
    'Administer vaccinations and manage animal health programmes.',
    'Advise on nutrition and breeding for livestock health.'
])
y+=8
y=label('Education',y)
y=text('Bachelor of Agricultural Technology',LEFT,y,WIDTH,'job')
y=text('General Agriculture',LEFT,y+3,WIDTH,'org')
y=text('Federal University of Technology, Minna | 2024',LEFT,y+3)
y=text('Second Class Honours (Lower Division)',LEFT,y+2,WIDTH,'small')
y+=22
y=label('National service & recognition',y)
y=text('Certificate of National Service',LEFT,y,WIDTH,'job')
y=text('National Youth Service Corps | 30 July 2025 - 29 July 2026',LEFT,y+4,WIDTH,'org')
y=text('Completed one year of national service. Certificate dated 29 July 2026.',LEFT,y+5)
y+=18
y=text('Road Safety CDS - Certificate of Service',LEFT,y,WIDTH,'job')
y=text('Federal Road Safety Corps CDS Group',LEFT,y+4,WIDTH,'org')
y=text('Awka North LGA, Anambra State | 9 July 2026',LEFT,y+3,WIDTH,'small')
y=text('Recognised for diligent and selfless service within the Community Development Service group.',LEFT,y+5)
assert y < H-60, f'Page 2 content exceeds safe boundary: {y}'
footer(2);c.save()

# Keep both local website download and production static download in sync.
shutil.copy2(OUT,ROOT/'public/OJO_OLUWATOBI_FAITH_CV.pdf')
dist=ROOT/'dist'
if dist.is_dir():
    shutil.copy2(OUT,dist/'OJO_OLUWATOBI_FAITH_CV.pdf')
print(f'Created: {OUT}')
print('Updated the local website CV download.')
