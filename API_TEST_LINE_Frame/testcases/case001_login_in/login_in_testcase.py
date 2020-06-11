#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import unittest
from API_TEST_LINE_Frame.utils.config_utils import conf
from API_TEST_LINE_Frame.utils.common_api import CommonApi

class LoginInTestcase(unittest.TestCase):
    def setUp(self):
        self.hosts = conf.hosts_url

    def tearDown(self):
        pass

    def test001_login_in_success(self):
        '''
        登录接口
        '''
        response_obj = CommonApi().logion_in()
        self.assertEqual(response_obj.json()['msg'],'登录成功')

    def test002_get_token(self):
        '''
        获取token
        '''
        response_obj = CommonApi().get_token()
        self.assertTrue(response_obj,True)
        return response_obj


if __name__=="__main__":
    unittest.main()
