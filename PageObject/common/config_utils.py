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

    '''截图路径封装'''
    @property
    def screen_shoot_path(self):
        value=self.conf.get('default','screen_shot_path')
        return value
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
        case_path_value = self.cfg.get('default', 'case_path')
        return case_path_value


conf=ConfigUtils()
if __name__=="__main__":
    print(conf.driver_name,conf.driver_path)
