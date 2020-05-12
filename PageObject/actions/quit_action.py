# -*- coding utf-8 -*-
from PageObject.element_infos.login.login_page import LoginPage
from PageObject.element_infos.main.main_page import MainPage
from PageObject.common.config_utils import conf

class QuitAction:
    def __init__(self,driver):
        self.main_page=MainPage(driver)

    def quit(self):
        self.main_page.click_username_menu()
        self.main_page.quit_zentao()
        return LoginPage(self.main_page.driver)