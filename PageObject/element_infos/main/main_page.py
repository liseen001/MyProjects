# -*- coding utf-8 -*-
import os

from PageObject.common.base_page import BasePage
from PageObject.common.config_utils import conf
from PageObject.common.read_excel import ReadExcel
from PageObject.element_infos.login.login_page import LoginPage
from PageObject.common.browser import browser

class MainPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        loginpage=LoginPage(driver)
        loginpage.open_url(conf.zend_path)
        loginpage.set_browser_max()
        loginpage.input_username(conf.zengtao_username)
        loginpage.input_password(conf.zentao_password)
        loginpage.click_login()


        mainpage_element=ReadExcel('main','main_page').get_element_info()
        self.__click_myzone=mainpage_element['click_myzone']
        self.__click_product_menu=mainpage_element['click_product_menu']
        self.__click_project_menu=mainpage_element['click_project_menu']
        self.__click_test_menu=mainpage_element['click_test_menu']
        self.__click_integration_menu=mainpage_element['click_integration_menu']
        self.__click_doc_menu=mainpage_element['click_doc_menu']
        self.__click_statistics_menu=mainpage_element['click_statistics_menu']
        self.__click_organazation_menu=mainpage_element['click_organazation_menu']
        self.__click_backstage_menu=mainpage_element['click_backstage_menu']
        self.__click_username_menu=mainpage_element['click_username_menu']
        self.__quit_login=mainpage_element['quit_login']

    '''点击我的地盘'''
    def click_myzone(self):
        self.click_operation(self.__click_myzone)
    '''点击产品菜单'''
    def click_product_menu(self):
        self.click_operation(self.__click_product_menu)
    '''点击项目菜单'''
    def click_project_menu(self):
        self.click_operation(self.__click_project_menu)
    '''点击测试菜单'''
    def click_test_menu(self):
        self.click_operation(self.__click_test_menu)
    '''点击集成菜单'''
    def click_integration_menu(self):
        self.click_operation(self.__click_integration_menu)
    '''点击文档菜单'''
    def click_doc_menu(self):
        self.click_operation(self.__click_doc_menu)
    '''点击统计菜单'''
    def click_statistics_menu(self):
        self.click_operation(self.__click_statistics_menu)
    '''点击组织菜单'''
    def click_organazation_menu(self):
        self.click_operation(self.__click_organazation_menu)
    '''点击后台菜单'''
    def click_backstage_menu(self):
        self.click_operation(self.__click_backstage_menu)

    def click_username_menu(self):
        self.click_operation(self.__click_username_menu)

    '''返回元素信息文本'''
    def get_usrname(self):
        value=self.get_text(self.__click_username_menu)
        return value

    def quit_zentao(self):
        self.click_operation(self.__quit_login)


mainpage = MainPage(driver=browser.get_default_driver())
if __name__=="__main__":
    mainpage.click_myzone()
    mainpage.click_product_menu()
    mainpage.click_project_menu()
    mainpage.click_test_menu()
    mainpage.click_integration_menu()
    mainpage.click_doc_menu()
    mainpage.click_statistics_menu()
    mainpage.click_organazation_menu()
    mainpage.click_backstage_menu()
    mainpage.click_username_menu()
    value=mainpage.get_usrname()
    value1=mainpage.get_title()
    print(value,value1)
    mainpage.quit_zentao()
    value2=mainpage.get_title()
    print(value2)




