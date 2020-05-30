#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:封装配置文件方便后面调用
import os
import configparser

current_path=os.path.dirname(__file__)
config_path=os.path.join(current_path,'../conf/config.ini')

class ConfigUtils(object):
    def __init__(self,config_path=config_path):
        self.config_path=config_path
        self.conf=configparser.ConfigParser()
        self.conf.read(config_path,encoding='utf-8')
    @property                             #页面路径
    def music_url(self):
        music_url_value=self.conf.get('default','music_url')
        return music_url_value
    @property                              #登录账号
    def username(self):
        username_value=self.conf.get('default','username')
        return username_value
    @property                              #登录密码
    def password(self):
        password_value=self.conf.get('default','password')
        return password_value

    @property                              #日志路径
    def log_path(self):
        log_path_value=self.conf.get('default','log_path')
        return log_path_value
    @property                              #设置日志级别
    def log_level(self):
        log_level_value=int(self.conf.get('default','log_level'))
        return log_level_value
    @property                              #webdriver存放路径
    def driver_path(self):
        driver_path_value=self.conf.get('default','driver_path')
        return driver_path_value
    @property                             #默认的webdriver配置
    def driver_name(self):
        driver_name_value=self.conf.get('default','driver_name')
        return driver_name_value
    
    @property                             #测试报告地址
    def report_path(self):
        report_path_value=self.conf.get('default','report_path')
        return report_path_value
    
    @property                            #默认超时时间
    def time_out(self):
        time_out_value=float(self.conf.get('default','time_out'))
        return time_out_value
    @property                            #截图存放路径
    def screen_shot_path(self):
        screen_shot_path_value = self.conf.get('default','screen_shot_path')
        return screen_shot_path_value
    @property                            #元素信息存放路径
    def element_infos_path(self):
        element_infos_path_value = self.conf.get('default','element_infos_path')
        return element_infos_path_value

    @property                           #测试配置数据
    def testdata_path(self):
        testdata_path_value = self.conf.get('default','testdata_path')
        return testdata_path_value


conf=ConfigUtils()
if __name__=="__main__":
    print(conf.log_level)

