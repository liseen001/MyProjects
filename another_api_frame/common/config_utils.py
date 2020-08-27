#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc: 封装配置文件类
import os
import configparser

current_path = os.path.dirname(__file__)
configfile_path = os.path.join( current_path,'..','conf/config.ini' )
class ConfigUtils():
    def __init__(self,configfile_path = configfile_path):
        self.configfile_path = configfile_path
        # self.__conf = configparser.ConfigParser()
        self.__conf = configparser.RawConfigParser()
        self.__conf.read( configfile_path,encoding='utf8' )




    '''默认配置项'''
    @property
    def host(self):
        '''获取主机地址'''
        host_value = self.__conf.get('default','host')
        return host_value


    '''path路径配置项'''
    @property
    def case_data_path(self):
        '''测试数据存放路径'''
        case_data_path_value = self.__conf.get( 'path','case_data_path' )
        return case_data_path_value
    @property
    def log_path(self):
        '''运行日志存放路径'''
        log_path_value = self.__conf.get( 'path','log_path' )
        return log_path_value
    @property
    def report_path(self):
        '''测试报告存放路径'''
        report_path_value = self.__conf.get( 'path','report_path' )
        return  report_path_value
    @property
    def case_path(self):
        '''测试用例存放路径'''
        case_path_value = self.__conf.get( 'path','case_path' )
        return case_path_value


    '''日志配置项'''
    @property
    def log_name(self):
        '''获取日志名称'''
        log_name_value = self.__conf.get( 'log','log_name' )
        return log_name_value
    @property
    def logger_filename(self):
        '''日志输出日期时间格式'''
        logger_filename_value = self.__conf.get('time','logger_filename')
        return logger_filename_value


    '''邮件配置项'''
    @property
    def smtp_server(self):
        '''邮件服务器'''
        smtp_server_value = self.__conf.get( 'mail','smtp_server' )
        return smtp_server_value
    @property
    def smtp_password(self):
        '''授权码'''
        smtp_password_value = self.__conf.get( 'mail','smtp_password' )
        return smtp_password_value
    @property
    def smtp_sender(self):
        '''邮件发送人'''
        smtp_sender_value = self.__conf.get( 'mail','smtp_sender' )
        return smtp_sender_value
    @property
    def smtp_receiver(self):
        '''邮件接收人'''
        smtp_receiver_value = self.__conf.get( 'mail','smtp_receiver' )
        return smtp_receiver_value
    @property
    def smtp_cc(self):
        '''邮件抄送人'''
        smtp_cc_value = self.__conf.get( 'mail','smtp_cc' )
        return smtp_cc_value
    @property
    def smtp_subject(self):
        '''邮件主题'''
        smtp_subject_value = self.__conf.get( 'mail','smtp_subject' )
        return smtp_subject_value


    '''数据库配置项'''
    @property
    def mysql_host(self):
        '''数据库地址'''
        mysql_host_value = self.__conf.get( 'mysql','mysql_host' )
        return mysql_host_value
    @property
    def mysql_port(self):
        '''数据库端口'''
        mysql_port_value = self.__conf.get('mysql','mysql_port')
        return mysql_port_value
    @property
    def msql_loginname(self):
        '''数据库登录账号'''
        msql_loginname_value = self.__conf.get( 'mysql','msql_loginname' )
        return msql_loginname_value
    @property
    def mysql_password(self):
        '''数据库密码'''
        mysql_password_value = self.__conf.get( 'mysql','mysql_password' )
        return mysql_password_value


    '''excel配置项'''
    @property
    def sheet_name(self):
        '''测试数据读取sheet名'''
        sheet_name_value = self.__conf.get( 'excel','sheet_name' )
        return sheet_name_value

    '''测试报告配置项'''
    @property
    def report_title(self):
        '''测试报告标题'''
        report_title_value = self.__conf.get('report', 'report_title')
        return report_title_value
    @property
    def report_description(self):
        '''测试报告描述'''
        report_description_value = self.__conf.get('report', 'report_description')
        return report_description_value
    @property
    def report_tester(self):
        '''测试报告开发者'''
        report_tester_value = self.__conf.get('report', 'report_tester')
        return report_tester_value




conf = ConfigUtils()
if __name__ == '__main__':
    print( conf.report_tester )