# -*- coding utf-8 -*-
import os
import xlrd
from Project_PageObject.common.config_utils import conf

current_path=os.path.dirname(__file__)
excel_path=os.path.join(current_path,conf.get_element_infos_excel_path())

class ReadExcel:
    def __init__(self,sheet_name,excel_path=excel_path):
        self.excel_path=excel_path
        self.workbook=xlrd.open_workbook(excel_path)
        self.sheet=self.workbook.sheet_by_name(sheet_name)

    def get_element_info(self):
        element_infos={}
        for i in range(1,self.sheet.nrows):
            element_info={}
            element_info['element_name']=self.sheet.cell_value(i,1)
            element_info['locator_type']=self.sheet.cell_value(i,2)
            element_info['locator_value']=self.sheet.cell_value(i,3)
            element_info['timeout']=self.sheet.cell_value(i,4)
            element_infos[self.sheet.cell_value(i,0)]=element_info
        return element_infos
read_excel=ReadExcel('login_page')

if __name__=="__main__":
    value=read_excel.get_element_info()
    print(value)
