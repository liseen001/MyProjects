#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:   测试获取token是否通过
import unittest
from API_TEST_LINE_Frame.utils.config_utils import conf
from API_TEST_LINE_Frame.utils.common_api import CommonApi

class GetAccessToken(unittest.TestCase):
    def setUp(self):
        self.hosts = conf.hosts_url

    def tearDown(self):
        pass

    def test001_get_access_token_success(self):
        '''
        获取token接口
        '''
        response_obj = CommonApi().get_access_token()
        self.assertEqual(response_obj.json()['expires_in'],7200)



if __name__=="__main__":
    unittest.main()
