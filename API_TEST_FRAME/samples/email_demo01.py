#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: email_demo01.py
# @time: 2020/8/13 21:21
# @desc:  发送邮件普通版
import smtplib
from email.mime.text import MIMEText
body_str='''
<h3 align="center">自动化测试报告</h3>
<table border="2" align="center" width="50%",height="400">
<tr><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td></tr>
</table>
'''
msg = MIMEText(body_str,'html','utf8')  #邮件信息对象
msg[ 'from' ] = '939856019@qq.com'  #发送人
msg['to'] = '939856019@qq.com'      #接收人
msg['Cc'] = ''                      #抄送人
msg['subject'] = '自动化测试报告_demo'  #邮件主题

smtp = smtplib.SMTP() #创建SMTP对象
smtp.connect( 'smtp.qq.com' ) #连接smtp主机
smtp.login( user='939856019@qq.com',password='fvcxckimqbwvbfde' ) #邮箱登录
smtp.sendmail( '939856019@qq.com',['939856019@qq.com'],msg.as_string() )  #发送邮件,发送人及接收人，接收人为列表

