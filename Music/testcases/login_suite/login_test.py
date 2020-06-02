#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import unittest
from Music.common.browser import Browser
from Music.common.base_page import BasePage
from Music.actions.login_action import LoginAction
from Music.common.config_utils import conf
from Music.common.selenium_base_case import SeleniumBaseCase
from Music.common.test_data_utils import TestDataUtils


class LoginTest(SeleniumBaseCase):
    '''登录测试类'''
    test_class_data = TestDataUtils('login_suite','login_test').convert_excedata_to_testdata()

    def setUp(self):
        super().setUp()

    @unittest.skipIf(test_class_data['test_login_success']['isnot'],'')
    def test_login_success(self):
        test_function_data = self.test_class_data['test_login_success']
        self._testMethodDoc = test_function_data['test_name']
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.login_success(test_function_data['test_parameter'].get('username'),test_function_data['test_parameter'].get('password'))
        actual_result = main_page.get_more_text()
        self.assertEqual(actual_result,test_function_data['excepted_result'],'test_login_success用例执行失败')

    def test_login_fail(self):
        test_function_data = self.test_class_data['test_login_fail']
        self._testMethodDoc = test_function_data['test_name']
        login_action = LoginAction(self.base_page.driver)
        actual_result = login_action.login_fail(test_function_data['test_parameter'].get('username'),test_function_data['test_parameter'].get('password'))
        print(actual_result)   ##
        self.assertEqual(actual_result,test_function_data['excepted_result'])

if __name__=="__main__":
    unittest.main()