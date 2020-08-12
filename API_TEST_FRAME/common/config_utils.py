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
        '''主机地址'''
        url_value = self.conf.get('default','url')
        return url_value

    @property
    def case_data_path(self):
        '''测试数据存放路径'''
        case_data_path_value = self.conf.get('path','case_data_path')
        return case_data_path_value
    @property
    def log_path(self):
        '''日志输出路径'''
        log_path_value = self.conf.get('path','log_path')
        return log_path_value
    @property
    def log_level(self):
        '''日志级别'''
        log_level_value = int(self.conf.get('log','log_level'))
        return log_level_value

    @property
    def report_path(self):
        '''测试报告存放路径'''
        report_path_value = self.conf.get( 'path','report_path' )
        return report_path_value

    @property
    def case_path(self):
        '''测试用例存放路径'''
        case_path_value = self.conf.get( 'path','case_path' )
        return case_path_value

conf = ConfigUtils()

if __name__=="__main__":
    print( conf.case_path )

