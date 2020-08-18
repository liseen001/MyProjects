#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:  封装读取表格数据
import os
import xlrd
from xlutils.copy import copy
from API_TEST_FRAME.common.config_utils import conf

class ExcelUtils():
    def __init__(self,file_path,sheet_name):
        self.file_path = file_path
        self.wb = xlrd.open_workbook( self.file_path,formatting_info=True )
        self.sheet_name = sheet_name
        self.sheet = self.get_sheet()  #整个表格对象，反向调用，构造里面调取下面的方法


    def get_sheet(self):
        sheet = self.wb.sheet_by_name(self.sheet_name)
        return sheet
    
    def get_row_count(self):
        row_count = self.sheet.nrows
        return row_count
    
    def get_col_count(self):
        col_count = self.sheet.ncols
        return col_count

    def __get_cell_value(self,row_index,col_index):
        cell_value = self.sheet.cell_value(row_index,col_index)
        return  cell_value
    
    def get_merged_info(self):
        merged_info = self.sheet.merged_cells
        return merged_info
    
    def get_merged_cell_value(self,row_index, col_index):
        '''既能获取普通单元格，又能获取合并单元格数据'''
        cell_value = None
        for (rlow,rhigh,clow,chigh) in self.get_merged_info():
            if (row_index >= rlow and row_index < rhigh):
                if (col_index >= clow and col_index < chigh):
                    cell_value = self.__get_cell_value(rlow,clow)
                    break;
                else:
                    cell_value =self.__get_cell_value(row_index,col_index)
            else:
                cell_value = self.__get_cell_value(row_index,col_index)
        return cell_value

    def get_sheet_data_by_dict(self):
        all_data_list = []
        first_row = self.sheet.row(0)  #取首行数据
        for row in range(1,self.get_row_count()):
            row_dict = {}
            for col in range(0,self.get_col_count()):
                row_dict[first_row[col].value] = self.get_merged_cell_value(row,col)
            all_data_list.append(row_dict)
        return all_data_list

    def update_excel_data(self,row_id,col_id,content):
        '''修改excel参数，传入行号列号和修改内容'''
        new_wb = copy(self.wb)
        sheet = new_wb.get_sheet( self.wb.sheet_names().index( self.sheet_name ) )
        sheet.write( row_id,col_id,content )
        new_wb.save(self.file_path)

    def clear_excel_colum(self,start_id,end_id,col_id):
        '''传入起始和结束行进行删除操作，写入为空'''
        new_wb = copy(self.wb)
        sheet = new_wb.get_sheet( self.wb.sheet_names().index(self.sheet_name) )
        for row_id in range(start_id,end_id):
            sheet.write( row_id,col_id,'' )
        new_wb.save( self.file_path )





if __name__ =="__main__":
    current_path = os.path.dirname(__file__)
    excel_path = os.path.join(current_path,conf.case_data_path)
    # print(excel_path)
    excelutils= ExcelUtils(excel_path,'Sheet1')
    print(excelutils.get_sheet_data_by_dict())
    # print( excelutils.get_merged_cell_value(4,0) )
    # for row in excelutils.get_sheet_data_by_dict():
    #     print(row)
    # print( excelutils.get_merged_cell_value(3,0) )
    # excelutils.update_excel_data( 2,14,'liseen' )