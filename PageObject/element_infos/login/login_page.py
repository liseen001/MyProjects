# -*- coding utf-8 -*-
from PageObject.common.browser import browser
from PageObject.common.config_utils import conf
from PageObject.common.read_excel import ReadExcel
from PageObject.common.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self,driver=browser.get_default_driver):
        '''父类有self.driver的构造，子类也有这个构造，因此要显示调用父类的构造'''
        super().__init__(driver)
        '''读取表格中存储的元素识别信息，元素信息也可以放数据库或者文件中'''
        '''传入模块名（sheet）及所属页面参数,默认参数'''
        element=ReadExcel('login','login_page').get_element_info()
        self.__username_inputbox=element['username_inputbox']
        self.__password_inputbox=element['password_inputbox']
        self.__login_button=element['login_button']
        self.__keep_login=element['keep_login']
        self.__forget_password=element['forget_password']
        self.__language_select=element['language_select']

    '''代码逻辑：元素信息（字典），调用父类中find_element方法查找相关元素，然后调用父类input_operation方法进行输入操作'''
    '''输入登录账号操作'''
    def inuput_username(self,username):
        self.input_operation(self.__username_inputbox,username)

    '''输入登录密码操作'''
    def input_password(self,password):
        self.input_operation(self.__password_inputbox,password)

    '''调用父类点击操作'''
    @property
    def click_login(self):
        self.click_operation(self.__login_button)

    @property
    def clic_forget_password(self):
        self.click_operation(self.__forget_password)


loginpage=LoginPage()
if __name__=="__main__":
    '''调用父类中打开浏览器的方法，传入url'''
    loginpage.open_url(conf.zend_path)
    loginpage.inuput_username(conf.zengtao_username)
    loginpage.input_password(conf.zentao_password)
    loginpage.clic_forget_password
    loginpage.set_browser_back
    loginpage.input_password(conf.zentao_password)
    loginpage.click_login
    loginpage.set_browser_quit
