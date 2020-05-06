# -*- coding utf-8 -*-
import os
import xlrd
'''从配置文件类中导入conf=ConfigUtils()对象conf'''
from Project_PageObject.common.config_utils import conf

current_path=os.path.dirname(__file__)
'''调用配置封装类中获取元素信息文件路径的方法传入路径'''
excel_path=os.path.join(current_path,conf.get_element_infos_excel_path())

class ReadExcel:
    '''默认参数传入sheet名，表格的路径'''
    def __init__(self,module_name,page_name,__excel_path=excel_path):
        self.__excel_path=excel_path
        '''定义工作表，打开的路径'''
        self.workbook=xlrd.open_workbook(__excel_path)
        '''定义读取的工作表中的sheet，这里产出变量名动态获取'''
        self.sheet=self.workbook.sheet_by_name(module_name)   #根据模块名称获取sheet名称,page_name:所属页面
        self.page_name=page_name
        self.row_count=self.sheet.nrows

    '''创建获取表格元素信息的方法'''
    def get_element_info(self):
        element_infos={}
        for i in range(1,self.row_count):
            if self.sheet.cell_value(i,2)==self.page_name:  #如果检索的所属页面为login_page，则查找下面的login_page的元素
                element_info={}
                element_info['element_name']=self.sheet.cell_value(i,1)
                element_info['locator_type']=self.sheet.cell_value(i,3)  #下标2被所属页面占据了
                element_info['locator_value']=self.sheet.cell_value(i,4)
                '''利用三目运算于符与isinstance设置表格超时时间为浮点型，如果没有传等待时间则设置默认时间为5'''
                timeout_value=self.sheet.cell_value(i,5)
                element_info['timeout']=timeout_value if isinstance(timeout_value,float) else conf.time_out

                element_infos[self.sheet.cell_value(i,0)]=element_info
        return element_infos

'''创建read_excel对象，其他模块调用这个类的方法'''
read_excel=ReadExcel('login','login_page')

if __name__=="__main__":
    value=ReadExcel('login','login_page').get_element_info()
    for e in value.values():
        print(e)
