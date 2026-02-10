import smtplib
from email.message import EmailMessage
from secrets import sender_email, app_password, receiver_email
 
 #Email details
def send_email(receiver_email,subject,content):

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    msg.set_content(content)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, app_password)
        server.send_message(msg)

    print("Email sent successfully")

send_email(receiver_email="4mh23cs158@gmail.com",subject="Test mail from Python",content="Hello! how are you.")