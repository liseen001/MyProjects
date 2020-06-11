#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc: 配置文件封装

import os
import configparser

current_path=os.path.dirname(__file__)
config_path=os.path.join(current_path,'../conf/config.ini')


class ConfigUtils(object):
    def __init__(self,config_path=config_path):
        self.config_path=config_path
        self.conf=configparser.ConfigParser()
        self.conf.read(config_path,encoding='utf-8')

    @property  #主机地址
    def hosts_url(self):
        hosts_url_value =self.conf.get('default','hosts')
        return hosts_url_value

    @property  #测试报告存放路径
    def report_parh(self):
        report_path_value = self.conf.get('default', 'report_path')
        return report_path_value
    @property  #登录账号
    def login_username(self):
        login_username_value =self.conf.get('default','username')
        return login_username_value
    @property
    def login_password(self):
        login_password_value = self.conf.get('default','password')
        return login_password_value


conf = ConfigUtils()
if  __name__=="__main__":
    print(conf.report_parh)
