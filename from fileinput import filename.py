from fileinput import filename
import json
from fpdf import FPDF

#Page Layout
pdf = FPDF('P', 'mm', 'Letter')
pdf.add_page()

#Import json file
with open('Resume.json') as resume:
    data = json.load(resume)

#--------------------------------------format inside json file---------------------------------------

#Personal Details
for nins in data: 
    pdf.ln(5)
    pdf.set_font("times", 'B', 16)
    pdf.cell(200, 6, nins['name'], ln=1)

    pdf.set_font("times", '', 11)
    pdf.cell(0, 5, nins['place'], ln=1)
    pdf.cell(0, 5, nins['phone_number'], ln=1)
    pdf.cell(0, 5, nins['mail'], ln=1)
    pdf.cell(0, 6, nins['account'], ln=1)

#skills
pdf.set_font("times", 'BU', 14)
pdf.cell(100, 15, nins['nino'], ln=1)

for onin in nins['skills']:
        pdf.set_font("times", '', 11)
        pdf.cell(0, 5, f"{onin['skill_01']}", ln=1)
        pdf.cell(0, 5, f"{onin['skill_02']}", ln=1)
        pdf.cell(0, 5, f"{onin['skill_03']}", ln=1)
        pdf.cell(0, 5, f"{onin['skill_04']}", ln=1)
        pdf.cell(0, 5, f"{onin['skill_05']}", ln=1)
        pdf.cell(0, 5, f"{onin['skill_06']}", ln=1)
        pdf.cell(0, 5, f"{onin['skill_07']}", ln=1)
        pdf.cell(0, 5, f"{onin['skill_08']}", ln=1)

#Experiences
pdf.set_font("times", 'BU', 14)
pdf.cell(100, 15, nins['pixelrei'], ln=1)

for rei in nins['exp']:
        pdf.set_font("times", 'BI', 13)
        pdf.cell(0, 5, f"{rei['top']}", ln=1)
        pdf.set_font("times", 'I', 12)
        pdf.cell(0, 6.5, f"{rei['company']}", ln=1)
        pdf.set_font("times", '', 11)
        pdf.cell(0, 6, f"{rei['dates']}", ln=1)
        pdf.cell(0, 5.5, f"{rei['ronan']}", ln=1)
        pdf.cell(0, 5.5, f"{rei['alexis']}", ln=1)
        pdf.cell(0, 5.5, f"{rei['timola']}", ln=1)
        pdf.cell(0, 5.5, f"{rei['valle']}", ln=1)
        pdf.set_font("times", 'I', 12)
        pdf.cell(0, 10, f"{rei['next']}", ln=1)
        pdf.set_font("times", '', 11)
        pdf.cell(0, 4, f"{rei['king']}", ln=1)
        pdf.cell(0, 7.7, f"{rei['nay']}", ln=1)
        pdf.cell(0, 3.5, f"{rei['justin']}", ln=1)

#Educational Background
pdf.set_font("times", 'BU', 14)
pdf.cell(100, 15, nins['educ'], ln=1)

for mads in nins['school']:
    pdf.set_font("times", '', 11)
    pdf.cell(50, 5, f"{mads['ter']}")
    pdf.cell(120, 5, f"{mads['univ']}")
    pdf.cell(80, 5, f"{mads['year']}", ln=1)

#Lines
pdf.set_line_width(0.5)
pdf.line(x1=12, y1=45, x2=205, y2=45) #personal details
pdf.line(x1=12, y1=100, x2=205, y2=100) #skills
pdf.line(x1=12, y1=180, x2=205, y2=180)#experience

pdf.output("VALLE_RONAN_ALEXIS.pdf")