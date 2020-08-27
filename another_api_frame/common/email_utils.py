#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc: 封装邮件
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from common.config_utils import conf
from common.nblog_utils import logger

class EmailUtils():
    def __init__(self,smtp_body,smtp_attach_path=None):
        self.smtp_server = conf.smtp_server
        self.smtp_sender = conf.smtp_sender
        self.smtp_password = conf.smtp_password
        self.smtp_receiver = conf.smtp_receiver
        self.smtp_cc = conf.smtp_cc
        self.smtp_subject = conf.smtp_subject
        self.smtp_body = smtp_body   #邮件正文
        self.smtp_attach = smtp_attach_path  #附件路径


    def emial_message_body(self):
        '''邮件体消息'''
        message = MIMEMultipart()
        message['from'] = self.smtp_sender
        message['to'] = self.smtp_receiver
        message['Cc'] = self.smtp_cc
        message['subject'] = self.smtp_subject
        message.attach( MIMEText( self.smtp_body,'html','utf-8' ) )
        if self.smtp_attach:
            attch_file = MIMEText( open( self.smtp_attach,'rb' ).read(),'base64','utf-8' )
            attch_file['Content-Type'] = 'application/octet-stream'
            attch_file.add_header( 'Content-Disposition','attachment',filename=('gbk','',os.path.basename( self.smtp_attach )) )  #处理附件路径
            message.attach( attch_file )
        return message

    def send_email(self):
        '''发送邮件'''
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.smtp_server)
            smtp.login(user=self.smtp_sender, password=self.smtp_password)
            smtp.sendmail(self.smtp_sender, self.smtp_receiver.split(",") + self.smtp_cc.split(","),self.emial_message_body().as_string())  # 接收者作为列表
            logger.info('发送邮件成功')
        except Exception as e:
            logger.error('邮件发送失败,失败的原因是：{}'.format( e.__str__() ))

if __name__ == '__main__':
    EmailUtils('<h3 align="center">自动化测试报告</h3>').send_email()
