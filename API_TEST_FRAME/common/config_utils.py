#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:  封装日志
import os
import configparser

current_path =os.path.dirname(__file__)
config_path = os.path.join(current_path,'..','conf/config.ini')

class ConfigUtils():
    def __init__(self,config_path=config_path):
        self.conf= configparser.ConfigParser()
        self.conf.read(config_path,encoding='utf-8')

    @property
    def url(self):
        url_value = self.conf.get('default','url')
        return url_value

    @property
    def case_data_path(self):
        case_data_path_value = self.conf.get('path','case_date_path')
        return case_data_path_value
    @property
    def log_path(self):
        log_path_value = self.conf.get('path','log_path')
        return log_path_value
    @property
    def log_level(self):
        log_level_value = self.conf.get('log','log_level')
        return log_level_value

conf = ConfigUtils()

if __name__=="__main__":
    print(conf.case_date_path)
