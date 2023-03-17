import smtplib
import os
from email.mime.text import MIMEText



email_login = "dronbrother@yandex.ru"
email_password = "12323212t"
email_host = "smtp.yandex.ru" #SSL
email_port = 465

mail_to = "andreykae28@gmail.com"
print("[OK] Get data")

server = smtplib.SMTP("smtp.yandex.ru", 587, timeout=10) #SMTP() для gmail
server.set_debuglevel(1)

print("[OK] Server connection")

try:
    with open("email_template.html") as file:
        template = file.read()
except IOError:
    print("[ERROR] Email template dont exist")
    exit()


try:
    server.starttls()
    server.login(email_login, email_password)
    print("[OK] login auth ")
    
    msg = MIMEText(template, "html")
    msg["Subject"] = "Инцидент"
    msg["From"] = email_login
    msg["To"] = mail_to

    server.sendmail(email_login, mail_to, msg.as_string())
    print("[OK] Send mail ")
except Exception as e:
    print(f"[EMAIL ERROR]\n{e}\n[END EMAIL ERROR]")

