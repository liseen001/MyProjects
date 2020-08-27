#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc: 封装测试数据格式,获取测试数据返回想要的数据格式
import os
from common.config_utils import conf
from common.excel_utils import ExcelUtils

test_data_path = os.path.join( os.path.dirname(__file__),conf.case_data_path )
# print( test_data_path )

class TestdataUtils():
    def __init__(self,test_data_path = test_data_path):
        self.test_data_path = test_data_path
        self.test_data_sheet = ExcelUtils( test_data_path,conf.sheet_name )
        self.test_data = self.test_data_sheet.get_sheet_data_by_dict()



    def __get_testcase_data_dict(self):
        testcase_dict = {}
        for row_data in self.test_data:
            if row_data['用例执行'] == '是':
                testcase_dict.setdefault( row_data['测试用例编号'],[] ).append( row_data )
        return  testcase_dict

    def def_testcase_data_list(self):
        testcase_list = []
        for k , v in self.__get_testcase_data_dict().items():
            one_case_dict = {}
            one_case_dict['case_id'] = k
            one_case_dict['case_info'] = v
            testcase_list.append( one_case_dict )
        return tuple( testcase_list )

    def get_row_num(self,case_id,case_step_name):
        '''通过用例编号与步骤获取行号用于将测试结果反写入数据到指定的行'''
        for j in range(len(self.test_data)):
            if self.test_data[j]['测试用例编号'] == case_id and self.test_data[j]['测试用例步骤'] == case_step_name:
                break
        return j+1


    def get_result_id(self):
        '''获取测试结果列的列号写入测试结果'''
        for col_id in range( len(self.test_data_sheet.sheet.row(0)) ):
            if self.test_data_sheet.sheet.row(0)[col_id].value =='测试结果':
                break
        return col_id

    def write_result_to_excel(self,case_id,case_step_name,content='通过'):
        '''把测试结果写入excel'''
        row_id = self.get_row_num( case_id ,case_step_name )
        col_id = self.get_result_id()
        self.test_data_sheet.update_excel_data( row_id,col_id,content )

    def clear_result_from_excel(self):
        '''清空测试结果'''
        col_id = self.get_result_id()
        row_count = self.test_data_sheet.get_row_count()  #获取sheet行
        self.test_data_sheet.clear_excel_colum( 1,row_count,col_id )

if __name__ == '__main__':
    testdata = TestdataUtils()
    for i in testdata.def_testcase_data_list():
        print( i )