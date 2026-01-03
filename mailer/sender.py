# financial_digest/mailer/sender.py

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import streamlit as st

def send_email(recipient, subject, body):
    """
    Sends an email using SMTP credentials stored in Streamlit Secrets.
    """
    smtp_server = st.secrets["smtp"]["server"]
    smtp_port = st.secrets["smtp"]["port"]
    smtp_user = st.secrets["smtp"]["user"]
    smtp_password = st.secrets["smtp"]["password"]

    msg = MIMEMultipart()
    msg["From"] = smtp_user
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html"))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.send_message(msg)
        print(f"Email sent to {recipient} with subject '{subject}'")
    except Exception as e:
        print(f"Failed to send email: {e}")
