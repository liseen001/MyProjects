# --*utf-8*--
import os
import xlrd
from Test.common.config_utils import conf

current_path=os.path.dirname(__file__)
excel_path=os.path.join(current_path,conf.get_excel_path())

class ReadExcel:
    def __init__(self):
        self.workbook=xlrd.open_workbook(conf.get_excel_path())
        self.sheet=self.workbook.sheet_by_index(0)

    def get_excel(self):
        all_case_infos=[]
        for i in range(1,self.sheet.nrows):
            case_info=[]
            for j in range(self.sheet.ncols):
                case_info.append(self.sheet.cell_value(i,j))
                all_case_infos.append(case_info)
        return  all_case_infos

read_excel=ReadExcel()

if __name__=="__main__":
    value=read_excel.get_excel()
    print(value)

