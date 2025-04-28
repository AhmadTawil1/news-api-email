import smtplib
import ssl
import os
import logging
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def send_email(message):
    try:
        # Get email configuration from environment variables
        host = "smtp.gmail.com"
        port = 465
        username = os.getenv('EMAIL_USERNAME')
        password = os.getenv('EMAIL_PASSWORD')
        receiver = os.getenv('RECEIVER_EMAIL')

        # Validate required environment variables
        if not all([username, password, receiver]):
            raise ValueError("Missing required email configuration in environment variables")

        # Create email message
        email_message = MIMEText(message, "plain", "utf-8")
        email_message["Subject"] = "Today's News Digest"
        email_message["From"] = username
        email_message["To"] = receiver

        # Create SSL context
        context = ssl.create_default_context()

        # Send email
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, email_message.as_string())
            logging.info(f"Email sent successfully to {receiver}")

    except smtplib.SMTPAuthenticationError:
        logging.error("Email authentication failed. Please check your credentials.")
        raise
    except smtplib.SMTPException as e:
        logging.error(f"SMTP error occurred: {str(e)}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error while sending email: {str(e)}")
        raise
