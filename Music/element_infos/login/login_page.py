#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc: 获取元素信息
from Music.common.browser import Browser
from Music.common.config_utils import conf
from Music.common.base_page import BasePage
from Music.common.element_data_utils import ELementdataUtils

class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        element = ELementdataUtils('login','login_page').get_element_info()
        self.username_inputbox = element['username_inputbox']
        self.password_inputbox = element['password_inputbox']
        self.login_button = element['login_button']
        self.return_loginfail_content = element['return_loginfail_content']

    def input_username(self,username):
        self.input_element_operation(self.username_inputbox,username)

    def input_password(self,password):
        self.input_element_operation(self.password_inputbox,password)

    def click_login(self):
        self.click_operation(self.login_button)

    def get_login_fail_alter_content(self):
        return self.switch_to_alter()

    def get_login_fail_return_content(self):
        text=self.get_elementinfo_text(self.return_loginfail_content)
        return text


if __name__ == "__main__":
    driver = Browser().get_default_driver()
    login_page = LoginPage(driver)
    login_page.open_url(conf.music_url)
    login_page.set_browser_personalized()
    login_page.input_username(conf.username)
    login_page.input_password(conf.password)
    login_page.click_login()
    login_page.substation_wait(2)
    login_page.screen_shoot_as_file()