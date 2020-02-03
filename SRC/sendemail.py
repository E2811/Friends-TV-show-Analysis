import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass

def SendEmail(receiver_email):
    subject = "Friends TV show report"
    body = "This is an email with attachment of a PDF Friends report"
    sender_email = "ironhackeli@gmail.com"
    password = getpass.getpass("Type your password and press enter:")

    # Creating message.
    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = receiver_email
    # Add body to email
    message.attach(MIMEText(body, "plain"))
    filename = "OUTPUT/FriendsTV.pdf"
    # Open PDF file 
    with open("OUTPUT/FriendsTV.pdf", "rb") as attachment:
        # Add file aenas application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)
    encoders.encode_base64(part)
    part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",)

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
    print('Email sent!')