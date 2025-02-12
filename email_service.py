import smtplib
import random

def send_email_otp(email):
    otp = str(random.randint(100000, 999999))  # Generate a 6-digit OTP

    # MailHog SMTP configuration
    smtp_server = "localhost"  # MailHog runs on localhost
    smtp_port = 1025           # Default MailHog SMTP port

    # Send email using MailHog
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.sendmail(
            'no-reply@example.com',  # From email
            email,                   # To email
            f"Subject: Your OTP\n\nYour OTP is: {otp}"  # Email content
        )
    print(f"OTP sent to {email} (Check MailHog: http://localhost:8025)")
    return otp
