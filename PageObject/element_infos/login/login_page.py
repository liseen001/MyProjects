# -*- coding utf-8 -*-
from PageObject.common.browser import Browser
from PageObject.common.config_utils import conf
from PageObject.common.element_data_utils import ElementdataUtils
from PageObject.common.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self,driver):
        '''父类有self.driver的构造，子类也有这个构造，因此要显示调用父类的构造'''
        super().__init__(driver)
        '''读取表格中存储的元素识别信息，元素信息也可以放数据库或者文件中'''
        '''传入模块名（sheet）及所属页面参数,默认参数'''
        element = ElementdataUtils('login','login_page').get_element_info()
        self.__username_inputbox=element['username_inputbox']
        self.__password_inputbox=element['password_inputbox']
        self.__login_button=element['login_button']
        # self.__keep_login=element['keep_login']
        # self.__forget_password=element['forget_password']
        # self.__language_select=element['language_select']
        # self.__get_login_fail_alter_content=element['get_login_fail_alter_content']

    '''代码逻辑：元素信息（字典），调用父类中find_element方法查找相关元素，然后调用父类input_operation方法进行输入操作'''
    '''输入登录账号操作'''
    def input_username(self,username):  #方法 == 》控件的操作
        self.input_operation(self.__username_inputbox,username)

    '''输入登录密码操作'''
    def input_password(self,password):
        self.input_operation(self.__password_inputbox,password)

    '''调用父类点击操作'''

    def click_login(self):
        self.click_operation(self.__login_button)
    '''点击忘记密码'''

    def click_forget_password(self):
        self.click_operation(self.__forget_password)

    def get_login_fail_alter_content(self):
        return self.switch_to_alter()



if __name__=="__main__":
    driver= Browser().get_default_driver()
    login_page=LoginPage(driver)
    login_page.open_url(conf.url)
    login_page.input_username(conf.zengtao_username)
    login_page.input_password(conf.zentao_password)
    login_page.click_login()
    login_page.wait(2)
    login_page.screen_shoot_as_file()



