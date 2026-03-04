from fpdf import FPDF, XPos, YPos

pdf = FPDF(orientation="P", unit="mm", format="A4")

pdf.add_page()


pdf.set_font(family="Helvetica", style = "B", size=12)
pdf.cell(w=26, h=12, text="Hello World", align="L",
         new_x=XPos.LMARGIN, new_y=YPos.NEXT, border=0)
pdf.cell(w=0, h=6, text="Hi There !", align="L",
         new_x=XPos.LMARGIN, new_y=YPos.NEXT, border=1)

pdf.output("output.pdf")