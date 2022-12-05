# Rotate PDF
This Python script uses the PyPDF2 module to rotate each page of a PDF file by a specified number of degrees.

It simplifies the process of rotating the pages of a PDF file, allowing the user to easily and quickly rotate multiple pages without having to manually open the PDF and rotate each page individually. It is particularly useful for PDF files with a large number of pages, as the program can rotate all of the pages in just a few seconds.

## How it works
The script first imports the PyPDF2 module, which is used to manipulate PDF files in Python. It then opens the input PDF file, reads its pages, and rotates each page by the specified number of degrees. The rotated pages are then written to a new PDF file.

## How to use
1. Install the PyPDF2 module by running the following command:

`pip install PyPDF2`

2. Open the rotate_pdf.py file in a text editor and specify the input and output file names, as well as the rotation angle, at the top of the file:

```
# The input and output file names
INPUT_FILE = "input.pdf"
OUTPUT_FILE = "output.pdf"

# The rotation angle (in degrees)
ANGLE = 90
```
3. Run the script by running the following command:

`python rotate_pdf.py`

The rotated PDF will be written to the output file specified in the script.

Note that you may need to adjust the code to match your specific requirements.



