import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username = "bayram031105@gmail.com"
password = "karmkojvqxiatbbm"


receiver = "aliyevbayram08@gmail.com"
context = ssl.create_default_context()

message = """
Putinin bajisini
"""

with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
