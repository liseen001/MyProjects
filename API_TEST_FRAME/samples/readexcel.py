#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc: 从excel读取合并单元格
import  os
import xlrd
from API_TEST_FRAME.common.config_utils import conf

excel_path = os.path.join(os.path.dirname(__file__),'..','test_data/test_data.xlsx')
print(excel_path)

wb = xlrd.open_workbook(excel_path)
sheet = wb.sheet_by_name('Sheet1')
cell_value = sheet.cell_value(1,0)
print(cell_value)

merged =sheet.merged_cells  #返回一个列表  起始行，结束行，其实列，结束列
print(merged)
row_index =3
col_index =0

#凡是在merged_cells属性范围内的单元格  它的值都要等于左上角首个单元格的值
for (rlow,rhigh,clow,chigh) in merged:  #遍历表格中所有合并单元格位置信息
    if (row_index >= rlow and row_index < rhigh): # 行坐标判断  1<=3<5
        if (col_index >=clow and col_index < chigh):  #列坐标判断 0<=0<1
            # 如果满足条件，就把合并单元格第一个位置的值赋值给其他合并单元格
            cell_value = sheet.cell_value(rlow,clow)
print(cell_value)
#转换成方法，此方法只能取合并单元格的值
def get_merged_cell_value(row_index,col_index):
    cell_value = None
    for (rlow, rhigh ,clow ,chigh) in merged:
        if (row_index >=rlow and row_index<=rhigh):
            if (col_index >=clow and col_index < chigh):
                cell_value =sheet.cell_value(rlow,clow)
    return cell_value
print(get_merged_cell_value(2,0))
for i in range(5):
    print(get_merged_cell_value(i,3))