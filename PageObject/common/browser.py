# -*- coding utf-8 -*-
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PageObject.common.config_utils import conf
from PageObject.common.log_utils import logutils

current_path=os.path.dirname(__file__)
chromedriver_path=os.path.join(current_path,conf.chromedriver_path)
firefoxdriver_path=os.path.join(current_path,conf.firefoxdriver_path)

class Browser(object):
    def __init__(self,__chromedriver_path=chromedriver_path,__firefoxdriver_path=firefoxdriver_path,driver_name=conf.default_driver_name):
        self.__chromedriver_path=chromedriver_path
        self.__firefoxdriver_path=firefoxdriver_path
        self.__driver_name=driver_name

    '''获取配置文件中默认配置浏览器的方法'''

    def get_default_driver(self):
        if self.__driver_name.lower()=='chrome':
            return self.get_chrome_driver
        elif self.__driver_name.lower()=='firefox':
            return self.get_firefox_driver
        elif self.__driver_name.lower()=='edge':
            pass



    '''获取谷歌驱动'''
    @property
    def get_chrome_driver(self):
        chrome_driver_path=os.path.join(self.__chromedriver_path)
        driver=webdriver.Chrome(executable_path=chrome_driver_path)
        return driver

    '''获取火狐驱动'''
    @property
    def get_firefox_driver(self):
        firefoxdriver_path=os.path.join(self.__firefoxdriver_path)
        driver=webdriver.Firefox(executable_path=firefoxdriver_path)
        logutils.info('初始化并启动默认浏览器驱动')
        return driver
browser=Browser()
if __name__=="__main__":
    browser.get_default_driver()