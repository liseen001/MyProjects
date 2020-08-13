#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: email_utils.py
# @time: 2020/8/13 22:15
# @desc: 封装邮件
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from API_TEST_FRAME.common.config_utils import conf

class EmailUtils():
    def __init__(self,smtp_body,smtp_attch_path=None):
        self.smtp_server = conf.smtp_server
        self.smtp_sender = conf.smtp_sender
        self.smtp_password = conf.smtp_password
        self.smtp_receiver = conf.smtp_receiver
        self.smtp_cc = conf.smtp_cc
        self.smtp_subject = conf.smtp_subject
        self.smtp_body = smtp_body  #邮件正文
        self.smtp_attch = smtp_attch_path  #附件路径

    def email_message_body(self):
        '''邮件消息体'''
        message = MIMEMultipart()
        message['from'] = self.smtp_sender
        message['to'] = self.smtp_receiver
        message['Cc'] = self.smtp_cc
        message['subject'] = self.smtp_subject
        message.attach( MIMEText(self.smtp_body,'html','utf8' ))
        if self.smtp_attch:
            attch_file =MIMEText( open(self.smtp_attch,'rb').read(),'base64','utf8' )
            attch_file['Content-Type']='application/octet-stream'
            attch_file.add_header( 'Content-Disposition','attachment',filename=('gbk','',os.path.basename(self.smtp_attch))) #处理附件路径
            message.attach( attch_file )
        return message

    def send_mail(self):
        '''发送邮件'''
        smtp = smtplib.SMTP()
        smtp.connect( self.smtp_server )
        smtp.login( user=self.smtp_sender,password=self.smtp_password )
        smtp.sendmail(self.smtp_sender,self.smtp_receiver.split(",")+self.smtp_cc.split(","),self.email_message_body().as_string())  #接收者为列表

if __name__ == '__main__':
    EmailUtils('<h3 align="center">自动化测试报告</h3>').send_mail()