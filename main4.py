from fpdf import FPDF
import pandas as pd

class PDF(FPDF):
    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 12)
        self.cell(0, 10, str(self.page_no()), 0, 0, "R")

pdf = PDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    # Set the header
    pdf.set_font("Helvetica", "B", 24)
    pdf.set_text_color(65,105,225)

    pdf.cell(0, 12, row["Topic"], ln=1)
    pdf.line(10,22,200,22)

    # Set the footer
    pdf.ln(265)
    pdf.set_font("Helvetica", "I", 8)
    pdf.set_text_color(65,105,225)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        # Set the footer
        pdf.set_font("Helvetica", "I", 8)
        pdf.set_text_color(65,105,225)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("output.pdf")