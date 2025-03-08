from fpdf import FPDF

def create_sample_pdf(filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="This is a sample PDF document", ln=1, align="C")
    pdf.cell(200, 10, txt="It contains information about technology and software development.", ln=1, align="C")
    pdf.cell(200, 10, txt="This PDF is created for testing our PDF processing system.", ln=1, align="C")
    pdf.output(filename)

if __name__ == "__main__":
    create_sample_pdf("sample.pdf")
    print("Sample PDF created: sample.pdf")
