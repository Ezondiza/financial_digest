# financial_digest/ocr/parser.py

import re
import pandas as pd

def parse_agency_data(raw_text):
    """
    Parses agency financial data from OCR text.
    Expected format: AgencyName USD NPR Total
    """
    pattern = r"(?P<agency>[A-Za-z\s]+)\s+(?P<usd>[\d,]+\.\d{2})\s+(?P<npr>[\d,]+\.\d{2})\s+(?P<total>[\d,]+\.\d{2})"
    matches = re.finditer(pattern, raw_text)
    data = [m.groupdict() for m in matches]
    return pd.DataFrame(data)

def parse_cheques(raw_text):
    """
    Parses cheque data from OCR text.
    Expected format: AgencyName DD-MMM-YY USD
    """
    pattern = r"(?P<agency>[A-Za-z\s]+)\s+(?P<date>\d{2}-[A-Za-z]{3}-\d{2})\s+(?P<usd>[\d,]+\.\d{2})"
    matches = re.finditer(pattern, raw_text)
    data = [m.groupdict() for m in matches]
    return pd.DataFrame(data)
