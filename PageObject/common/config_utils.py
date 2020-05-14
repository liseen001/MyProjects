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

    '''创建获取配置文件的通用方法'''
    def read_ini(self,selection,option):
        value=self.conf.get(selection,option)
        return value
    '''构造方法，其他调用这个方法的时候不需要传括号，属性当方法用，配置文件获取禅道默认配置的路径'''
    @property
    def zend_path(self):
        value=self.conf.get('default','zend_path')
        return value

    @property
    def log_file_path(self):
        value=self.conf.get('default','log_file_path')
        return value
    '''配置获取默认浏览器的方法'''
    @property
    def driver_name(self):
        value=self.conf.get('default','driver_path')
        return value

    '''元素信息表路径'''
    @property
    def element_infos_path(self):
        value=self.conf.get('default','element_infos_path')
        return value

    '''默认等待时间'''
    @property
    def time_out(self):
        '''因为返回的等待时间为字符串，此处强制转换为浮点型'''
        value=float(self.conf.get('default','time_out'))
        return value
    '''谷歌驱动读取'''
    @property
    def chromedriver_path(self):
        value=self.conf.get('default','chromedriver_path')
        return value
    '''火狐驱动读取'''
    @property
    def firefoxdriver_path(self):
        value=self.conf.get('default','firefoxdriver_path')
        return value
    '''获取默认驱动'''
    @property
    def default_driver_name(self):
        value=self.conf.get('default','driver_name')
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


conf=ConfigUtils()

if __name__=="__main__":
    print(conf.log_level)
