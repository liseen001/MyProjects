# --*utf-8*--
from PageObject.element_infos.login.login_page import LoginPage
from PageObject.element_infos.main.main_page import MainPage
from PageObject.common.config_utils import conf



class LoginAction:
    def __init__(self,driver):
        '''实例化登录页面'''
        self.login_page=LoginPage(driver)


    '''登录动作'''
    def login_action(self,username,password):
        self.login_page.input_username(username)
        self.login_page.input_password(password)
        self.login_page.click_login()

    '''登录成功，登录成功后进入主页'''
    def login_success(self,username,passworld):
        self.login_action(username,passworld)
        return MainPage(self.login_page.driver)

    '''默认登录,传入默认登录账密'''
    def default_login(self):
        return self.login_success(conf.default_username,conf.default_password)

    '''登录失败,获取弹窗的内容'''
    def login_fail(self,username,password):
        self.login_action(username,password)
        return self.login_page.get_login_fail_alter_content()

    '''利用cookie登录，自己写'''
    def login_by_cookie(self):
        pass

