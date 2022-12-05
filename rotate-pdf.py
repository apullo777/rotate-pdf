import PyPDF2

with open("input.pdf", "rb") as file:
    pdf = PyPDF2.PdfFileReader(file)
    output = PyPDF2.PdfFileWriter()
    
    # Iterate over the pages of the PDF
    for i in range(pdf.getNumPages()):
        page = pdf.getPage(i)
        page.rotateClockwise(90)
        output.addPage(page)
    
    # Write the output PDF to a file
    with open("output.pdf", "wb") as output_file:
        output.write(output_file)