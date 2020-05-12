# -*- coding utf-8 -*-
import os
import time
from selenium import webdriver
from  selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
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
        logutils.info('退出浏览器')

    def close_tab(self):
        self.driver.close()
        logutils.info('关闭当前tab页签')

    def set_browser_back(self):
        self.wait()
        self.driver.back()
        logutils.info('浏览器返回上一页')

    def get_text(self,element_info):
        element=self.find_element(element_info)
        logutils.info('获取元素文本信息%s'%element_info['element_name'])
        return element.text

    def get_title(self):
        value=self.driver.title
        logutils.info('获取浏览器标题，标题是%s'%value)

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

#鼠标键盘封装  建议代码思路：先判断操作系统类型
    '''鼠标移动到元素上去'''
    def move_to_element_be_mouse(self,element_info):
        element=self.find_element(element_info) #识别元素
        ActionChains(self.driver).move_to_element(element).perform()

    '''推荐写法'''
    def long_press_element(self,element_info):
        element = self.find_element(element_info)  # 识别元素
        ActionChains(self.driver).click_and_hold(element).pause(seconds=conf.time_out).reset_actions(element)

#alrer弹出窗的封装
    '''确定与取消按钮，默认点击确定'''
    def switch_to_alter(self,action='accept',time_out=conf.time_out):
        '''等待时间'''
        self.wait(time_out)
        WebDriverWait(self.driver,time_out).until(EC.alert_is_present())
        alter=self.driver.switch_to.alert
        alter_text=alter.text
        if action=='accept':
            alter.accept()
        elif action=='dismiss':
            alter.dismiss()
        return alter_text

#切换句柄的封装
    def get_window_handle(self):
        return self.driver.current_window_handle

    def switch_to_window_by_handle(self,window_handle):
        self.driver.switch_to.window(window_handle)
    '''根据title切换'''
    def switch_to_window_by_title(self,title):
        window_handles =self.driver.window_handles
        for window_handle in window_handles:
            '''页面包含title则切过去，如果不包含则不等待'''
            if WebDriverWait(self.driver,conf.time_out).until(EC.title_contains(title)):
                self.driver.switch_to.window(window_handle)
                break
    '''根据url切换'''
    def switch_to_window_by_url(self,url):
        window_handles=self.driver.window_handles
        for window_handle in window_handles:
            if WebDriverWait(self.driver,conf.time_out).until(EC.url_contains(url)):
                self.driver.switch_to.window(window_handle)
                break
#截图封装
    '''根据时间截图的封装,元组类型的不定长阐述，长度为0则为默认路径，不为零则取第一个路径'''
    def screen_shoot_as_file(self,*screenshot_path):
        current_dir = os.path.dirname(__file__)
        if len(screenshot_path)==0:
            screenshot_filepath=conf.screen_shoot_path
        else:
            screenshot_filepath=screenshot_path[0]
        now=time.strftime('%Y_%m_%d_%H_%M_%S')
        screenshot_filepath=os.path.join(current_dir,screenshot_filepath,'UITest——%s.png'%now)
        self.driver.get_screenshot_as_file(screenshot_filepath)


if __name__=="__main__":
    pass