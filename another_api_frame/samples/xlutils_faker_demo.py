#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import os,json
import xlrd
import ast
import re
import string
from xlutils.copy import copy
from samples.faker_demo import faker
from common.config_utils import conf
from common.nblog_utils import logger
from tkinter import messagebox



class WriteFakerTestdatas():
    def __init__(self):
        self.excel_path = conf.case_data_path
        self.excel_path = os.path.join(os.path.dirname(__file__), self.excel_path)
        self.wb = xlrd.open_workbook(self.excel_path, formatting_info=True)
        self.new_wb = copy(self.wb)
        self.sheet = self.new_wb.get_sheet(self.wb.sheet_names().index( conf.sheet_name ))



    def get_cell_info(self,row_index,col_index):
        '''获取单元格信息，包括合并单元格'''
        sheet = self.wb.sheet_by_name(conf.sheet_name)
        merged_info = sheet.merged_cells
        cell_value = None
        for (rlow,rhigh,clow,chigh) in merged_info:
            if ( row_index<=rlow and row_index<rhigh ):
                if (col_index>=clow and col_index<chigh):
                    cell_value = sheet.cell_value( rlow,clow )
                    break;
                else:
                    cell_value = sheet.cell_value( row_index,col_index )
            else:
                cell_value = sheet.cell_value(row_index,col_index)
        return cell_value


    def write_to_excel(self,row_index,col_index,content=None):
        '''写入到固定的单元格，通过键写入'''
        upadte_info = content
        self.sheet.write(row_index, col_index,str(upadte_info))
        self.new_wb.save(self.excel_path)
        return content

    # def write_to_excel_new(self):
    #     sheet = self.wb.sheet_by_name(conf.sheet_name)
    #     dict = sheet.cell_value(13,0)
    #     print(dict)
    #     dict=ast.literal_eval(dict)
    #     print(dict)
    #     for k, v in dict.items():
    #         v = eval(v)
    #         dict=dict.update({k:v})
    #     self.sheet.write(13,0,dict)
    #     self.new_wb.save(self.excel_path)
    #     return dict






    '''
    1、获取单元格信息
    2、修改数据
    现获取需要修改数据的行列，取出需要修改的数据，默认为字典，然后用字典中update的方法 dict = {"name":"ss"} dict.update(name='heh') 修改数据
    3、修改多个键的情况  获取字典键值，用过键值替换数据，保存数据
    '''
writefakertestdatas = WriteFakerTestdatas()
if __name__ == '__main__':
    # print( writefakertestdatas.write_to_excel(13,0,{'name':faker.create_random_name,'card_num':faker.create_randon_ssn}),
    # writefakertestdatas.write_to_excel(14,0,{'name':faker.create_random_name,'card_num':faker.create_randon_ssn}),
    # writefakertestdatas.write_to_excel(15, 0,{'name':faker.create_random_name,'card_num':faker.create_randon_ssn}),
    # writefakertestdatas.write_to_excel(16, 0,{'name':faker.create_random_name,'card_num':faker.create_randon_ssn}),
    # writefakertestdatas.write_to_excel(17, 0,{'name':faker.create_random_name,'card_num':faker.create_randon_ssn}),
    # writefakertestdatas.write_to_excel(18, 0,{'name':faker.create_random_name,'card_num':faker.create_randon_ssn}),
    # writefakertestdatas.write_to_excel(19, 0, {'name':faker.create_random_name,'card_num':faker.create_randon_ssn}),
    # writefakertestdatas.write_to_excel(14, 1,{'name':faker.create_random_name,'card_num':faker.create_randon_ssn}),
    # writefakertestdatas.write_to_excel(15, 1,{'name':faker.create_random_name,'card_num':faker.create_randon_ssn}),
    # writefakertestdatas.write_to_excel(16, 1, {'name':faker.create_random_name,'card_num':faker.create_randon_ssn}),
    # writefakertestdatas.write_to_excel(17, 1, {'name':faker.create_random_name,'card_num':faker.create_randon_ssn}),
    # writefakertestdatas.write_to_excel(18, 1, {'name':faker.create_random_name,'card_num':faker.create_randon_ssn}),
    # writefakertestdatas.write_to_excel(19, 1,{'name':faker.create_random_name,'card_num':faker.create_randon_ssn}) )
    print('hello')








