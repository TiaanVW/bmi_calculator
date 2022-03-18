from smtplib import SMTP
from email.mime.text import MIMEText
from secret_info import password, username

def send_mail(email, height, weight):
    receiver_email=email

    subject="Your BMI"
    content=f"Hi! \n\nYour BMI is <strong>{height/weight}</strong>"

    msg=MIMEText(content, 'html')

    msg['Subject']=subject
    msg['To']=receiver_email
    msg['From']=username

    gmail=SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.ehlo()
    gmail.login(username, password)
    gmail.send_message(msg)