# -*- coding utf-8 -*-
import os
import configparser
current_path=os.path.dirname(__file__)
config_path=os.path.join(current_path,'../conf/config.ini')
class CongfigUtils:
    def __init__(self,config_path=config_path):
        '''定义配置文件路径'''
        self.config_path=config_path
        '''创建conf对象，引用配置文件内置方法'''
        self.conf=configparser.ConfigParser()
        '''配置文件读取的路径与读取格式'''
        self.conf.read(self.config_path,encoding='utf-8')

        '''创造读取配置文件方法，传入selection和option作为默认参数'''
    def read_ini(self,selection,option):
        '''引入异常处理'''
        try:
            value=self.conf.get(selection,option)
        except Exception as e:
            print('系统错误'%str(e))
            '''函数返回值为value'''
            return value

    '''创建获取项目url地址的方法'''
    def get_music_url(self):
        value=self.conf.get('default','music_url')
        return value
    '''创建获取表格路径的方法'''
    def get_excel_path(self):
        value=self.conf.get('default','excel_path')
        return value

    '''创建获取打印日志输入路径的方法'''
    def get_logs_path(self):
        value=self.conf.get('default','logs_path')
        return value

    '''创建获取driver驱动路径的方法'''
    def get_foxfire_path(self):
        value=self.conf.get('default','foxfire_path')
        return value
    '''获取音乐软件登录账户名'''
    def get_music_login_username(self):
        value=self.conf.get('default','username')
        return value
    '''获取音乐软件登录密码'''
    def get_music_login_password(self):
        value=self.conf.get('default','password')
        return value
conf=CongfigUtils()

if __name__=="__main__":
    print(conf.get_music_url())