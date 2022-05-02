import smtplib
import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail():
    port = 2525
    smtp_server = "smtp.mailtrap.io"
    login = "45b4b3fe8a1fef"  # Mailtrap login
    password = "d738990a10867e"  # Mailtrap password

    subject = "Crypto Datasheet"
    sender_email = "mailtrap@example.com"
    receiver_email = "new@example.com"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Email body
    now = datetime.datetime.now()
    current_date = now.strftime("%Y-%m-%d %H:%M:%S")
    body = "Here you have a datasheet with the most important infos for bitcoin. This datasheet was created on: %s" % current_date
    message.attach(MIMEText(body, "plain"))

    filename = "datasheet/Crypto Datasheet.pdf"
    # Open PDF file in binary mode

    # We assume that the file is in the directory where you run your Python script from
    with open(filename, "rb") as attachment:
        # The content type "application/octet-stream" means that a MIME attachment is a binary file
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode to base64
    encoders.encode_base64(part)

    # Add header
    part.add_header(
        "Content-Disposition",
        "attachment; filename=Crypto Datasheet.pdf",
    )

    # Add attachment to your message and convert it to string
    message.attach(part)
    text = message.as_string()

    # send your email
    with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
        server.login(login, password)
        server.sendmail(
            sender_email, receiver_email, text
        )
