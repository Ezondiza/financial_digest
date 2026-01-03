# financial_digest/mailer/monthly.py

from mailer.sender import send_email
from mailer.templates import monthly_template

def generate_monthly_summary():
    """
    Generates the monthly financial summary and sends it via email.
    """
    summary_text = "This is the monthly financial summary with key highlights."
    email_body = monthly_template(summary_text)

    recipient = "recipient@example.com"
    subject = "Monthly Financial Summary"

    send_email(recipient, subject, email_body)
    print("Monthly summary generated and email sent.")
