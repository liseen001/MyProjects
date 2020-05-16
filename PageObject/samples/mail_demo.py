#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: mail_demo.py
# @time: 2020/5/16 23:46
# @desc:发送邮件
import smtplib  #发送邮件时用的
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


smtp_server = 'smtp.qq.com'   #邮件服务地址
smtp_sender = '939856019@qq.com'  #发送邮箱
smtp_senderpassword = 'fvcxckimqbwvbfde'   #授权码
smtp_receiver='907864991@qq.com，939856019@qq.com'   #收件人，可写多人
smtp_cc='939856019@qq.com'   #抄送人
smtp_subject = '自动化测试报错（测试版）'   #邮件主题
smtp_body = '来自python邮件测试'  #邮件正文


msg = MIMEText(smtp_body,'html','utf-8')  #邮件信息的对象
msg['from'] = smtp_sender   #发送人
msg['to'] = smtp_receiver   #接收人
msg['Cc']=smtp_cc    #抄送人
msg['subject']=smtp_subject

#用引擎发送邮件
#导入smtplib，发送邮件时用的

smtp=smtplib.SMTP()    #做一个smtp对象
smtp.connect(smtp_server) #链接邮箱服务器，可加端口号，QQ邮箱端口号为465
smtp.login(user=smtp_sender,password=smtp_senderpassword)     #登录邮箱
smtp.sendmail(smtp_sender,smtp_receiver.split(',')+smtp_cc.split(','),msg.as_string())
