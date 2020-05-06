# --*utf-8*--
import os
import configparser
curren_path=os.path.dirname(__file__)
config_path=os.path.join(curren_path,'../conf/config.ini')

class ConfigUtils:
    '''传入config_path参数'''
    def __init__(self,__config_path=config_path):
        self.__config_path=config_path
        '''创建配置文件对象'''
        self.conf=configparser.ConfigParser()
        '''文件读取配置的路径及编码格式'''
        self.conf.read(self.__config_path,encoding='utf-8')

    '''创建读取配置文件方法，需要传入默认值selection和option,其他模块可以通过调用这个方法传入不同的配置文件的值进行操作，也可以如下面一样，把配置文件的每个配置都定义一个方法'''
    def read_ini(self,selection,option):
        try:
            value=self.conf.get(selection,option)
        except Exception as e:
            print('系统错误'%str(e))
        return value
    '''定义获取禅道地址配置的方法'''
    def get_zend_path(self):
        try:
            value=self.conf.get('default','zend_path')
        except Exception as e:
            print('系统错误'%str(e))
        return value
    '''定义获取配置文件中禅道登录名的方法'''
    def get_username(self):
        value=self.conf.get('default','username')
        return value
    '''定义获取配置文件中禅道登录面的方法'''
    def get_password(self):
        value=self.conf.get('default','password')
        return value

    '''定义获取配置文件中火狐驱动的方法'''
    '''构造方法调用的时候不用加括号'''
    @property
    def get_foxfire_path(self):
        value=self.conf.get('default','foxdriver_path')
        return value
    @property
    def get_chrome_driver(self):
        value=self.conf.get('default','chromedriver_path')
        return value

    '''定义获取配置文件中日志文件路径的方法'''
    def get_logs_path(self):
        value=self.conf.get('default','log_path')
        return value

    '''定义获取配置文件中表格存放路径的方法'''
    def get_excel_path(self):
        value=self.conf.get('default','excel_path')
        return value

    '''定义获取配置文件中元素信息存放路径的方法'''
    def get_element_infos_excel_path(self):
        value=self.conf.get('default','element_infos_excel')
        return value

    '''获取默认默认浏览器驱动的方法'''
    @property
    def get_driver_name(self):
        value=self.conf.get('default','driver_name')
        return value

conf=ConfigUtils()

if __name__=="__main__":
    print(conf.get_password())
    print(conf.get_driver_name)


