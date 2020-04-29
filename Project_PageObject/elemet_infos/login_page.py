# --*utf-8*--
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from Project_PageObject.common.config_utils import conf

current_path= os.path.dirname(__file__)
driver_path=os.path.join(current_path,conf.get_foxfire_path())

class LoginPage(object):
    def __init__(self):
        self.driver=webdriver.Firefox(executable_path=driver_path)
        self.driver.implicitly_wait(10)
        self.driver.get(conf.get_zend_path())
        self.username_inputbox=self.driver.find_element(By.XPATH,'//input[@name="account"]')
        self.password_inputbox=self.driver.find_element(By.XPATH,'//input[@name="password"]')
        self.logion_button=self.driver.find_element(By.XPATH,'//button[@id="submit"]')
        self.keeplogin_checkbox=self.driver.find_element(By.XPATH,'//input[@id="keepLoginon"]')

    def input_username(self,username):
        self.username_inputbox.send_keys(username)

    def input_password(self,password):
        self.password_inputbox.send_keys(password)

    def click_login(self):
        self.logion_button.click()

if __name__=="__main__":
    loginpage=LoginPage()
    loginpage.input_username(conf.get_username())
    loginpage.input_password(conf.get_password())
    loginpage.click_login()