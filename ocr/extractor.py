# financial_digest/ocr/extractor.py

import easyocr
import pdfplumber

# Initialize EasyOCR reader (English only, add 'ne' for Nepali if needed)
reader = easyocr.Reader(['en'])

def extract_text_from_image(image_path):
    """
    Extracts text from an image file using EasyOCR.
    """
    results = reader.readtext(image_path, detail=0)
    return "\n".join(results)

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file using pdfplumber + EasyOCR fallback.
    """
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            # Try direct text extraction
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
            else:
                # Fallback: render page as image and OCR
                img = page.to_image(resolution=300).original
                results = reader.readtext(img, detail=0)
                text += "\n".join(results) + "\n"
    return text
