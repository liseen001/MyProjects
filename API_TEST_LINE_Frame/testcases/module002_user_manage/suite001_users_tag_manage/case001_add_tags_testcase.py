#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:  创建标签
import unittest
from API_TEST_LINE_Frame.utils.config_utils import conf
from API_TEST_LINE_Frame.utils.common_api import CommonApi
from API_TEST_LINE_Frame.utils.log_utils import logutils

class AddTags(unittest.TestCase):
    def setUp(self):
        self.hosts= conf.hosts_url
    def tearDown(self):
        pass

    def test_add_tags_success(self):
        '''
        创建标签接口
        '''
        response_obj =CommonApi().add_tags()
        self.assertEqual(response_obj.status_code,200)



if __name__ =="__main__":
    unittest.main()