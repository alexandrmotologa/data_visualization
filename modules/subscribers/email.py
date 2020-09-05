from socket import gaierror
import smtplib
from email.message import EmailMessage

def sendEmail(adressTo, name, adressFrom, password):
    print(f"Sending email to {adressTo} from {adressFrom}")
    port = 587
    smtp_server = "smtp.gmail.com"
    login = adressFrom
    msg = EmailMessage()
    msg['Subject'] = "asdasdasdasd"
    msg['From'] = f"<{adressFrom}>"
    msg['To'] = f" <{adressTo}>"
    msg.set_content("This is my first message with Python.")


    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(login, password)
            server.send_message(msg)


        print('Sent')
    except (gaierror, ConnectionRefusedError):
        print('Failed to connect to the server. Bad connection settings?')
    except smtplib.SMTPServerDisconnected:
        print('Failed to connect to the server. Wrong user/password?')
    except smtplib.SMTPException as e:
        print('SMTP error occurred: ' + str(e))
