# -*- coding utf-8 -*-
import os

from PageObject.common.base_page import BasePage
from PageObject.common.config_utils import conf
from PageObject.common.element_data_utils import ElementdataUtils
from PageObject.element_infos.login.login_page import LoginPage
from PageObject.common.browser import Browser

class MainPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        mainpage_element=ElementdataUtils('main','main_page').get_element_info()
        self.myzone_link=mainpage_element['myzone_link']
        self.user_menu=mainpage_element['user_menu']
        self.quit_button = mainpage_element['quit_button']


    '''点击我的地盘'''
    def goto_myzone(self):
        self.click_operation(self.myzone_link)

    def get_username(self):
        value = self.get_text(self.user_menu)
        return value

    def click_username(self):
        self.click_operation( self.user_menu )

    def click_quit_button(self):
        self.close_tab( self.quit_button )


if __name__=="__main__":
    driver = Browser().get_default_driver()
    # driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
    # main_page = LoginAction(driver).default_login()
    # value = main_page.get_username()
    # print(value)




