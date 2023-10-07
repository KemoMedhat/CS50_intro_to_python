from fpdf import FPDF
class my_pdf(FPDF):
    def header(self):
        self.image("./shirtificate.png", 10, 70, 190)
        self.set_font("helvetica", "", 48)
        self.cell(0, 57, "CS50 Shirtificate", align="C")
        self.ln(20)




def main():
    name = input("name: ")
    pdf = my_pdf()
    pdf.add_page(orientation="portrait", format="a4")
    pdf.set_font('helvetica', size=24)
    pdf.cell(0, 213,f"{name} took CS50",align="C")
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()