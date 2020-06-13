#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc: 删除标签
import unittest
from API_TEST_LINE_Frame.utils.common_api import CommonApi
from API_TEST_LINE_Frame.utils.log_utils import logutils

class DeleteTags(unittest.TestCase):
    def setUp(self):
        logutils.info('测试用例 [%s] 开始执行' % ('删除标签接口测试'))
    def tearDown(self):
        logutils.info('测试用例 [%s] 执行完毕' % ('删除标签接口测试'))

    def test_delete_tags(self):
        '''
        删除创建的标签接口
        '''
        response_onj = CommonApi().delete_tags()
        self.assertEqual(response_onj.json()['errcode'],0)
