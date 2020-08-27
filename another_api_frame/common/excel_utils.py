#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:  待处理问题，自己弄的表格代码获取不了表格信息
import os
import xlrd
from xlutils.copy import copy

class ExcelUtils():
    def __init__(self,file_path,sheet_name):
        self.file_path = file_path
        self.wb = xlrd.open_workbook( self.file_path,formatting_info=True )
        self.sheet_name = sheet_name
        self.sheet = self.get_sheet()

    def get_sheet(self):
        '''通过表格名称获取sheet对象'''
        sheet = self.wb.sheet_by_name(self.sheet_name)
        return sheet

    def get_row_count(self):
        '''获取行号'''
        row_count = self.sheet.nrows
        return row_count

    def get_col_count(self):
        '''获取列号'''
        col_count = self.sheet.ncols
        return col_count

    def __get_cell_value(self,row_index,col_index):
        cell_value = self.sheet.cell_value(row_index,col_index)
        return  cell_value

    def get_merged_info(self):
        '''获取合并单元格对象'''
        merged_info = self.sheet.merged_cells
        return merged_info

    def get_merged_cell_value(self,row_index,col_index):
        '''既能获取普通单元格又能获取合并单元格信息'''
        cell_value = None
        for (rlow,rhigh,clow,chigh) in self.get_merged_info():
            if (row_index>= rlow and row_index < rhigh):
                if (col_index >= clow and col_index < chigh):
                    cell_value = self.__get_cell_value( rlow,clow )
                    break;
                else:
                    cell_value=self.__get_cell_value( row_index,col_index )
            else:
                cell_value = self.__get_cell_value( row_index,col_index )
        return cell_value

    def get_sheet_data_by_dict(self):
        '''以字典的形式返回sheet中的数据'''
        all_data_list = []
        first_row = self.sheet.row(0)
        for row in range(1,self.get_row_count()):
            row_dict = {}
            for col in range(0,self.get_col_count()):
                row_dict[first_row[col].value] = self.get_merged_cell_value( row,col )
            all_data_list.append( row_dict )
        return all_data_list

    def update_excel_data(self,row_id,col_id,content ):
        '''修改excel参数，传入行号和列号及修改内容'''
        new_wb = copy(self.wb)
        sheet = new_wb.get_sheet( self.wb.sheet_names().index(self.sheet_name) )
        sheet.write( row_id,col_id,content )
        new_wb.save(self.file_path)

    def clear_excel_colum(self,start_id,end_id,col_id):
        '''传入起始行和结束行进行删除测试结果操作，写入为空'''
        new_wb = copy(self.wb)
        sheet = new_wb.get_sheet( self.wb.sheet_names().index( self.sheet_name ) )
        for row_id in range( start_id,end_id ):
            sheet.write( row_id,col_id,'' )
        new_wb.save( self.file_path )



if __name__ == '__main__':
    current_path = os.path.dirname(__file__)
    excel_path = os.path.join( current_path,'..','test_data/test_case.xlsx' )
    excelutils =ExcelUtils(excel_path,'Sheet1')
    print( excelutils.get_sheet_data_by_dict() )
    # i = 0
    # for row in excelutils.get_sheet_data_by_dict():
    #     if row['测试用例编号'] =='case01' and row['测试用例步骤'] == 'step_01':
    #         break;
    #     else:
    #         i =i+1
    # print(i+1)
    testdatas = excelutils.get_sheet_data_by_dict()
    for j in range(len(testdatas)):
        if testdatas[j]['测试用例编号'] == 'case01' and testdatas[j]['测试用例步骤'] == 'step_01':
            break;
    print( j+1 )