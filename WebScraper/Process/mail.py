import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from secret import passw
from datetime import datetime

timestamp = str(datetime.now().strftime("%d_%m_%Y_%H_%M"))
subject = "Team project report"
body = "This is automatically generated email which includes report for date : " + timestamp
sender_email = "team.project.email.notif@gmail.com"
recipients = ["mpetras2@vub.sk", "xmlyncek@stuba.sk", "xmikusa1@stuba.sk", "xkytosova@stuba.sk", "xklimko@stuba.sk",
              "xstevuliakova@stuba.sk", "xkrnacova@stuba.sk", "xstancikovaz@stuba.sk",
              "team.project.email.notif@gmail.com"]
password = passw

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = ", ".join(recipients)
message["Subject"] = subject

# Add body to email
message.attach(MIMEText(body, "plain"))

filename = "C:\\Users\\42194\\Desktop\\TP\\WebScraper\\Reports\\report.csv"  # In same directory as script

# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= report_" + timestamp + ".csv",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()


# Log in to server using secure context and send email
def send_mail_report():
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        try:
            server.ehlo()
            server.login(sender_email, password)
            server.sendmail(sender_email, recipients, text)
            server.quit()
        except():
            print("nieco je zle s mailom")
