# --*utf-8*--
import os
from selenium import webdriver
from Project_PageObject.common.config_utils import conf
from Project_PageObject.common.logutils import logutils
from Project_PageObject.common.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)    #父类有self.driver的构造，子类也有这个构造，因此要显示调用父类的构造
        '''元素的识别信息，可以放数据库或者文件中'''
        self.username_inputbox={'element_name':'用户名输入框',  #元素名字
                                'locator_type':'xpath',#元素的定位方式
                                'locator_value':'//input[@name="account"]',  #元素定位的值
                                'timeout':5}   #超时时间

        self.password_inputbox={'element_name':'输入密码',
                                'locator_type':'xpath',
                                'locator_value':'//input[@name="password"]',
                                'timeout':5}

        self.login_button={'element_name':'登录按钮',
                                'locator_type':'xpath',
                                'locator_value':'//button[@id="submit"]',
                                'timeout':5}
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
    '''打开浏览器，显示构造driver'''
    current_path = os.path.dirname(__file__)
    driver_path = os.path.join(current_path, conf.get_foxfire_path())
    driver=webdriver.Firefox(executable_path=driver_path)

    loginpage = LoginPage(driver)   #实例化driver操作
    loginpage.open_url('http://106.53.50.202:8999/zentao6/www/user-login.html')  #调用父类中打开浏览器的方法
    loginpage.input_username(conf.get_username())   #调用字类输入用户名的方法输入用户名
    loginpage.input_password(conf.get_password())
    loginpage.click_login()