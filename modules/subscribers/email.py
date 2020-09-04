from socket import gaierror
import smtplib

def sendEmail(adressTo, name, adressFrom, password):
    print(f"Sending email to {adressTo} from {adressFrom}")
    port = 587
    smtp_server = "smtp.gmail.com"
    login = adressFrom

    message = f"""\
    Subject: Hi Gmail!
    To: {adressTo}
    From: {adressFrom}

    This is my first message with Python."""

    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(login, password)
            server.sendmail(adressFrom, adressTo, message)

        print('Sent')
    except (gaierror, ConnectionRefusedError):
        print('Failed to connect to the server. Bad connection settings?')
    except smtplib.SMTPServerDisconnected:
        print('Failed to connect to the server. Wrong user/password?')
    except smtplib.SMTPException as e:
        print('SMTP error occurred: ' + str(e))