#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import os
import xlrd,ast
excel_path = os.path.join(os.path.dirname(__file__),'..','test_data/test_case.xls')
wb = xlrd.open_workbook(excel_path)
sheet = wb.sheet_by_name('Sheet1')

data = sheet.cell_value(2,17)
data1 = sheet.cell_value(2,16)
# print(data,'\n',data1)
data=data.split(';')
data1=data1.split(';')
for i in range(len(data)):
    # print(i)
    a=data[i]+data1[i]
    print(a)

