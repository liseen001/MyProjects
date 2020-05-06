# --*utf-8*--
import os
from selenium import webdriver
from Project_PageObject.common.config_utils import conf
from Project_PageObject.common.logutils import logutils
from Project_PageObject.common.base_page import BasePage
from Project_PageObject.common.read_excel import ReadExcel
from Project_PageObject.common.browser import browser

class LoginPage(BasePage):
    def __init__(self,driver):
        '''父类有self.driver的构造，子类也有这个构造，因此要显示调用父类的构造'''
        super().__init__(driver)
        '''元素的识别信息，可以放数据库或者文件中'''
        elements=ReadExcel('login_page').get_element_info()
        self.username_inputbox=elements['username_inputbox']
        self.password_inputbox=elements['password_inputbox']
        self.login_button=elements['login_button']


    #代码逻辑：这是一个元素信息（字典），首先调用父类input方法，首先会调用find_element方法查找元素
    def input_username(self,username):
        self.input( self.username_inputbox,username )        #输入元素信息字典与对应的元素的内容：content
        logutils.info('输入用户名'+str(username))     #输出日志,这些位置最好不要加日志，都加在父类

    def input_password(self,password):
        self.input(self.password_inputbox,password)
        logutils.info('输入密码'+str(password))

    def click_login(self):
        self.click(self.login_button)
        logutils.info('点击登录按钮')

if  __name__=="__main__":
    '''打开浏览器，显示构造,调用browser类中的构造属性，当方法用，不用加括号driver'''
    driver=browser.get_driver()

    loginpage = LoginPage(driver)   #实例化driver操作
    loginpage.open_url('http://106.53.50.202:8999/zentao6/www/user-login.html')  #调用父类中打开浏览器的方法
    loginpage.input_username(conf.get_username())   #调用字类输入用户名的方法输入用户名
    loginpage.input_password(conf.get_password())
    loginpage.click_login()