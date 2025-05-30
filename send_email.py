import smtplib, os, ssl



def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = os.getenv("PORTFOLIO_MAIL")
    password = os.getenv("PASSWORD_FOR_PORTFOLIO_APP_MAIL")
    receiver = os.getenv("PORTFOLIO_MAIL")
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

