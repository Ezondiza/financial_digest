# financial_digest/data/archive.py

import os
import pandas as pd
from datetime import datetime

ARCHIVE_DIR = "financial_digest/data/archives"

def ensure_archive_dir():
    if not os.path.exists(ARCHIVE_DIR):
        os.makedirs(ARCHIVE_DIR)

def save_to_csv(df, prefix):
    ensure_archive_dir()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{prefix}_{timestamp}.csv"
    filepath = os.path.join(ARCHIVE_DIR, filename)
    df.to_csv(filepath, index=False)
    print(f"Saved {prefix} data to {filepath}")
    return filepath

def save_to_excel(agency_df=None, cheques_df=None):
    ensure_archive_dir()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"financial_summary_{timestamp}.xlsx"
    filepath = os.path.join(ARCHIVE_DIR, filename)

    with pd.ExcelWriter(filepath, engine="xlsxwriter") as writer:
        if agency_df is not None and not agency_df.empty:
            agency_df.to_excel(writer, sheet_name="Agency Data", index=False)
        if cheques_df is not None and not cheques_df.empty:
            cheques_df.to_excel(writer, sheet_name="Cheques", index=False)

    print(f"Saved summary to {filepath}")
    return filepath
