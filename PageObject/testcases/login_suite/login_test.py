# --*utf-8*--
import unittest
from PageObject.common.browser import Browser
from PageObject.actions.login_action import LoginAction
from PageObject.common.base_page import BasePage
from PageObject.common.config_utils import conf
from PageObject.element_infos.main.main_page import MainPage
from PageObject.common.selenium_base_case import SeleniumBaseCase

class LoginTest(SeleniumBaseCase):
    def setUp(self):
        '''如果遇到需要单独写的东西可以在运行代码中的setup里面 刷新操作'''
        '''调用父类的setUp'''
        super().setUp()

    '''登录成功'''
    @unittest.skipIf(True,'')  #判断测试用例是否执行,满足条件则跳过执行用例
    def test_login_success(self):
        login_action=LoginAction(self.base_page.driver)
        mainpage=login_action.login_success(conf.zengtao_username,conf.default_password)
        actual_result=mainpage.get_usrname()
        self.assertEqual(actual_result,'admin','test_login_success用例执行失败')

    '''登录失败'''
    def test_login_fail(self):
        login_action=LoginAction(self.base_page.driver)
        actual_result=login_action.login_fail('sss','213123')
        self.assertEqual(actual_result,'登录失败，请检查您的用户名或密码是否填写正确。','test_login_fail用例执行失败')
if __name__=="__main__":
    unittest.main()