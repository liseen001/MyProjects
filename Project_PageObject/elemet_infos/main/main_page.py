# --*utf-8*--
import os
from selenium import webdriver
from Project_PageObject.common.config_utils import conf
from Project_PageObject.common.base_page import BasePage
from Project_PageObject.elemet_infos.login.login_page import LoginPage
from  Project_PageObject.common.read_excel import ReadExcel

class MainPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        loginpage=LoginPage(driver)
        loginpage.open_url(conf.get_zend_path())
        loginpage.input_username(conf.get_username())
        loginpage.input_password(conf.get_password())
        loginpage.click_login()

        elements=ReadExcel('main_page').get_element_info()
        self.click_myzone=elements['click_myzone']
        self.click_product_menu=elements['click_product_menu']
        self.click_project_menu=elements['click_project_menu']
        self.click_test_menu=elements['click_test_menu']
        self.click_integration_menu=elements['click_integration_menu']
        self.click_doc_menu=elements['click_doc_menu']
        self.click_statistics_menu=elements['click_statistics_menu']
        self.click_organazation_menu=elements['click_organazation_menu']
        self.click_backstage_menu=elements['click_backstage_menu']
        self.click_username_menu=elements['click_username_menu']

    def click_myzone_operation(self):
        self.click(self.click_myzone())
    def click_product_menu_operation(self):
        self.click(self.click_product_menu)
    def click_project_menu_operation(self):
        self.click(self.click_project_menu)
    def click_test_menu_operation(self):
        self.click(self.click_test_menu)
    def click_integration_menu_operation(self):
        self.click(self.click_integration_menu)
    def click_doc_menu_operation(self):
        self.click(self.click_doc_menu)
    def click_statistics_menu_operation(self):
        self.click(self.click_statistics_menu)
    def click_organazation_menu_operation(self):
        self.click(self.click_organazation_menu)
    def click_backstage_menu_operation(self):
        self.click(self.click_backstage_menu)
    def click_username_menu_operation(self):
        self.click(self.click_username_menu)

if __name__=="__main__":
    current_path=os.path.dirname(__file__)
    driver_path=os.path.join(current_path,conf.get_foxfire_path())
    driver=webdriver.Firefox(executable_path=driver_path)
    mainpage=MainPage(driver)
    mainpage.click_doc_menu_operation()
    mainpage.click_product_menu_operation()