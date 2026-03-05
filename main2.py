from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Helvetica", style = "B", size=24)
    pdf.set_text_color(65, 105, 225)  # Blu
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L",
            ln=1)
    pdf.line(10, 22, 200, 22)
    # numero pagina
    pdf.set_y(266)
    pdf.set_font("Helvetica", "I", 12)
    #pdf.cell(0, 10, f"Pagina {pdf.page_no()}", 0, 0, "R")
    pdf.cell(0, 10, str(pdf.page_no()), 0, 0, "R")

'''
pdf.cell(w=26, h=12, txt="Hello World", align="L",
         ln=0, border=0)

pdf.cell(w=26, h=12, txt="Hello World", align="L",
         ln=1)

pdf.cell(w=26, h=12, txt="Hello World", align="L",
         ln=0, border=1)

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

'''
pdf.output("output.pdf")
