
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import SMTP_EMAIL, SMTP_PASSWORD, SMTP_NAME
from string import Template

def load_template(path='emailer/template.html'):
    with open(path, 'r', encoding='utf-8') as f:
        return Template(f.read())

def send_email(to_email, to_name):
    msg = MIMEMultipart("alternative")
    msg['Subject'] = "Une solution moderne pour votre association"
    msg['From'] = f"{SMTP_NAME} <{SMTP_EMAIL}>"
    msg['To'] = to_email

    template = load_template()
    html_content = template.substitute(name=to_name, from_name=SMTP_NAME)
    msg.attach(MIMEText(html_content, 'html'))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SMTP_EMAIL, SMTP_PASSWORD)
            server.sendmail(SMTP_EMAIL, to_email, msg.as_string())
        print(f"[✓] Email envoyé à {to_email}")
    except Exception as e:
        print(f"[!] Échec d’envoi à {to_email} : {e}")
