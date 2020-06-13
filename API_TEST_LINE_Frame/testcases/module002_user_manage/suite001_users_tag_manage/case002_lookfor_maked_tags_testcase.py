#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc: 获取公众号已创建的标签
import unittest
from API_TEST_LINE_Frame.utils.common_api import CommonApi
from API_TEST_LINE_Frame.utils.log_utils import logutils


class LookforMakedtags(unittest.TestCase):
    def setUp(self):
        logutils.info('测试用例 [%s] 开始执行'%('获取公众号已创建的标签'))

    def tearDown(self):
        logutils.info('测试用例 [%s] 执行结束' % ('获取公众号已创建的标签'))

    def test_lookfor_maked_tags(self):
        '''
        获取公众号已创建的标签接口
        '''
        response_obj = CommonApi().look_for_makedtags()
        self.assertEqual(response_obj.json().__contains__('tags'),True)
        response_obj.close()


if __name__=="__main__":
    unittest.main()