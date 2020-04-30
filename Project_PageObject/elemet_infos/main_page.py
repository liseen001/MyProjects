# --*utf-8*--
import os
from selenium.webdriver.common.by import By
from Project_PageObject.common.config_utils import conf
from Project_PageObject.elemet_infos.login_page import loginpage
from Project_PageObject.common.logutils import logutils

current_path=os.path.dirname(__file__)
driver_path=os.path.join(current_path,conf.get_foxfire_path())

class MainPage(object):
    def __init__(self):
        self.driver=loginpage.driver
        loginpage.input_username(conf.get_username())
        loginpage.input_password(conf.get_password())
        loginpage.click_login()
        self.companyname_showbox=self.driver.find_element(By.XPATH,'//h1[@id="companyname"]')
        self.myzone_menu=self.driver.find_element(By.XPATH,'//li[@data-id="my"]')
        self.product_menu=self.driver.find_element(By.XPATH,'//li[@data-id="product"]')
        self.username_showspan=self.driver.find_element(By.XPATH,'//span[@class="user-name"]')
        logutils.logger.info('登录禅道操作')

    def get_companyname(self):
        value=self.companyname_showbox.get_attribute('title')
        return value

    def goto_myzone(self):
        self.myzone_menu.click()


    def goto_productzone(self):
        self.product_menu.click()

    def get_username(self):
        value=self.username_showspan.text
        return value

mainpage=MainPage()
if __name__=="__main__":
    mainpage.goto_productzone()
