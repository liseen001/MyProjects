# -*- coding utf-8 -*-
from PageObject.common.browser import browser
from PageObject.common.base_page import BasePage
from PageObject.common.config_utils import conf
from PageObject.common.read_excel import ReadExcel
from PageObject.element_infos.login.login_page import LoginPage
from PageObject.element_infos.main.main_page import MainPage

class FirstPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        loginpage = LoginPage(driver)
        loginpage.open_url(conf.zend_path)
        loginpage.set_browser_max()
        loginpage.input_username(conf.zengtao_username)
        loginpage.input_password(conf.zentao_password)
        loginpage.click_login()


        firstpage_element=ReadExcel('myzone','first_page').get_element_info()
        self.homepage_button=firstpage_element['homepage_button']

    def clck_homepage_button(self):
        self.click_operation(self.homepage_button)

if __name__=="__main__":
    firstpage = FirstPage(driver=browser.get_default_driver())
    firstpage.clck_homepage_button()
    firstpage.screen_shoot_as_file()

