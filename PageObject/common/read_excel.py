# -*- coding utf-8 -*-
import os
import xlrd
from PageObject.common.config_utils import conf
from PageObject.common.excel_utils import ExcelUtils

current_path=os.path.dirname(__file__)
'''调用配置类中元素信息表格路径的属性当方法'''
element_infos_path=os.path.join(current_path,conf.element_infos_path)

class ReadExcel():
    '''module_name:sheet名，page_name：元素信息表中的所属页面字段'''
    def __init__(self,module_name,page_name,element_infos_path=element_infos_path):
        self.element_infos_path=element_infos_path
        '''定义工作表及路径'''
        self.workbook=xlrd.open_workbook(element_infos_path)
        '''定义读取工作表中的sheet，动态获取，根据模块名module_name获取'''
        self.sheet=self.workbook.sheet_by_name(module_name)
        self.page_name=page_name
        '''定义行数对象'''
        self.row_count=self.sheet.nrows



    '''创建获取表格元素信息的方法'''
    def get_element_info(self):
        element_infos={}
        for i in range(1,self.row_count):
            '''如果检索表格中下表三为login_page,则查找下面的login_page元素'''
            if self.sheet.cell_value(i,2)==self.page_name:
                element_info={}
                element_info['element_name']=self.sheet.cell_value(i,1)
                '''小标2被表格中的page_name占据了'''
                element_info['locator_type']=self.sheet.cell_value(i,3)
                element_info['locator_value']=self.sheet.cell_value(i,4)
                '''利用三目运算符与isinstance设置表格超时时间为浮点型，如果表格time_out没有传等待时间则默认等待时间为5'''
                timeout_value=self.sheet.cell_value(i,5)
                element_info['time_out']=timeout_value if isinstance(timeout_value,float) else conf.time_out
                '''获取表格中下表0的值放入element_infos中'''
                element_infos[self.sheet.cell_value(i,0)]=element_info
        return element_infos



if __name__=="__main__":
    value=ReadExcel('product','add_product_page').get_element_info()
    for e in value.values():
        print(e)