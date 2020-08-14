#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: xlutils_demo.py
# @time: 2020/8/14 22:11
# @desc:
import os
import xlrd
from xlutils.copy import copy

excle_path = os.path.join( os.path.dirname(__file__),'test_data.xls' )
# print( excle_path )

'''
创建工作部对象，formatting_info=True用于保存修改后的excel格式不错乱
，xlrd不支持这个，只支持2003,把文件另存为2003模式即可
'''
wb = xlrd.open_workbook( excle_path,formatting_info=True) #
# sheet1= wb.sheet_by_name('Sheet1')
# print( sheet1.cell_value(0,0) )
new_workbook = copy(wb)  # new_workbook 已经变成可写的对象 xlwt 对象

sheet = new_workbook.get_sheet(0)  #获取第一个单元表格
sheet.write(1,3,60)    #1,3为单元格位置，60为单元格被修改的信息
new_workbook.save(excle_path)  #保存修改