# --*utf-8*--
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from Project_PageObject.common.config_utils import conf
from Project_PageObject.common.logutils import logutils
from Project_PageObject.common.base_page import BasePage
from Project_PageObject.common.base_page import basepage



class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.username_inputbox={'element_name':'用户名输入框',
                                'locator_type':'xpath',
                                'locator_value':'//input[@name="account"]',
                                'timeout':5}

        self.password_inputbox={'element_name':'输入密码',
                                'locator_type':'xpath',
                                'locator_value':'//input[@name="password"]',
                                'timeout':5}

        self.login_button={'element_name':'登录按钮',
                                'locator_type':'xpath',
                                'locator_value':'//button[@id="submit"]',
                                'timeout':5}

    def input_username(self,username):
        basepage.input(self.username_inputbox,username)
        logutils.info('输入用户名'+str(username))     #输出日志

    def input_password(self,password):
        basepage.input(self.password_inputbox,password)
        logutils.info('输入密码'+str(password))

    def click_login(self):
        basepage.click(self.login_button)
        logutils.info('点击登录按钮')



if __name__=="__main__":
    current_path = os.path.dirname(__file__)
    driver_path = os.path.join(current_path, conf.get_foxfire_path())
    driver=webdriver.Firefox(executable_path=driver_path)

    loginpage = LoginPage(driver)
    loginpage.open_url()
    loginpage.input_username('admin')
    loginpage.input_password('P1666666,')
    loginpage.click_login()