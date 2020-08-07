#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import os
import xlrd
currtent_path = os.path.dirname(__file__)
exlce_path = os.path.join(currtent_path,r'C:\Users\Administrator\Desktop\test.xls')
print(exlce_path)

wb=xlrd.open_workbook(exlce_path)
print(wb)
sheet=wb.sheet_by_name('Sheet1')
merged =  sheet.merged_cells
# row_index = sheet.nrows ;  clos_index=sheet.ncols

# for (rlow,rhigh,clow,chigh) in merged:
#     if (row_index>=rlow and row_index < rhigh):
#         if (clos_index >=clow and clos_index<chigh):
#             cell_value = sheet.cell_value(rlow,clow)
# print(cell_value)

def get_merged_cell_value(row_index,col_index):
    cell_value = None
    for ( rlow,rhigh,clow,chigh ) in merged:
        if (row_index >= rlow and row_index < rhigh):
            if ( col_index>=clow and col_index <chigh ):
                cell_value = sheet.cell_value( rlow,clow )
                break;
            else:
                cell_value = sheet.cell_value(row_index,col_index)
    return  cell_value

if __name__ == '__main__':
    for i in range(5):
        print(get_merged_cell_value(i,3))