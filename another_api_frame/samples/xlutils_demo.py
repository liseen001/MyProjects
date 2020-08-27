#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import os
import xlrd
from xlutils.copy import copy
excel_utils_path = os.path.join( os.path.dirname(__file__),'..','test_data/demo_data.xls' )
print( excel_utils_path )
wb = xlrd.open_workbook( excel_utils_path,formatting_info=True )
sheet=wb.sheet_by_name('Sheet1')
print( sheet.cell_value(0,0) )

new_workbook = copy(wb)

sheet = new_workbook.get_sheet( wb.sheet_names().index('Sheet1') )
sheet.write(0,0,'事件aaa')
new_workbook.save(excel_utils_path)