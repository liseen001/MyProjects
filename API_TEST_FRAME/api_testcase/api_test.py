#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: api_test.py
# @time: 2020/8/12 22:45
# @desc:  参数化测试
'''
思路：1、先取出数据
'''
import warnings
import  paramunittest
import unittest
from API_TEST_FRAME.common.testdata_utils import TestdatatUtiles
from API_TEST_FRAME.common.requests_utils import RequestsUtils

case_infos = TestdatatUtiles().def_testcase_data_list()  #取出所有测试用例数据

@paramunittest.parametrized(
    *case_infos
)

class ApiTest(paramunittest.ParametrizedTestCase):
    def setUp(self):
        '''解决报警问题'''
        warnings.simplefilter( 'ignore',ResourceWarning )

    def setParameters( self, case_id, case_info ):
        self.case_id = case_id  #转入内部
        self.case_info = case_info

    def test_api_common_function(self):
        '''测试描述'''
        self._testMethodName = self.case_info[0].get("测试用例编号")
        self._testMethodDoc = self.case_info[0].get("测试用例名称")
        actual_result = RequestsUtils().request_by_step( self.case_info )
        # print( actual_result )
        self.assertTrue( actual_result.get('check_result'),actual_result.get('message') )  #将check_result与message进行断言比对



if __name__ == '__main__':
    unittest.main()