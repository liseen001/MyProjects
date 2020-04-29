# --*utf-8*--
import os
import configparser
curren_path=os.path.dirname(__file__)
config_path=os.path.join(curren_path,'../conf/config.ini')

class ConfigUtils:
    def __init__(self,config_path=config_path):
        self.config_path=config_path
        self.conf=configparser.ConfigParser()
        self.conf.read(self.config_path,encoding='utf-8')


    def read_ini(self,selection,option):
        try:
            value=self.conf.get(selection,option)
        except Exception as e:
            print('系统错误'%str(e))
        return value

    def get_zend_path(self):
        try:
            value=self.conf.get('default','zend_path')
        except Exception as e:
            print('系统错误'%str(e))
        return value

    def get_username(self):
        value=self.conf.get('default','username')
        return value

    def get_password(self):
        value=self.conf.get('default','password')
        return value

    def get_foxfire_path(self):
        value=self.conf.get('default','foxdriver_path')
        return value

conf=ConfigUtils()

if __name__=="__main__":
    print(conf.get_password())

