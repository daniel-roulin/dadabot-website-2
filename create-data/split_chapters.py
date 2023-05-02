import os
import pdftotext
from PyPDF2 import PdfFileMerger
from progress import progress


def split_pdf(pdf, start, stop, name):
    # print(f"Splitting pdf '{pdf.name}' into '{name}' from {start} to {stop}")
    merger = PdfFileMerger()
    merger.append(fileobj=pdf, pages=(start - 1, stop))
    output = open(name, "wb")
    merger.write(output)
    output.close()


def split_chapters(pdf_path, destination_dir):
    print("Splitting complete pdf into chapters...")

    # Create destination folder if not exists
    os.makedirs(destination_dir, exist_ok=True)

    # Load the PDF
    pdf_file = open(pdf_path, "rb")
    pdf_text = pdftotext.PDF(pdf_file)

    # Iterate over all the pages
    start = 0
    for i in range(len(pdf_text)):
        page = pdf_text[i]
        if page.startswith("Chapter"):
            stop = i
            if start:
                chapter = int(page[8:10]) - 1
                destination_path = os.path.join(destination_dir, f"chapter{chapter}.pdf")
                split_pdf(pdf_file, start, stop, destination_path)
            start = stop + 1
        progress(i, len(pdf_text))

    destination_path = os.path.join(destination_dir, f"chapter{chapter + 1}.pdf")
    split_pdf(pdf_file, start, stop, destination_path)

    pdf_file.close()
    print("Done!")