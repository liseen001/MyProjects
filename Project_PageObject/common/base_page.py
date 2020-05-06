# -*- coding utf-8 -*-
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from Project_PageObject.common.config_utils import conf
from Project_PageObject.common.logutils import logutils
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    '''传入默认参数driver'''
    def __init__(self,driver):
        '''实例化driver'''
        self.driver=driver


    '''浏览器操作封装----二次封装打开浏览器地址'''
    def open_url(self,url):
        self.driver.get(url)
        '''base_page类中打印日志'''
        logutils.info('打开url地址%s'%url)
    '''设置浏览器最大化'''
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

    '''识别元素信息封装    核心   element_info=login_page中的元素的识别信息   可以让所有元素显示等待   补齐元素识别方法，加可以加异常'''
    def find_element(self,element_info):
        '''locator_type  定位方式'''
        locator_type_name=element_info['locator_type']
        '''定位的元素'''
        locator_value_info=element_info['locator_value']
        '''超时时间'''
        locator_timeout=element_info['timeout']
        if locator_type_name =='id':    #可以用包含等方式
            locator_type=By.ID          #把字符串的方式改成真正的方式
        elif locator_type_name=='class':
            locator_type=By.CLASS_NAME
        elif locator_type_name=='name':
            locator_type=By.NAME
        elif locator_type_name=='xpath':
            locator_type=By.XPATH
        '''#self.driver传入浏览器，等待时间   locator_type：定位方式    locator_value_info：元素信息'''
        element=WebDriverWait(self.driver,locator_timeout).until(lambda x:x.find_element(locator_type,locator_value_info))
        logutils.info('[%s]元素识别成功'%element_info['element_name'])
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


    #封装iframe切换框架，有id\name用id\name，没有就做iframe对象
    '''思路一'''
    def switch_to_frame(self,element_info):
        element = self.find_element(element_info)
        self.driver.switch_to.frame(element)

    '''思路二,先处理id和name,然后再切换框架'''
    def switch_to_frame_id_or_name(self,id_or_name):
        self.driver.switch_to.frame(id_or_name)

    def switch_to_frame_by_element(self,element_info):
        elment=self.find_element(element_info)
        self.driver.switch_to.frame(elment)

    '''思路三：用字典的方式处理，不定长参数，一个*代表元组，两个则代表字典'''
    def switch_to_frame_dict(self,**element_dict):
        if 'id' in element_dict.keys():
            self.driver.switch_to.frame(element_dict['id'])
        elif 'name' in element_dict.keys():
            self.driver.switch_to.frame(element_dict['name'])
        elif 'element' in element_dict.keys():
            self.driver.switch_to.frame(element_dict['element'])


    '''对js进行封装，执行js操作'''
    def execute_script(self,js_str,element_info=None):
        if element_info:
            self.driver.excute_script(js_str)
        else:
            self.driver.excute_script(js_str,None)

    '''对js删除操作封装'''
    def delete_element_attribute(self,element_info,attribute_name):
        element=self.find_element(element_info)
        self.execute_script('..JScode..')



