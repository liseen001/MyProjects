#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc: 编辑标签
import unittest
from API_TEST_LINE_Frame.utils.common_api import CommonApi
from API_TEST_LINE_Frame.utils.log_utils import logutils

class UpdateMakedtags(unittest.TestCase):
    def setUp(self):
        logutils.info('测试用例 [%s] 开始执行' % ('获取编辑标签接口测试'))
    def tearDown(self):
        logutils.info('测试用例 [%s] 执行完毕' % ('获取编辑标签接口测试'))

    def test_update_maked_tags(self):
        '''
        编辑标签接口
        '''
        response_obj = CommonApi().edit_tags()
        self.assertEqual(response_obj.json()['errmsg'],"ok")


if __name__=="__main__":
    unittest.main()