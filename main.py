# financial_digest/main.py

import argparse
from ocr.extractor import extract_text_from_image, extract_text_from_pdf
from ocr.parser import parse_agency_data, parse_cheques
from data.archive import save_to_csv, save_to_excel
from mailer.monthly import generate_monthly_summary

def run_pipeline(file_path):
    if file_path.lower().endswith(".pdf"):
        raw_text = extract_text_from_pdf(file_path)
    else:
        raw_text = extract_text_from_image(file_path)

    agency_df = parse_agency_data
