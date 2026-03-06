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

    for i in range(row["Pages"]):
        pdf.add_page()

        # numero pagina
        pdf.set_y(266)
        pdf.set_font("Helvetica", "I", 12)
        #pdf.cell(0, 10, f"Pagina {pdf.page_no()}", 0, 0, "R")
        pdf.cell(0, 10, str(pdf.page_no()), 0, 0, "R")

pdf.output("output.pdf")