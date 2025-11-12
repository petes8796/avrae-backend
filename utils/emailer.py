import os, smtplib
from email.message import EmailMessage

def send_new_application_email(app_id, doc):
    ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")  # recipient (you)
    SMTP_USER = os.getenv("GMAIL_USER")     # sender
    SMTP_PASS = os.getenv("GMAIL_APP_PASSWORD")

    if not all([ADMIN_EMAIL, SMTP_USER, SMTP_PASS]):
        print("Email not sent — SMTP credentials missing.")
        return

    msg = EmailMessage()
    msg["Subject"] = f"New Avrae Application: {doc.get('name')}"
    msg["From"] = SMTP_USER
    msg["To"] = ADMIN_EMAIL

    msg.set_content(f"""
    New application received:

    Name: {doc.get('name')}
    Email: {doc.get('email')}
    Country: {doc.get('country')}
    Reason: {doc.get('reason')}

    Check your admin dashboard for approval.
    """)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(SMTP_USER, SMTP_PASS)
            smtp.send_message(msg)
            print(f"Email sent successfully to {ADMIN_EMAIL}")
    except Exception as e:
        print("Failed to send email:", e)
