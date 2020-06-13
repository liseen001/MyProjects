#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:   测试获取token是否通过
import unittest
from API_TEST_LINE_Frame.utils.log_utils import logutils
from API_TEST_LINE_Frame.utils.common_api import CommonApi

class GetAccessToken(unittest.TestCase):
    def setUp(self):
        logutils.info('测试用例 [%s] 开始执行' % ('获取access_token接口测试'))

    def tearDown(self):
        logutils.info('测试用例 [%s] 执行完毕' % ('获取access_token接口测试'))

    def test001_get_access_token_success(self):
        '''
        获取token接口
        '''
        response_obj = CommonApi().get_access_token()
        self.assertEqual(response_obj.json()['expires_in'],7200)



if __name__=="__main__":
    unittest.main()
