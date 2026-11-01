import smtplib
from email.message import EmailMessage
from . import config

def send_email(subject: str, body: str) -> None:
    sender = config.require("EMAIL_FROM")
    password = config.require("EMAIL_APP_PASSWORD")
    recipient = config.require("EMAIL_TO")

    msg = EmailMessage()
    msg["From"], msg["To"], msg["Subject"] = sender, recipient, subject
    msg.set_content(body)

    with smtplib.SMTP_SSL(config.SMTP_HOST, config.SMTP_PORT) as s:
        s.login(sender, password)
        s.send_message(msg)