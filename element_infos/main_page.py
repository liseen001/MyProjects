# -*- coding utf-8 -*-
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from element_infos.login_page import LoginPage

current=os.path.dirname(__file__)
driver_path=os.path.join(current,'../webdriver/geckodriver')


class MainPage(object):
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=driver_path)
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get('http://106.53.50.202:8999/zentao6/www/user-login.html')

        self.companyname=self.driver.find_element(By.XPATH,'//h1[@id="companyname"]')          #1、查找公司命名元素
        self.myzone_menu=self.driver.find_element(By.XPATH,'//li[@data-id="my"]')              #2、我的地盘
        self.product_menu=self.driver.find_element(By.XPATH,'//li[@data-id="product"]')        #3、产品
        self.project_menu=self.driver.find_element(By.XPATH,'//li[@data-id="project"]')        #4、项目
        self.test_menu=self.driver.find_element(By.XPATH,'//li[@data-id="qa"]')                #5、测试
        self.integration_menu=self.driver.find_element(By.XPATH,'//li[@data-id="ci"]')         #6、集成
        self.doc_menu=self.driver.find_element(By.XPATH,'//li[@data-id="doc"]')                #7、文档
        self.statistic_menu=self.driver.find_element(By.XPATH,'//li[@data-id="report"]')       #8、统计
        self.organization_menu=self.driver.find_element(By.XPATH,'//li[@data-id="company"]')   #9、
        self.admin_menu=self.driver.find_element(By.XPATH,'//li[@data-id="admin"]')            #10、后台

    def get_companyname(self):
        value = self.companyname.text
        return value
    def click_myzone_menu(self):
        self.myzone_menu.click()
    def click_product_menu(self):
        self.product_menu.click()
    def click_project_menu(self):
        self.product_menu.click()
    def click_test_menu(self):
        self.test_menu.click()
    def click_integration_menu(self):
        self.integration_menu.click()
    def click_doc_menu(self):
        self.doc_menu.click()
    def click_statistic_menu(self):
        self.statistic_menu.click()
    def click_organization_menu(self):
        self.organization_menu.click()
    def click_admin_menu(self):
        self.admin_menu.click()

if __name__=="main__":
    main_page=MainPage()
    main_page.get_companyname()
    main_page.click_myzone_menu()
    main_page.click_product_menu()
