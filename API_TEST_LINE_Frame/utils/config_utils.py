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
    @property
    def weixin_grant_type(self):
        lweixin_grant_type_value =self.conf.get('default','grant_type')
        return lweixin_grant_type_value
    @property
    def weixin_appid(self):
        weixin_appid_value = self.conf.get('default','appid')
        return weixin_appid_value
    @property
    def weixin_secret(self):
        weixin_secret_value = self.conf.get('default','secret')
        return weixin_secret_value
    @property
    def log_path(self):
        log_path_value = self.conf.get('default','log_path')
        return log_path_value
    @property
    def log_level(self):
        log_level_value = int(self.conf.get('default','log_level'))
        return log_level_value


conf = ConfigUtils()
if  __name__=="__main__":
    print(conf.log_path)
