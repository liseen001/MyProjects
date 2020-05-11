# --*utf-8*--
import unittest
from PageObject.common.browser import browser
from PageObject.actions.login_action import LoginAction
from PageObject.common.base_page import BasePage
from PageObject.common.config_utils import conf
from PageObject.element_infos.main.main_page import mainpage

class LoginTest(unittest.TestCase):
    def setUp(self):
        '''做一个basepage对象'''
        self.base_page=BasePage(browser.get_default_driver())
        '''浏览器最大化'''
        self.base_page.set_browser_max()
        '''隐式等待'''
        self.base_page.implicitly_wait()
        '''打开禅道网址'''
        self.base_page.open_url(conf.zend_path)

    def tearDown(self):
        self.base_page.close_tab()

    '''登录成功'''
    def test_login_success(self):
        login_action=LoginAction(self.base_page.driver)
        login_action.login_success(conf.zengtao_username,conf.default_password)
        actual_result=mainpage.get_usrname()
        self.assertEqual(actual_result,'admin','test_login_success用例执行失败')

    '''登录失败'''
    def test_login_fail(self):
        login_action=LoginAction(self.base_page.driver)
        actual_result=login_action.login_fail('sss','213123')
        print('actual_result%s'%actual_result)
        self.assertEqual(actual_result,'登录失败，请检查您的用户名或密码是否填写正确。')
if __name__=="__main__":
    unittest.main()