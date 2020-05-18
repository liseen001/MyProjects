# -*- coding utf-8 -*-
import os
import configparser

current_path=os.path.dirname(__file__)
config_path=os.path.join(current_path,'../conf/config.ini')

class ConfigUtils(object):
    '''传入config_path参数'''
    def __init__(self,config_path=config_path):
        self.config_path=config_path
        '''创建配置文件对象'''
        self.conf=configparser.ConfigParser()
        '''设置读取文件的路径及编码格式'''
        self.conf.read(config_path,encoding='utf-8')

    @property
    def url(self):
        value=self.conf.get('default','url')
        return value

    @property
    def driver_path(self):
        driver_path_value=self.conf.get('default','driver_path')
        return driver_path_value

    @property
    def driver_name(self):
        driver_name_value=self.conf.get('default','driver_name')
        return driver_name_value

    '''默认等待时间'''
    @property
    def time_out(self):
        '''因为返回的等待时间为字符串，此处强制转换为浮点型'''
        value=float(self.conf.get('default','time_out'))
        return value

    @property
    def log_file_path(self):
        value=self.conf.get('default','log_file_path')
        return value


    '''元素信息表路径'''
    @property
    def element_infos_path(self):
        value=self.conf.get('default','element_infos_path')
        return value

#   禅道配置
    '''登录用户名'''
    @property
    def zengtao_username(self):
        value=self.conf.get('default','username')
        return value
    '''登录密码'''
    @property
    def zentao_password(self):
        value=self.conf.get('default','password')
        return value


    @property
    def screen_shoot_path(self):
        screen_shoot_path_value=self.conf.get('default','screen_shot_path')
        return screen_shoot_path_value

    @property
    def report_path(self):
        report_path_value=self.conf.get('default', 'report_path')
        return report_path_value

    '''默认登录用户名'''
    @property
    def default_username(self):
        value = self.conf.get('default', 'default_username')
        return value

    '''默认登录密码'''
    @property
    def default_password(self):
        value = self.conf.get('default', 'default_password')
        return value

    '''定义的新的log路径'''
    @property
    def log_path(self):
        value=self.conf.get('default','log_path')
        return value

    '''日志级别'''
    @property
    def log_level(self):
        log_level_value=int(self.conf.get('default','log_level'))
        return log_level_value
    @property
    def testdata_path(self):
        testdata_path_value=self.conf.get('default','testdata_path')
        return testdata_path_value
    @property
    def case_path(self):
        case_path_value = self.conf.get('default', 'case_path')
        return case_path_value



    #邮件
    @property
    def smtp_server(self):  #邮件服务器
        smtp_server_value=self.conf.get('email', 'smtp_server')
        return smtp_server_value

    @property
    def smtp_sender(self):  #邮件发送人
        smtp_sender_value=self.conf.get('email', 'smtp_sender')
        return smtp_sender_value

    @property
    def smtp_password(self):  #邮件授权码
        smtp_password_value=self.conf.get('email', 'smtp_password')
        return smtp_password_value

    @property
    def smtp_receiver(self):  #邮件接收人
        smtp_receiver_value=self.conf.get('email', 'smtp_receiver')
        return smtp_receiver_value

    @property
    def smtp_cc(self):  #邮件抄送人
        smtp_cc_value=self.conf.get('email', 'smtp_cc')
        return smtp_cc_value

    @property
    def smtp_subject(self):  #邮件主题
        smtp_subject_value = self.conf.get('email', 'smtp_subject')
        return smtp_subject_value



conf=ConfigUtils()
if __name__=="__main__":
    print(conf.case_path,conf.report_path)
