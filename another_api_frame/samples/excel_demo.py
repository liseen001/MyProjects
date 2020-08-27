#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import os
import xlrd
current_path = os.path.dirname(__file__)
test_data_path = os.path.join( current_path,'..','test_data/demo_data.xls' )
# print( test_data_path )

wb = xlrd.open_workbook( test_data_path )
sheet = wb.sheet_by_name('Sheet1')
# print( sheet.cell_value(0,0) )



def get_merged_cell_value(row_index,col_index):
    merged = sheet.merged_cells
    cell_value = None
    for ( rlow,rhigh,clow,chgih ) in merged:
        if ( row_index>=rlow and row_index<rhigh):
            if (col_index>=clow and col_index<chgih):
                cell_value = sheet.cell_value(rlow,clow)
                break;
            else:
                cell_value =sheet.cell_value( row_index,col_index )
        else:
            cell_value = sheet.cell_value( row_index,col_index )
    return cell_value

for i in range(5):
    print( get_merged_cell_value(i,3) )