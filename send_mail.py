import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def guimail():
    email_user = 'nhnam97@gmail.com'
    email_send = 'maichikhuong98@gmail.com'
    subject = 'de cuong nghien cuu khoa hoc'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    body = 'Hi there'
    msg.attach(MIMEText(body,'plain'))

    filename = 'NHN_NCKH.doc'
    attachment = open(filename,'rb')

    part = MIMEBase('application','octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition','attachment;filename= '+filename)

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,'nhomaimotnguoi')

    #message = 'hom nay la ngay 05/01/2018. File nay duoc gui tu Python. Awsome!!!'
    server.sendmail(email_user,email_send,text)
    server.quit()
for i in range(10):
    guimail()
