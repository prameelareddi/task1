import os
import PyPDF2
from pytesseract import image_to_string
from pdf2image import convert_from_path

pytesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
os.environ['TESSERACT_CMD'] = pytesseract_path

def extract_text_from_pdf(file_path):
    text = ""
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()
    except Exception:
        pages = convert_from_path(file_path)
        for page in pages:
            text += image_to_string(page)
    return text
