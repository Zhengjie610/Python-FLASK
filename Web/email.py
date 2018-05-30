#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = 'czj19930610@qq.com'  # 发件人邮箱账号
my_pass = 'uhmvbjysugpfcahc'  # 发件人邮箱密码
my_user = 'chenzhengjie168@gmail.com'  # 收件人邮箱账号，我这边发送给自己
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
