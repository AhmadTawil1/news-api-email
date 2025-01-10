import smtplib, ssl
import os
from email.mime.text import MIMEText


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "ahmadtw213@gmail.com"
    password = os.getenv("PASSWORD")
    
    receiver = "ahmadtw213@gmail.com"
    my_context = ssl.create_default_context()

    # Create a MIMEText object with UTF-8 encoding
    email_message = MIMEText(message, "plain", "utf-8")
    email_message["Subject"] = "Tesla News"
    email_message["From"] = username
    email_message["To"] = receiver

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, email_message.as_string())
