# financial_digest/mailer/templates.py

def monthly_template(summary_text):
    """
    Returns an HTML template for the monthly summary email.
    """
    return f"""
    <html>
        <body style="font-family: Arial, sans-serif;">
            <h2 style="color: #2E86C1;">Monthly Financial Summary</h2>
            <p>{summary_text}</p>
            <hr>
            <p style="font-size: 12px; color: gray;">
                This is an automated message from Financial Digest.
            </p>
        </body>
    </html>
    """
