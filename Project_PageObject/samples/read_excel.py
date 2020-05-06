# --*utf-8*--
import os
import xlrd
from Project_PageObject.common.config_utils import conf

current_path=os.path.dirname(__file__)
element_infos_excel_path=os.path.join(current_path,conf.get_element_infos_excel_path())

workbook=xlrd.open_workbook(element_infos_excel_path)
'''通过sheet名字获取'''
sheet=workbook.sheet_by_name('login_page')
'''定义一个对象获取所有login_page中的信息'''
element_infos={}
for i in range(1,sheet.nrows):
    element_info={}
    element_info['element_name']=sheet.cell_value(i,1)
    element_info['locator_type']=sheet.cell_value(i,2)
    element_info['locator_value']=sheet.cell_value(i,3)
    element_info['time_out']=sheet.cell_value(i,4)
    element_infos[sheet.cell_value(i,0)]=element_info
print(element_infos)