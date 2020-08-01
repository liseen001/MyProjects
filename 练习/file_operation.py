#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import os
import xlrd

file_path_01 = r'C:\Users\Administrator\Desktop\opencagent\photo\h5lunbo\\'
file_path_02= r'C:\Users\Administrator\Desktop\opencagent\photo\h5youhui\rukou\\'

# for filename01 in os.listdir(file_path_01):
#     for filename02 in os.listdir(file_path_02):
#         image_path1 = os.path.join(file_path_01, filename01)
#         image_pat2=os.path.join(file_path_02,filename02)
#         count=0
#         for i in  len(os.listdir(file_path_01)):
#             count +=i
#             image_pat2=image_pat2[i]
#     print( image_path1,image_pat2 )

# for i in  os.listdir(file_path_01):
#     list=[i]
#     lista=list[int(i)]
#     print(lista)

wb=xlrd.open_workbook(r'C:\Users\Administrator\Desktop\newadmin\dtqp.xls','r')
sheet1 = wb.sheet_by_name('dtqp')
print(sheet1.cell_value(0,0))
# for col in sheet1.gridline_colour_index:
#     print(col)

for i in range(sheet1.ncols):
        print(sheet1.cell_value(i,2))


