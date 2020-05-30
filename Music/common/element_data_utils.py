#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import os
import xlrd
from common.config_utils import conf

current_path=os.path.dirname(__file__)
excel_path=os.path.join(current_path,'..',conf.element_infos_path)

class ELementdataUtils:
    def __init__(self,module_name,page_name,element_path=excel_path):
        self.element_path = element_path
        self.excel_path = os.path.join(self.element_path,module_name,page_name + '.xls')
        self.workbook = xlrd.open_workbook(self.excel_path)
        self.sheet = self.workbook.sheet_by_index(0)
        self.row_count = self.sheet.nrows


    def get_element_info(self):
        element_infos = {}
        for i in range(1,self.row_count):
            element_info = {}
            element_info['element_name'] = self.sheet.cell_value(i,1)
            element_info['locator_type'] = self.sheet.cell_value(i,2)
            element_info['locator_value'] = self.sheet.cell_value(i,3)
            timeout_value = self.sheet.cell_value(i,4)
            element_info['timeout'] = timeout_value if isinstance(timeout_value,float) else conf.time_out
            element_infos[self.sheet.cell_value(i,0)] = element_info
        return  element_infos
    
    
if __name__ == "__main__":
    elements = ELementdataUtils('login','login_page').get_element_info()
    for e in elements.values():
        print(e)
