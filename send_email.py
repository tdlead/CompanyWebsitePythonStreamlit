import smtplib
import ssl


def send_email(message):
    HOST = "smtp.gmail.com"
    PORT = 465
    USERNAME = 'dubineanschi.tatiana@gmail.com'
    PASSWORD = "yqzg jnnm klod uozq"
    receiver = 'dubineanschi.tatiana@gmail.com'
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host=HOST, port=PORT, context=context) as server:
        server.login(USERNAME, PASSWORD)
        server.sendmail(USERNAME, receiver, msg=message)

