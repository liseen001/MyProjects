#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import os
import configparser
import ast
import json

current_path=os.path.dirname(__file__)
config_path=os.path.join(current_path,'..','conf/config.ini')

class ConfigUtils():
    def __init__(self,config_path=config_path):
        self.__conf =configparser.ConfigParser()
        self.__conf.read(config_path,encoding='utf-8')

    @property
    def url(self):
        value=self.__conf.get('default','url')
        return value

    @property
    def host(self):
        value = self.__conf.get('default', 'host')
        return value

    @property
    def loginName(self):
        value=self.__conf.get('default','loginName')
        return value

    @property
    def password(self):
        value=self.__conf.get('default','password')
        return value




    @property
    def log_path(self):
        value=self.__conf.get('path','log_path')
        return value

    @property
    def log_level(self):
        value=int(self.__conf.get('log','log_level'))
        return value

    @property
    def report_path(self):
        value=self.__conf.get('path','report_path')
        return value



    #headerinfo
    @property
    def login_headerinfo(self):
        value=self.__conf.get('headerinfo','login_headerinfo')
        return value







conf=ConfigUtils()

if __name__=="__main__":
    print(conf.login_headerinfo)
    print(type(conf.login_headerinfo))