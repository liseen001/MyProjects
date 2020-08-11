#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: excle数据应用.py
# @time: 2020/8/11 22:38
# @desc:
#使用excel数据驱动  requests_utils   使用case_info
from API_TEST_FRAME.common.testdata_utils import TestdatatUtiles
from API_TEST_FRAME.common.requests_utils import RequestsUtils

all_case_info =TestdatatUtiles().def_testcase_data_list()
# case_info = all_case_info[0].get('case_info')
# print( case_info )
# RequestsUtils().request_by_step( case_info )

for case_info in all_case_info:
    RequestsUtils().request_by_step( case_info.get( 'case_info' ) )