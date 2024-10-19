import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# run it on python 3.8 and above
sender_email = "example@gmail.com"
reciever_email = "example1@gmail.com"
password ="12345"
subject = 'Hello, from Python'
body = 'This is a for learning purposes'

msg =MIMEMultipart()
msg['From'] =sender_email
msg['To']= reciever_email
msg['Subject'] = subject

msg.attach(MIMEText(body, 'plain'))

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, reciever_email, msg.as_string())
    print('Email send succesfully.')
except smtplib.SMTPAuthenticationError:
    print('Authentication error: Check your email and password.')
except smtplib.SMTPConnectError:
    print('Connection error: Unable to connect to the email server.')
except Exception as e:
    print(f'An error occurred: {e}')
finally:
    server.quit()      