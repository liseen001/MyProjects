#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:修改谷歌秘钥
import unittest
import requests
from API_TEST_LINE_Frame.utils.config_utils import conf
from API_TEST_LINE_Frame.utils.common_api import CommonApi

class UpdateGooglsecretTestcase(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test003_update_googlesectet(self):
        response_obj =CommonApi().update_google_secret()
        self.assertEqual(response_obj.json()['msg'],'修改用户名成功')


if __name__ == "__main__":
    unittest.main()
