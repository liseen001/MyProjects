#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: api_test_pytest.py
# @time: 2020/9/7 21:15
# @desc:
import warnings
import pytest
from API_TEST_FRAME.common.testdata_utils import TestdatatUtiles
from API_TEST_FRAME.common.requests_utils import RequestsUtils
from nb_log import LogManager

# case_infos = TestdatatUtiles().def_testcase_data_list_by_sql()  #取出所有测试用例数据
case_infos = TestdatatUtiles().def_testcase_data_list()
logger = LogManager(__file__).get_logger_and_add_handlers()


param_keys = ','.join(list(case_infos[0].keys()))
param_values=[]
for case_info in case_infos:
    case_id_data = case_info.get('case_id')
    case_info_data = case_info.get('case_info')
    param_values.append( (case_id_data,case_info_data) )

# for param_value in param_values:
#     print(param_value)

class TestApi:
    @pytest.mark.parametrize(param_keys,param_values)
    def test_api_common_function(self,case_id,case_info):
        print("测试用例[%s]开始执行"%(case_info[0].get("测试用例编号") + case_info[0].get("测试用例名称")))
        actual_result = RequestsUtils().request_by_step(case_info)
        assert actual_result.get('check_result'),actual_result.get('message')


if __name__ == '__main__':
    pytest.main(['-s','-v'])

