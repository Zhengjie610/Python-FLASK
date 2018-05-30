#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = 'chenzhengjie168@gmail.com'
my_pass = '189xsb7D'
my_user = 'chenzhengjie168@gmail.com'
def mail():
    ret = True
    try:
        msg = MIMEText('This is system generated Email', 'plain', 'utf-8')
        msg['From'] = formataddr(["Smart Home System", my_sender])
        msg['To'] = formataddr(["User", my_user])
        msg['Subject'] = "Smart Home System"

        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(my_sender, my_pass)
        server.sendmail(my_sender, [my_user, ], msg.as_string())
        server.quit()
    except Exception:
        ret = False
    return ret


ret = mail()
if ret:
    print("Email was Sent")
else:
    print("Failed")
