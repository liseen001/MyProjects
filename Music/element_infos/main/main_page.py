#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
from Music.common.base_page import BasePage
from Music.common.config_utils import conf
from Music.common.browser import Browser
from Music.common.element_data_utils import ELementdataUtils

from Music.element_infos.login.login_page import LoginPage

class MainPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        element =ELementdataUtils('main','main_page').get_element_info()
        self.music_class_menu = element['music_class_menu']
        self.singer_class_menu = element['singer_class_menu']
        self.chatroom_memu = element['chatroom_memu']
        self.search_menu = element['search_menu']
        self.more_menu = element['more_menu']

    def click_music_class_menu(self):
        self.click_operation(self.music_class_menu)

    def click_singer_class_menu(self):
        self.click_operation(self.singer_class_menu)

    def click_chatroom_memu(self):
        self.click_operation(self.chatroom_memu)

    def click_search_menu(self):
        self.click_operation(self.search_menu)

    def get_more_text(self):
        value = self.get_elementinfo_text(self.more_menu)
        return value

if __name__ == "__main__":
    # element = ELementdataUtils('main', 'main_page').get_element_info()
    # for i in element.values():
    #     print(i)
    driver = Browser().get_default_driver()
    driver.get(conf.music_url)
