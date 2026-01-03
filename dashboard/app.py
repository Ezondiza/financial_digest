# financial_digest/dashboard/app.py

import streamlit as st
from financial_digest.mailer.monthly import generate_monthly_summary
from financial_digest.ocr.extractor import extract_text_from_image, extract_text_from_pdf
from financial_digest.ocr.parser import parse_agency_data, parse_cheques
from financial_digest.data.archive import save_to_csv, save_to_excel


st.title("Financial Digest Dashboard")

uploaded_file = st.file_uploader("Upload an image or PDF", type=["png", "jpg", "jpeg", "pdf"])

raw_text = ""
if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        raw_text = extract_text_from_pdf(uploaded_file)
    else:
        raw_text = extract_text_from_image(uploaded_file)

agency_df, cheques_df = None, None

if raw_text:
    st.subheader("Parsed Agency Data")
    agency_df = parse_agency_data(raw_text)
    if not agency_df.empty:
        st.dataframe(agency_df)
        if st.button("Archive Agency Data"):
            save_to_csv(agency_df, "agency")
            st.success("Agency data archived successfully!")

    st.subheader("Parsed Cheques")
    cheques_df = parse_cheques(raw_text)
    if not cheques_df.empty:
        st.dataframe(cheques_df)
        if st.button("Archive Cheques Data"):
            save_to_csv(cheques_df, "cheques")
            st.success("Cheques data archived successfully!")

    if st.button("Archive Full Summary (Excel)"):
        save_to_excel(agency_df, cheques_df)
        st.success("Full summary archived successfully!")

if st.button("Send Monthly Summary"):
    generate_monthly_summary()
    st.success("Monthly summary email sent successfully!")
