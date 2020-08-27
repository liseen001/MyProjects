#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import warnings
import paramunittest
import unittest
from common.testdata_utils import TestdataUtils
from common.requests_utils import RequestsUtils
from common.config_utils import conf
from common.nblog_utils import logger

case_infos = TestdataUtils().def_testcase_data_list()  #取出所有测试用例数据
logger.info('\n\n====================================================正在获取测试用例数据====================================================\n\n')

@paramunittest.parametrized(
    *case_infos
)

class ApiTest(paramunittest.ParametrizedTestCase):
    def setUp(self):
        '''解决报警问题'''
        warnings.simplefilter( 'ignore',ResourceWarning )

    def setParameters(self, case_id, case_info):
        self.case_id = case_id
        self.case_info = case_info

    def test_api_common_function(self):
        self._testMethodName = self.case_info[0].get('测试用例编号')
        self._testMethodDoc = self.case_info[0].get('测试用例名称')
        actual_result = RequestsUtils().request_by_step( self.case_info )
        self.assertTrue(actual_result.get('check_result'), actual_result.get('message'))

    # def assert_demo(self,actual_result,except_result):
    #     self.assertIn(actual_result,except_result)



if __name__ == '__main__':
    unittest.main()
    # ApiTest().assertIn()
