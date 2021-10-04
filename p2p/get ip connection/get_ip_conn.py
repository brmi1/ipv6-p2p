# !для использования требуется разрешить доступ небезопасным приложениям!
from smtplib import SMTP_SSL
from imap_tools import MailBox, A
from time import sleep
from get_my_ip import get_my_ip

login = "" # адрес для обмена ip, должен быть общим у обоих клиентов
password = "" # пароль от почты
address = get_my_ip()
timeout = 2.5

to = login
email_text = f"""\
Subject: IP

{address}"""

smtp_server = SMTP_SSL('smtp.gmail.com', 465)
smtp_server.login(login, password)
smtp_server.sendmail(login, to, email_text)

conn_ip = ""
while conn_ip == "":
    mail = MailBox('imap.gmail.com')
    mail.login(login, password, 'INBOX')
    for msg in mail.fetch(A(subject="IP")):
        if msg.text.replace("\r\n","") != address:
            conn_ip = msg.text.replace("\r\n","")
    sleep(timeout)

print(f"Connection ip {conn_ip}")

for uid in mail.uids(A(subject="IP")):
    mail.delete(uid)
