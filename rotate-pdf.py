import PyPDF2

# The input and output file names
INPUT_FILE = "input.pdf"
OUTPUT_FILE = "output.pdf"

# The rotation angle (in degrees)
ANGLE = 90

with open(INPUT_FILE, "rb") as file:
    pdf = PyPDF2.PdfFileReader(file)
    output = PyPDF2.PdfFileWriter()
    
    # Iterate over the pages of the PDF
    for i in range(pdf.getNumPages()):
        page = pdf.getPage(i)
        page.rotateClockwise(ANGLE)
        output.addPage(page)
    
    # Write the output PDF to a file
    with open(OUTPUT_FILE, "wb") as output_file:
        output.write(output_file)