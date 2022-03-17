from smtplib import SMTP
from email.mime.text import MIMEText
from secrets import username, password

def send_mail(email, height, weight):
    sender_email=username
    sender_password=password
    receiver_email=email

    subject="Your BMI"
    content=f"Hi! \n\nYour BMI is <strong>{height/weight}</strong>"

    msg=MIMEText(content, 'html')

    msg['Subject']=subject
    msg['To']=receiver_email
    msg['From']=sender_email

    gmail=SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(sender_email, sender_password)
    gmail.send_message(msg)