import smtplib, ssl
import os;

def send_mail(message):
    host = 'smtp.gmail.com'
    port = 465
    user = 'maheshbharath69@gmail.com'
    #password = os.getenv("PASSWORD")
    password = 'ofgj xezw xxfj oklo'
    receiver = 'maheshbharath69@gmail.com'
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user, password)
        server.sendmail(user, receiver, message)


