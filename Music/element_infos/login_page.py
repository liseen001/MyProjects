# -*- coding utf-8 -*-
import os
from selenium import webdriver
from Music.common.confing_utils import conf
from Music.common.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self,driver):
        '''父类有selef.driver的构造，子类也有这个构造，这里需要显示调用父类的构造'''
        super().__init__(driver)
        '''识别元素信息,用户名输入、密码输入、点击登录按钮'''
        self.username_inputbox={'element_name':'用户名输入框',
                                'locator_type':'xpath',
                                'locator_value':'//input[@type="text"]',
                                'timeout':5}
        '''locator_type:识别元素的方法，locator_value：元素识别的具体对象,timeout:设置超时时间'''
        self.password_inputbox={'element_name':'密码输入框',
                                'locator_type':'xpath',
                                'locator_value':'//input[@type="password"]',
                                'timeout':5}
        self.login_buttom={'element_name':'登录按钮',
                           'locator_type':'xpath',
                           'locator_value':'//div[@class="login-btn"]',
                           'timeout':5}
    '''这是一个元素信息（字典），首先调用父类input方法，首先会调用find_element方法查找元素'''
    def input_username(self,username):
        self.input(self.username_inputbox,username)
    def input_password(self,password):
        self.input(self.password_inputbox,password)
    def click_login(self):
        self.click(self.login_buttom)

if __name__=="__main__":
    '''打开浏览器操作'''
    current_path=os.path.dirname(__file__)
    driver_path=os.path.join(current_path,conf.get_foxfire_path())
    driver=webdriver.Firefox(executable_path=driver_path)


    '''实例化driver'''
    loginpage=LoginPage(driver)
    '''调用父类中打开浏览器的方法，调用config_utils中获取url的方法'''
    loginpage.open_url(conf.get_music_url())
    '''调用父类中设置浏览器最大化的方法'''
    loginpage.set_browser_max()
    '''子类中调用输入用户名函数，用户名调用配置类中获取用户名的方法'''
    loginpage.input_username(conf.get_music_login_username())
    '''子类中调用输入密码函数，密码调用配置类中获取用户名的方法'''
    loginpage.input_password(conf.get_music_login_password())
    '''调用子类中点击登录的方法'''
    loginpage.click_login()