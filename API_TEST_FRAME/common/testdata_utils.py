#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:  获取测试数据返回想要的数据格式
import os
from API_TEST_FRAME.common.excel_utils import ExcelUtils
from API_TEST_FRAME.common.config_utils import conf
from API_TEST_FRAME.common.sql_utils import SqlUtils

current_path = os.path.dirname(__file__)
test_data_path = os.path.join(current_path,conf.case_data_path)
# print(test_data_path)

class TestdatatUtiles():
    def __init__(self,test_data_path=test_data_path):
        self.test_data_path=test_data_path
        self.test_data_sheet = ExcelUtils( test_data_path,'Sheet1' )
        self.test_data = self.test_data_sheet.get_sheet_data_by_dict()
        self.test_data_by_mysql = SqlUtils().get_mysql_test_case_info()

    def __get_testcase_data_dict(self):
        testcase_dict = {}
        for row_data in self.test_data:
            if row_data['用例执行'] == '是':
                testcase_dict.setdefault( row_data['测试用例编号'],[]).append( row_data )
        return  testcase_dict

    def def_testcase_data_list(self):
        testcase_list = []
        for k,v in self.__get_testcase_data_dict().items():
            one_case_dict = {}
            one_case_dict['case_id'] = k
            one_case_dict['case_info'] = v
            testcase_list.append(one_case_dict)
        return tuple(testcase_list)   #以元组的方式返回数据  安全性

    def __get_testcase_data_dict_by_mysql(self):
        testcase_dict = {}
        for row_data in self.test_data_by_mysql:
            testcase_dict.setdefault( row_data['测试用例编号'],[]).append( row_data )
        return  testcase_dict

    def def_testcase_data_list_by_sql(self):
        testcase_list = []
        for k,v in self.__get_testcase_data_dict_by_mysql().items():
            one_case_dict = {}
            one_case_dict['case_id'] = k
            one_case_dict['case_info'] = v
            testcase_list.append(one_case_dict)
        return tuple(testcase_list)

    def get_row_num(self,case_id,case_step_name):
        '''通过用例编号与步骤获取行号用于将测试结果反写入数据到指定的行，列是固定的'''
        for j in range(len(self.test_data)):
            if self.test_data[j]['测试用例编号'] == case_id and self.test_data[j]['测试用例步骤'] == case_step_name:
                break
        return j+1

    def get_result_id(self):
        '''并获取测试结果的列号写入测试结果'''
        for col_id in range( len(self.test_data_sheet.sheet.row(0)) ):
            if self.test_data_sheet.sheet.row(0)[col_id].value == '测试结果':
                break
        return col_id

    def write_result_to_excel(self,case_id,case_step_name,content='通过'):
        '''把测试结果写入excel'''
        row_id = self.get_row_num(case_id,case_step_name)
        col_id = self.get_result_id()
        self.test_data_sheet.update_excel_data( row_id,col_id,content )  #列号为固定值


    def clear_result_from_excel(self):
        '''清空测试结果'''
        col_id = self.get_result_id()
        row_count = self.test_data_sheet.get_row_count() #获取sheet行
        self.test_data_sheet.clear_excel_colum(1,row_count,col_id)




if __name__ == "__main__":
    testdatautils = TestdatatUtiles()
    # for i in testdatautils.def_testcase_data_list_by_sql():
    #     print(i)
    # testdatautils.write_result_to_excel('case03','step_02')
    testdatautils.clear_result_from_excel()