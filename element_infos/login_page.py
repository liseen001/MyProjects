import os
from selenium import webdriver
from selenium.webdriver.common.by import By

current=os.path.dirname(__file__)
driver_path=os.path.join(current,'../webdriver/geckodriver')


class LoginPage(object):
    def __init__(self):
        self.driver=webdriver.Firefox(executable_path=driver_path)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('http://106.53.50.202:8999/zentao6/www/user-login.html')
        self.username_inputbox=self.driver.find_element(By.XPATH,'//input[@id="account"]')
        self.password_inputbox=self.driver.find_element(By.XPATH,'//input[@name="password"]')
        self.keeplogin_checkbox=self.driver.find_element(By.XPATH, '//input[@id="keepLoginon"]')
        self.login_butons=self.driver.find_element(By.XPATH,'//button[@id="submit"]')

    def input_username(self,username):
        self.username_inputbox.send_keys(username)

    def input_password(self,password):
        self.password_inputbox.send_keys(password)

    def keep_kogin(self):
        self.keeplogin_checkbox.click()

    def click_login(self):
        self.login_butons.click()


if __name__=="__main__":
    login_page=LoginPage()
    login_page.input_username('admin')
    login_page.input_password('P1666666,'),
    login_page.keep_kogin()
    login_page.click_login()
