#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc: 封装base_page类
import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.common.by import By
from common import HTMLTestReportCN
from common.config_utils import conf
from common.log_utils import logutils
from selenium.webdriver.support.wait import WebDriverWait

class BasePage(object):
    def __init__(self,driver):
        self.driver=driver
        self.chains = ActionChains(self.driver)
        logutils.info('实例化浏览器驱动')

#===============  浏览器操作封装  ===============
    def open_url(self,url):
        try:
            self.driver.get(url)
            logutils.info('打开浏览器地址%s'%url)
        except Exception as e:
            logutils.error('不能打开浏览器地址，原因是：%s'%e.__str__())
            self.screen_shoot_as_file()

    def close_current_browser_tab(self):
        try:
            self.driver.close()
            logutils.info('关闭当前tab页签')
        except Exception as e:
            logutils.error('关闭当前tab页签失败，原因是：%s'%e.__str__())
            self.screen_shoot_as_file()

    def exit_browser(self):
        try:
            self.driver.quit()
            logutils.info('关闭浏览器')
        except Exception as e:
            logutils.error('关闭浏览器失败，失败的原因是：%s'%e.__str__())
            self.screen_shoot_as_file()

    def set_browser_max(self):
        try:
            self.driver.maximize_window()
            logutils.info('设置浏览器最大化')
        except Exception as e:
            logutils.error('设置浏览器最大化失败，原因是:%s'%e.__str__())
            self.screen_shoot_as_file()

    def set_browser_personalized(self):
        try:
            logutils.info('开始进行个性化浏览器设置')
            self.driver.maximize_window()
            time.sleep(2)
            self.driver.set_window_size(450,900)
            logutils.info('最大化浏览器，等待时间为默认等待时间，设置浏览器窗口为450*900的H5页面')
        except Exception as e:
            logutils.error('进行个性化浏览器设置失败，失败的原因是：%s'%e.__str__())
            self.screen_shoot_as_file()

    def set_browser_min(self):
        try:
            self.driver.minimize_window()
            logutils.info('设置浏览器最小化')
        except Exception as e:
            logutils.error('设置浏览器最大化失败，原因是:%s'%e.__str__())
            self.screen_shoot_as_file()

    def set_browser_refresh(self):
        try:
            self.driver.refresh()
            logutils.info('刷新浏览器')
        except Exception as e:
            logutils.error('刷新浏览器失败，失败的原因是：%s'%e.__str__())
            self.screen_shoot_as_file()
    def get_current_browser_title(self):
        try:
            value =self.driver.title
            logutils.info('获取当前浏览器窗口的标题'%value)
        except Exception as e:
            logutils.error('获取当前浏览器窗口的标题失败，失败的原因是：%s'%e.__str__())
            self.screen_shoot_as_file()

    def get_elementinfo_text(self,element_info):
        try:
            element=self.driver.find_element(element_info)
            logutils.info('获取元素文本信息%s成功'%(element_info['element_name']))
        except Exception as e:
            logutils.error(('获取元素文本信息%s失败'%element_info['element_name']),'原因是：%s'%e.__str__())
            self.screen_shoot_as_file()
        return element.text

    def set_browser_back(self):
        try:
            self.substation_wait()
            self.driver.back()
            logutils.info('返回浏览器上一页')
        except Exception as e:
            logutils.error('返回浏览器上一页，失败的原因是：%s'%e.__str__())

    def switch_to_frame_by_element(self,element_info):   #  方法一切换至frame框架
        try:
            self.substation_wait(conf.time_out)
            element = self.find_element(element_info)
            self.driver.switch_to.frame(element)
            logutils.info('切换至frame框架')
        except Exception as e:
            logutils.error('切换至frame框架失败，失败的原因是：%s'%e.__str__())

    def switch_to_frame_id_or_name(self,id_or_name):   #  方法二切换至frame框架
        try:
            self.driver.switch_to.frame(id_or_name)
            logutils.info('切换至frame框架')
        except Exception as e:
            logutils.error('切换至frame框架失败，失败的原因是%s'%e.__str__())

    def switch_to_frame_dict(self,**element_dict):
        try:
            if 'id' in element_dict.keys():
                self.driver.switch_to.frame(element_dict['id'])
            elif 'name' in element_dict.keys():
                self.driver.switch_to.frame(element_dict['name'])
            elif 'element' in element_dict.keys():
                self.driver.switch_to.frame(element_dict['element'])
            logutils.info('切换至frame成功')
        except Exception as e:
            logutils.error('切换至frame框架失败，失败的原因是：%s'%e.__str__())


# ===============  等待时间操作封装  ===============
    def substation_wait(self,seconds=conf.time_out):
        time.sleep(seconds)
        logutils.info('设置固定等待时间为：%s'%seconds)

    def implicity_wait(self,seconds=conf.time_out):
        try:
            self.driver.implicitly_wait(seconds)
            logutils.info('设置隐式等待时间为%s秒'%seconds)
        except Exception as e:
            logutils.error('隐式等待设置失效，原因是：%s'%e.__str__())
            self.screen_shoot_as_file()

# ===============  截图封装  ===============
    def screen_shoot_as_file(self):     #新截图方法  调用HTMLTestReportCN里面的方法截图
        try:
             report_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),'..',conf.report_path)  #自定义截图报告路径
             report_dir = HTMLTestReportCN.ReportDirectory(report_path)
             report_dir.get_screenshot(self.driver)
             logutils.info('截图成功')
        except Exception as e:
             logutils.error('截图失败，失败的原因是：%s'%e.__str__())

    def screen_shot_as_file_old(self,*screenshot_path):
        try:
            current_dir = os.path.dirname(__file__)
            if len(screenshot_path) == 0:
                screenshot_filepath = conf.screen_shot_path
            else:
                 screenshot_filepath = screenshot_path[0]
            now = time.strftime('%Y_%m_%d_%H_%M_%S')
            screenshot_filepath = os.path.join(current_dir,screenshot_filepath,'测试截图——%s.png'%now)
            self.driver.get_screenshot_as_file(screenshot_filepath)
            logutils.info('截图成功')
        except Exception as e:
            logutils.error('截图失败，失败的原因是：%s'%e.__str__())



# ===============  元素识别、操作、元素操封装  ===============
    '''查找元素的封装'''
    def find_element(self,element_info):
        '''
        根据提供的元素参数信息进行元素的查找
        :param element_info:
        :return:element对象
        '''
        try:
            locator_type_name=element_info['locator_type']   #locator_type_name  定位方式
            locator_value_info=element_info['locator_value']  #locator_value_info  被定为到的元素
            locator_timeout = element_info['timeout']   #locator_timeout  超时时间
            if locator_type_name == 'id':
                locator_type = By.ID
            elif locator_type_name == 'name':
                locator_type = By.NAME
            elif locator_type_name == 'class':
                locator_type = By.CLASS_NAME
            elif locator_type_name == 'xpath':
                locator_type = By.XPATH
            element = WebDriverWait(self.driver,locator_timeout).until(lambda x:x.find_element(locator_type,locator_value_info))
            logutils.info('[%s]元素识别成功'%element_info['element_name'])
        except Exception as e:
            logutils.error('[%s]元素识失败，失败的原因是：%s'%(element_info['element_name'],e.__str__()))
            self.screen_shoot_as_file()
        return element

    '''点击元素操作的封装  element_info  元素信息'''
    def click_operation(self,element_info):
        element = self.find_element(element_info)
        try:
            element.click()
            logutils.info('[%s]元素进行点击操作'%element_info['element_name'])
        except Exception as e:
            logutils.error('[%s]元素点击操作失败，原因是%s'%e.__str__())
            self.screen_shoot_as_file()

    '''元素输入操作的封装'''
    def input_element_operation(self,element_info,content):
        element = self.find_element(element_info)
        try:
            element.send_keys(content)
            logutils.info('[%s]元素输入内容为：%s' %(element_info['element_name'], content))
        except Exception as e:
            logutils.error('[%s]元素输入失败，输入的元素内容为:%s'%(element_info['element_name'],content))
            self.screen_shoot_as_file()


# ===============  JS操作封装  ===============
    def excute_script(self,js_str,element_info=None):
        try:
            if element_info:
                self.driver.execute_script(js_str)
            else:
                self.driver.execute_script(js_str,None)
                logutils.info('执行js操作成功')
        except Exception as e:
            logutils.error('执行js操作失败，失败的原因是：%s'%e.__str__())
            self.screen_shoot_as_file()

# ===============  alrer弹出窗封装  ===============
    '''确定与取消按钮，默认点击确定'''
    def switch_to_alter(self,action='accept',time_out=conf.time_out):
        try:
            self.substation_wait(time_out)
            try:
                WebDriverWait(self.driver,time_out).until(Ec.alert_is_present())
                logutils.info('成功切换至弹出框')
            except Exception as e:
                logutils.error('切换至弹出框失败，失败的原因是：%s' % e.__str__())
            alter = self.driver.switch_to.alert
            alter_text = alter.text
            if action == 'accept':
                alter.accept()
            elif action == 'dismiss':
                alter.dismiss()
            logutils.info('切换至页面弹出框，获取弹出框的文本信息为%s'%alter_text)
        except Exception as e:
            logutils.error('切换至弹出框，获取弹出框的文本信息失败%s失败的原因是：%s',e.__str__())
            self.screen_shoot_as_file()

# ===============  切换句柄的封装  ===============
    def get_window_handle(self):
        return self.driver.current_window_handle
    def switct_to_window_by_handle(self,window_handle):
        self.driver.switch_to.window(window_handle)

    def switch_to_window_by_title(self,title):
        try:
            window_handles = self.driver.window_handles
            for window_handle in window_handles:
                '''页面包含title则切过去，如果不包含则不等待'''
                if WebDriverWait(self.driver, conf.time_out).until(Ec.title_contains(title)):
                    self.driver.switch_to.window(window_handle)
                    logutils.info('根据网页标题%s切换句柄' % (title))
                    break
        except Exception as e:
            logutils.error('切换句柄失败，失败的原因是%s'%e.__str__())
            self.screen_shoot_as_file()


    def switch_to_window_by_url(self,url):
        try:
            window_handles = self.driver.window_handles
            for window_handle in window_handles:
                if WebDriverWait(self.driver,conf.time_out).until(Ec.url_contains(url)):
                    self.driver.switch_to.window(window_handle)
                    logutils.info('根据url切换句柄成功')
                    break
        except Exception as e:
            logutils.error('根据url切换句柄失败，失败的原因是%s'%e.__str__())
            self.screen_shoot_as_file()


# ===============  鼠标键盘封装  建议代码思路：先判断操作系统类型  ===============
    def move_to_element_be_mouse(self,element_info):
        try:
            element = self.find_element(element_info)
            ActionChains(self.driver).move_to_element(element).perform()
            logutils.info('鼠标移动至元素%s成功'%element)
        except Exception as e:
            logutils.error('鼠标移动至元素%s失败'%element,'失败的原因是：%s'%e.__str__())
            self.screen_shoot_as_file()

    '''推荐写法'''
    def long_press_element(self,element_info):
        try:
            element = self.find_element(element_info)
            ActionChains(self.driver).click_and_hold(element).pause(seconds=conf.time_out).reset_actions(element)
            logutils.info('鼠标移动至元素%s成功' % element)
        except Exception as e:
            logutils.error('鼠标移动至元素%s失败'%element,'失败的原因是：%s'%e.__str__())
            self.screen_shoot_as_file()