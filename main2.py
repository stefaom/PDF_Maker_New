from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")

pdf.add_page()

pdf.set_font(family="Helvetica", style = "B", size=12)
'''
pdf.cell(w=26, h=12, txt="Hello World", align="L",
         ln=0, border=0)
'''
pdf.cell(w=26, h=12, txt="Hello World", align="L",
         ln=1)
'''
pdf.cell(w=26, h=12, txt="Hello World", align="L",
         ln=0, border=1)
'''
pdf.set_font(family="Helvetica", size=10)
pdf.cell(w=0, h=12, txt="Hi There !", align="L",
         ln=1)

pdf.add_page()

pdf.set_font(family="Helvetica", style = "B", size=12)
pdf.cell(w=26, h=12, txt="Hello World", align="L",
         ln=1)
pdf.set_font(family="Helvetica", size=10)
pdf.cell(w=0, h=12, txt="Hi There !", align="L",
         ln=1)


pdf.output("output.pdf")
