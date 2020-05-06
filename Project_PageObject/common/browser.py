# -*- coding utf-8 -*-
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Project_PageObject.common.config_utils import conf

current_path=os.path.dirname(__file__)
chromedriver_path=os.path.join(current_path,conf.get_chrome_driver)
firefoxdriver_path=os.path.join(current_path,conf.get_foxfire_path)


class Browser(object):
    def __init__(self,chromedriver_path=chromedriver_path,firefoxdriver_path=firefoxdriver_path,driver_name=conf.get_driver_name):
        self.__chrome_driver_path=chromedriver_path
        self.__firefox_driver_path=firefoxdriver_path
        self.__driver_name=driver_name

    '''封装获取配置文件配置的默人浏览器驱动方法'''
    def get_driver(self):
        if self.__driver_name.lower()=='chrome':
            return self.get_chrome_driver
        elif self.__driver_name.lower()=='firefox':
            return self.get_firefox_driver
        elif self.__driver_name.lower()=='edge':
            return self.get_edge_driver


    '''封装谷歌浏览器'''
    @property
    def get_chrome_driver(self):
        chrome_options=Options()
        chrome_options.add_argument('--disable-gpu')  #谷歌文档提刀需要加上这个属性来规避BUG
        chrome_options.add_argument('lang=zh_CN.UTF-8')  #设置默认编码为utf-8
        chrome_options.add_experimental_option('useAutomationExtension',False) #取消浏览器正在收到自动化工具的提示
        chrome_options.add_experimental_option("excludeSwitches",['enable-aotomation'])
        chrome_driver_path=os.path.join(self.__chrome_driver_path,)
        driver=webdriver.Chrome(options=chrome_options,executable_path=chrome_driver_path)
        return driver

    '''封装火狐浏览器'''
    @property
    def get_firefox_driver(self):
        firefox_driver_path=os.path.join(self.__firefox_driver_path)
        driver=webdriver.Firefox(executable_path=firefox_driver_path)
        return driver

    '''封装IE浏览器'''
    @property
    def get_edge_driver(self):
        pass

browser=Browser()

if __name__=="__main__":
    browser.get_chrome_driver