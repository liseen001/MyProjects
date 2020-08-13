#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: email_demo01.py
# @time: 2020/8/13 21:21
# @desc:  发送邮件带附件
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart()  #邮件信息对象
msg.attach( MIMEText('<h3 align="center">自动化测试报告</h3>','html','utf8') )


msg[ 'from' ] = '939856019@qq.com'  #发送人
msg['to'] = '939856019@qq.com'      #接收人
msg['Cc'] = ''                      #抄送人
msg['subject'] = '自动化测试报告_demo'  #邮件主题

html_path = os.path.join( os.path.dirname(__file__),'..','test_reports/' )

attach_file = MIMEText( open('1.txt','rb').read(),'base64','utf8' )
attach_file['Content-Type'] = 'application/octet-stream'
attach_file['Content-Disposition'] = 'attachment; filename="test.txt"'  #filename必须为英文，否则会出错
msg.attach( attach_file )



smtp = smtplib.SMTP() #创建SMTP对象
smtp.connect( 'smtp.qq.com' ) #连接smtp主机
smtp.login( user='939856019@qq.com',password='fvcxckimqbwvbfde' ) #邮箱登录
smtp.sendmail( '939856019@qq.com',['939856019@qq.com'],msg.as_string() )  #发送邮件,发送人及接收人，接收人为列表

