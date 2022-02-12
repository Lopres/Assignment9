from fileinput import filename
import json
from fpdf import FPDF

#Page Layout
pdf = FPDF('P', 'mm', 'Letter')
pdf.add_page()

#Import json file
with open('RESUME.json') as r:
    data = json.load(r)

#-------------------------------------------
for name in data: 
    pdf.ln(5)
    pdf.set_font("times", 'I' , 10 ,)
    pdf.cell(0,10,name['Header'],ln=1)
    pdf.set_font("times", 'B', 20)
    pdf.cell(0,10, name['name'], ln=1)

    pdf.set_font("times", '', 11)
    pdf.cell(0, 5, name['place'], ln=1)
    pdf.cell(0, 5, name['phone_number'], ln=1)
    pdf.cell(0, 5, name['email'], ln=1)
    

#this is for skills and experiences
pdf.set_font("times", 'BU', 14)
pdf.cell(100, 15, name['ali'], ln=1)

for skill in name['Skills']:
        pdf.set_font("times", '', 11)
        pdf.cell(0, 5, f"{skill['s1']}", ln=1)
        pdf.cell(0, 5, f"{skill['s2']}", ln=1)
        pdf.cell(0, 5, f"{skill['s3']}", ln=1)
        pdf.cell(0, 5, f"{skill['s4']}", ln=1)
        pdf.cell(0, 5, f"{skill['s5']}", ln=1)

#Experiences
pdf.set_font("times", 'BU', 14)
pdf.cell(100, 15, name['pixelrei'], ln=1)

for rei in name['exp']:
        pdf.set_font("times", 'BI', 13)
        pdf.cell(0, 5, f"{rei['top']}", ln=1)
        pdf.set_font("times", 'BI', 12)
        pdf.cell(0, 6.5, f"{rei['company']}", ln=1)
        pdf.set_font("times", '', 11)
        pdf.cell(0, 6, f"{rei['dates']}", ln=1)
        pdf.cell(0, 5.5, f"{rei['John']}", ln=1)
        pdf.cell(0, 5.5, f"{rei['Alixes']}", ln=1)
        pdf.cell(0, 5.5, f"{rei['Lopres']}", ln=1)
        pdf.set_font("times", 'BI', 12)
        pdf.cell(0, 5.5, f"{rei['next']}", ln=1)
        pdf.set_font("times", 'I', 10)
        pdf.cell(0, 10, f"{rei['next1']}", ln=1)
        pdf.set_font("times", 'I', 11)
        pdf.cell(0, 4, f"{rei['next2']}", ln=1)
        pdf.cell(0, 7.7, f"{rei['next3']}", ln=1)


#Educational Background
pdf.set_font("times", 'BU', 14)
pdf.cell(10, 15, name['educ'], ln=1)

for Sch in name['school']:
    pdf.set_font("times", '', 11)
    pdf.cell(50, 5, f"{Sch['T']}")
    pdf.cell(120, 5, f"{Sch['U']}")
    pdf.cell(80, 5, f"{Sch['Sy']}", ln=1)

#Lines
pdf.set_line_width(0.5)
pdf.line(x1=12, y1=50, x2=205, y2=50) #personal details
pdf.line(x1=12, y1=90, x2=205, y2=90) #skills
pdf.line(x1=12, y1=180, x2=205, y2=180)#experience


pdf.output("Lopres,John Alixes.pdf")
