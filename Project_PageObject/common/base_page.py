# -*- coding utf-8 -*-
import os
import  time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Project_PageObject.common.config_utils import conf
from Project_PageObject.common.logutils import logutils
from selenium.webdriver.support.wait import WebDriverWait

current_path = os.path.dirname(__file__)
driver_path = os.path.join(current_path, conf.get_foxfire_path())
driver = webdriver.Firefox(executable_path=driver_path)

class BasePage(object):
    def __init__(self,driver):
        self.driver=driver


    '''浏览器操作封装----二次封装'''
    def open_url(self,url=conf.get_zend_path()):
        self.driver.get(url)
        logutils.info('打开url地址%s'%url)   #打印日志

    def set_browser_max(self):
        self.driver.maximize_window()
        logutils.info('设置浏览器最大化')

    def set_browser_min(self):
        self.driver.minimize_window()
        logutils.info('设置浏览器最小化')

    def get_title(self):
        value=self.driver.title
        logutils.info('获取浏览器网页标题')
        return value

#元素识别、操作

    #识别元素信息
    def find_element_info(self,element_info):
        locator_type_name=element_info['locator_type']   #locator_type  定位方式
        locator_value_info=element_info['locator_value'] #定位的元素
        locator_timeout=element_info['timeout']           #超时时间
        if locator_type_name =='id':
            locator_type=By.ID
        elif locator_type_name=='class':
            locator_type=By.CLASS_NAME
        elif locator_type_name=='xpath':
            locator_type=By.XPATH
        element=WebDriverWait(self.driver,locator_timeout).until(lambda x:x.find_element(locator_type,locator_value_info))
        return element

    def click(self,element_info):
        element=self.find_element(element_info)
        element.click()

    def input(self,element_info,content):
        element=self.find_element(element_info)
        element.send_keys(content)

basepage=BasePage(driver)

