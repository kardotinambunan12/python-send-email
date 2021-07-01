# import email
from email.mime import text
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from sys import path

email_pengirim = input('masukkan email pengirim :')
email_penerima = input('masukkan email penerima :')
title_msg = input('masukkan title pesan :')
isi_msg = input('masukkan isi pesan :')
password_pengirim = input('masukkan password pengirim :')

msg = MIMEMultipart()
msg['From'] = email_penerima
msg['To'] = email_pengirim
msg['Subject'] = title_msg
msg["Bcc"] = email_penerima 

body = isi_msg
msg.attach(MIMEText(body, 'plain'))

# lampirkan sesuai dengan nama filename dengan nama file attachment

file_name = input('masukkan nama file :')
attachment = open('./file/file.txt', 'rb')
part = MIMEBase("application", "octet-stream")

part.set_payload((attachment).read())
encoders.encode_base64(part)

part.add_header("Content-Disposition", f"attachment; filename= {file_name}",
)
# part.add_header('Content-Disposition',"attachment; file_name=%s" % file_name)

msg.attach(path)


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_pengirim, password_pengirim)
text= msg.as_string()
server.sendmail(email_pengirim, email_penerima, text)

server.quit()