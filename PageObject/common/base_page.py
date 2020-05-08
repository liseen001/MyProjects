# -*- coding utf-8 -*-
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObject.common.config_utils import conf
from PageObject.common.log_utils import logutils
from selenium.webdriver.support.wait import WebDriverWait

class BasePage(object):
    '''传入默认参数'''
    def __init__(self,driver):
        '''实例化driver'''
        self.driver=driver

#浏览器封装操作
    '''打开浏览器地址'''
    def open_url(self,zendao_url):
        self.driver.get(zendao_url)
        logutils.info('打开浏览器path地址%s'%zendao_url)

    '''设置浏览器最大化并打印日志'''
    def set_browser_max(self):
        self.driver.maximize_window()
        logutils.info('设置浏览器最大化')

    def set_browser_min(self):
        self.driver.minimize_window()
        logutils.info('设置浏览器最小化')

    def browser_refresh(self):
        self.driver.refresh()
        logutils.info('刷新浏览器')

    def title(self):
        title=self.driver.title
        logutils.info('获取浏览器网页标题title')
        return title

    '''隐式等待时间封装，设置为配置文件中默认等时间为5'''
    def implicitly_wait(self,seconds=conf.time_out):
        self.driver.implicitly_wait(seconds)
        logutils.info('设置隐式等待时间为5秒')

    '''固定等待时间'''
    def wait(self,seconds=conf.time_out):
        time.sleep(seconds)
        logutils.info('固定等待时间为%s'%(seconds))

    def set_browser_quit(self):
        time.sleep(5)
        self.driver.close()
        logutils.info('关闭浏览器')

    def set_browser_back(self):
        self.wait()
        self.driver.back()
        logutils.info('浏览器返回上一页')

#元素识别、操作、元素操封装

    '''识别元素信息封装：核心  element_info=login中的元素的识别信息，可以让所有元素显示等待   补齐元素识别方法，加可以加异常'''
    '''封装查找元素的方法'''
    def find_element(self,element_info):
        '''locator_type  定位方式'''
        locator_type_name=element_info['locator_type']
        '''被定位到的元素'''
        locator_value_info=element_info['locator_value']
        '''超时花间'''
        locator_timeout=element_info['timeout']
        if locator_type_name=='id':
            locator_type=By.ID
        elif locator_type_name=='class':
            locator_type=By.CLASS_NAME
        elif locator_type_name=='xpath':
            locator_type=By.XPATH
        elif locator_type_name=='text':
            locator_type=By.LINK_TEXT
        '''self.driver传入浏览器，等待时间 locator_type：定位方式，locator_value_info：元素信息 '''
        element=WebDriverWait(self.driver,locator_timeout).until(lambda x:x.find_element(locator_type,locator_value_info))
        logutils.info('[%s]元素识别成功'%element_info['element_name'])
        return element

    '''点击操作的封装  element_info  元素信息'''
    def click_operation(self,element_info):
        element=self.find_element(element_info)
        element.click()
        logutils.info('[%s]元素进行点击操作'%element_info['element_name'])

    '''输入操作封装  conten:输入内容'''
    def input_operation(self,element_info,content):
        element=self.find_element(element_info)
        element.send_keys(content)
        logutils.info('[%s]元素进行输入内容：%s'%(element_info['element_name'],content))

    '''封装iframe切换框架方法一，有id和name则用之，无则做iframe对象'''
    def switch_to_frame(self,element_info):
        self.wait()
        element=self.find_element(element_info)
        self.driver.switch_to.frame(element)

    '''封装iframe切换框架方法二，先处理id和name，然后再切换框架'''
    def switch_to_frame_id_or_name(self,id_or_name):
        self.driver.switch_to.frame(id_or_name)

    def switch_to_frame_by_element(self,element_info):
        element=self.find_element(element_info)
        self.driver.switch_to.frame(element)
    '''封装iframe切换框架方法三，不定长参数，一个*代表元祖，两个代表字典'''
    def switch_to_frame_dict(self,**element_dict):
        if 'id' in element_dict.keys():
            self.driver.switch_to.frame(element_dict['id'])
        elif 'name' in element_dict.keys():
            self.driver.switch_to.frame(element_dict['name'])
        elif 'element' in element_dict.keys():
            self.driver.switch_to.frame(element_dict['element'])

    '''对js操作进行封装，执行操作封装'''
    def excute_script(self,js_str,element_info=None):
        if element_info:
            self.driver.execute_script(js_str)
        else:
            self.driver.execute_script(js_str,None)

if __name__=="__main__":
    pass