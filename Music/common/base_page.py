# -*- coding utf-8 -*-
import os
from selenium.webdriver.common.by import By
from selenium import  webdriver
from Music.common.confing_utils import conf
from  Music.common.log_utils import logutils
from selenium.webdriver.support.wait import WebDriverWait

class BasePage(object):
    '''实例化浏览器对象'''
    def __init__(self,driver):
        self.driver=driver

    '''浏览器的二次封装'''
    def open_url(self,url):
        self.driver.get(url)
        '''打印日志'''
        logutils.info('打开浏览器:%s'%url)
    '''浏览器最大化设置'''
    def set_browser_max(self):
        self.driver.maximize_window()
        logutils.info('设置浏览器最大化')
    '''浏览器最小化设置'''
    def set_browser_min(self):
        self.driver.minimize_window()
        logutils.info('设置浏览器最小化')
    def get_title(self):
        value=self.driver.title
        logutils.info('获取浏览器网页标题')
        return value
    '''识别元素信息订单封装，element_info=login_page中的元素的识别信息   可以让所有元素显示等待   补齐元素识别方法，可以加异常'''
    def find_element(self,element_info):
        locator_type_name=element_info['locator_type']
        locator_value_info=element_info['locator_value']
        locator_timeout=element_info['timeout']
        if locator_type_name=='id':
            locator_type=By.ID
        elif locator_type_name=='class':
            locator_type=By.CLASS_NAME
        elif locator_type_name=='xpath':
            locator_type=By.XPATH
        '''self.driver传入浏览器，等待时间   locator_type：定位方式    locator_value_info：元素信息'''
        element=WebDriverWait(self.driver,locator_timeout).until(lambda x:x.find_element(locator_type,locator_value_info))
        logutils.info('[%s] 元素识别成功'%element_info['element_name'])
        return element
    '''封装输入方法，子类输入操作时候可调用这个方法'''
    def input(self,element_info,content):
        element=self.find_element(element_info)
        element.send_keys(content)
        logutils.info('[%s] 元素输入内容：%s'%(element_info['element_name'],content))

    '''封装点击操作方法，子类点击操作时可以调用这个方法'''
    def click(self,element_info):
        element=self.find_element(element_info)
        element.click()
        logutils.info('[%s] 元素进行点击操作'%element_info['element_name'])

