import webbrowser
import os

from fpdf import FPDF


class PdfReport:
    """
    Creates a Pdf file that contains data
    about the flatmates
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill_to_pay):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        flatmate1_pay = str(round(flatmate1.pays(bill_to_pay, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill_to_pay, flatmate1), 2))
        pdf.add_page()

        # Add icon
        pdf.image("files/house.jpg", w=30, h=30)

        # insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, align="C", ln=1)

        # Insert Period label
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt='Period', border=0)
        pdf.cell(w=150, h=40, txt=bill_to_pay.period, border=0, ln=1)

        # Insert Name and amount to pay label
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)

        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0, ln=1)
        pdf.output(f"files/{self.filename}")

        os.chdir("files")
        webbrowser.open(self.filename)


