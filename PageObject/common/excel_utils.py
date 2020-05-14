#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: excel_utils.py
# @time: 2020/5/13 23:32
# @desc:
import os
import xlrd
from PageObject.common.config_utils import conf

class ExcelUtils(object):
    '''判断是否是一个excel文件再进行处理，并且文件确实存在的文件下再进行处理'''
    def __init__(self,excel_path,sheet_name=None):
        self.excel_path=excel_path
        self.sheet_name=sheet_name  #表格
        self.sheet_data=self.__get_sheet_data()   #表格所以数据,初始化的时候就调用下面的方法

    def __get_sheet_data(self):
        workbook=xlrd.open_workbook(self.excel_path)
        if self.sheet_name:   #当sheet_name没带参数时，默认取第一个表格
            sheet=workbook.sheet_by_name(self.sheet_name)
        else:
            sheet=workbook.sheet_by_index(0)
        return sheet

    '''统计行数'''
    @property
    def get_row_count(self):
        row_count=self.sheet_data.nrows
        return row_count
    '''统计列数'''
    @property
    def get_col_count(self):
        col_count=self.sheet_data.ncols
        return col_count

    '''通过列表的方式读取数据'''
    def get_sheet_data_by_list(self):
        all_excel_data=[]
        for rownum in range(self.get_row_count):
            row_excel_data=[]
            for colnum in range(self.get_col_count):
                cell_value=self.sheet_data.cell_value(rownum,colnum)
                row_excel_data.append(cell_value)
            all_excel_data.append(row_excel_data)
        return all_excel_data

    '''以字典的方式返回'''




if __name__=="__main__":
    value=ExcelUtils('main').get_sheet_data_by_list()
    for e in value:
        print(e)