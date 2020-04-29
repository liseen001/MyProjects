# --*utf-8*--
import os
import configparser

current_path=os.path.dirname(__file__)
config_path=os.path.join(current_path,'../conf/config.ini')

class ConfigUtils:
    def __init__(self):
        self.config_path=config_path
        self.conf=configparser.ConfigParser()
        self.conf.read(self.config_path,encoding='utf-8')


    def read_ini(self,selection,option):
        value=self.conf.get(selection,option)
        return value

    def get_log_path(self):
        value=self.read_ini('default','log_path')
        return value

    def get_excel_path(self):
        try:
            value=self.read_ini('default','excel_path')
        except KeyError as e:
            print('找不到excel_path配置信息')
        return value

conf=ConfigUtils()

if __name__=="__main__":
    value=conf.get_excel_path()
    value_1=conf.get_log_path()
    print(value)
    print(value_1)