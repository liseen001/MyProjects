# --*utf-8*--
import os
import xlrd
from Test.common.config_utils import conf

current_path=os.path.dirname(__file__)
excel_path=os.path.join(current_path,conf.get_excel_path())
workbook=xlrd.open_workbook(excel_path)
sheet=workbook.sheet_by_index(0)
print(sheet.cell_value(1,2))

print(sheet.nrows,sheet.ncols)
for i in range(1,sheet.nrows):
    all_case_info=[]
    case_info=[]
    for j in range(sheet.ncols):
        case_info.append(sheet.cell_value(i,j))
        all_case_info.append(case_info)
print(all_case_info)