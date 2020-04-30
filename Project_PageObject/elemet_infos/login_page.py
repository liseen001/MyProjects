# --*utf-8*--
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from Project_PageObject.common.config_utils import conf
from Project_PageObject.common.logutils import logutils

current_path= os.path.dirname(__file__)
driver_path=os.path.join(current_path,conf.get_foxfire_path())

class LoginPage(object):
    def __init__(self):
        self.driver=webdriver.Firefox(executable_path=driver_path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(conf.get_zend_path())
        self.username_inputbox=self.driver.find_element(By.XPATH,'//input[@name="account"]')
        self.password_inputbox=self.driver.find_element(By.XPATH,'//input[@name="password"]')
        self.logion_button=self.driver.find_element(By.XPATH,'//button[@id="submit"]')
        self.keeplogin_checkbox=self.driver.find_element(By.XPATH,'//input[@id="keepLoginon"]')

    def input_username(self,username):
        self.username_inputbox.send_keys(username)
        logutils.info('输入用户名'+str(username))     #输出日志

    def input_password(self,password):
        self.password_inputbox.send_keys(password)
        logutils.info('输入密码'+str(password))

    def click_login(self):
        self.logion_button.click()
        logutils.info('点击登录按钮')

loginpage=LoginPage()

if __name__=="__main__":
    loginpage.input_username(conf.get_username())
    loginpage.input_password(conf.get_password())
    loginpage.click_login()