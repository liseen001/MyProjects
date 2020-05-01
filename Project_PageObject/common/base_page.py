# -*- coding utf-8 -*-
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from Project_PageObject.common.config_utils import conf
from Project_PageObject.common.logutils import logutils
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self,driver):
        self.driver=driver    #


    '''浏览器操作封装----二次封装'''
    def open_url(self,url):
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

#元素识别、操作  元素操作封装

    #识别元素信息封装    核心   element_info=login_page中的元素的识别信息   可以让所有元素显示等待   补齐元素识别方法，加可以加异常
    def find_element(self,element_info):
        locator_type_name=element_info['locator_type']   #locator_type  定位方式
        locator_value_info=element_info['locator_value'] #定位的元素
        locator_timeout=element_info['timeout']           #超时时间
        if locator_type_name =='id':    #可以用包含等方式
            locator_type=By.ID          #把字符串的方式改成真正的方式
        elif locator_type_name=='class':
            locator_type=By.CLASS_NAME
        elif locator_type_name=='name':
            locator_type=By.NAME
        elif locator_type_name=='xpath':
            locator_type=By.XPATH         #self.driver传入浏览器，等待时间   locator_type：定位方式    locator_value_info：元素信息
        element=WebDriverWait(self.driver,locator_timeout).until(lambda x:x.find_element(locator_type,locator_value_info))
        logutils.info('[%s]元素识别成功'%element_info['element_name'])   #元素名称
        return element

    #点击操作封装    element_info：元素信息字典
    def click(self,element_info):
        element=self.find_element(element_info)
        element.click()
        logutils.info('[%s]元素进行点击操作'%element_info['element_name'])

    #输入操作封装   content：输入内容
    def input(self,element_info,content):
        element=self.find_element(element_info)
        element.send_keys(content)
        logutils.info('[%s]元素输入内容： %s'%(element_info['element_name'],content))



