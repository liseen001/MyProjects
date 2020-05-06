# -*- coding utf-8 -*-
import os
import xlrd
from Music.common.confing_utils import conf

current_path=os.path.dirname(__file__)
'''调用配置封装类中的get_excel_path方法'''
excel_path=os.path.join(current_path,conf.get_excel_path())

class ReadExcel:
    def __init__(self):
        '''创建一个表格对象，对象打开的路径来excel_path存放表格的位置'''
        self.workbook=xlrd.open_workbook(conf.get_excel_path())
        '''创建一个表单元对象，对象获取下表为0的sheet'''
        self.sheet=self.workbook.sheet_by_index(0)

    '''创建获取表格内容的方法'''
    def get_excel(self):
        '''定义列表，获取sheet中所有的信息'''
        all_case_infos=[]
        '''表行从第二行开始，第一行为摘要信息'''
        for i in range(1,self.sheet.nrows):
            case_info=[]
            for j in range(self.sheet.ncols):
                '''case_info列表中获取i,j中的信息'''
                case_info.append(self.sheet.cell_value(i,j))
                '''case_info中逐步获取的信息追加到all_case_infos列表中'''
                all_case_infos.append(case_info)
            return all_case_infos

'''创建读取表格的对象,外部可以通过引入这个对象直接调取类里面的方法'''
read_excel=ReadExcel()

if __name__=="__main__":
    value=read_excel.get_excel()
    print(value)
