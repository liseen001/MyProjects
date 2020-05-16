# -*- coding utf-8 -*-
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PageObject.common.config_utils import conf
from PageObject.common.log_utils import logutils

current_path = os.path.abspath(os.path.dirname(__file__))
dri_path = os.path.join( current_path,'..', conf.driver_path )

class Browser(object):
    def __init__(self,driver_path= dri_path,driver_name= conf.driver_name):
        self.__driver_path=driver_path
        self.__driver_name=driver_name

    '''获取配置文件中默认配置浏览器的方法'''
    def get_default_driver(self):
        if self.__driver_name.lower() == 'chrome':
            return self.__get_chrome_driver
        elif self.__driver_name.lower() == 'firefox':
            return self.__get_firefox_driver
        elif self.__driver_name.lower() == 'edge':
            return self.__get_edge_driver
    @property
    def __get_chrome_driver(self):
        chrome_options = Options()
        chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_argument('lang=zh_CN.UTF-8')  #设置默认编码为utf-8
        chrome_options.add_experimental_option('useAutomationExtension', False)#取消chrome受自动控制提示
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])#取消chrome受自动控制提示
        chrome_driver_path = os.path.join(self.__driver_path, 'chromedriver')
        driver = webdriver.Chrome(options=chrome_options,executable_path=chrome_driver_path)
        logutils.info('初始化并启动谷歌浏览器')
        return driver

    @property
    def __get_firefox_driver(self):
        firefox_driver_path = os.path.join(self.__driver_path, 'geckodriver')
        driver = webdriver.Firefox(executable_path=firefox_driver_path)
        return driver

    @property
    def __get_edge_driver(self):
        edge_driver_path = os.path.join(self.__driver_path, 'MicrosoftWebDriver.exe')
        driver = webdriver.Edge(executable_path=edge_driver_path)
        return driver

    @property
    def __get_remote_driver(self):   # selenium支持分布式 grid == > 配置（你自己的代码编写、配置）
        pass
if __name__ == "__main__":
    Browser().get_default_driver()
