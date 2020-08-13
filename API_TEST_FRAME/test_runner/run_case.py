#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: run_case.py
# @time: 2020/8/12 23:28
# @desc:  加载并运行所有测试用例
import os
import unittest
from API_TEST_FRAME.common.config_utils import conf
from API_TEST_FRAME.common import HTMLTestReportCN
from API_TEST_FRAME.common.email_utils import EmailUtils

current_path = os.path.dirname(__file__)
test_case_path = os.path.join( current_path,'..',conf.case_path )  #例存放路径
test_report_pth = os.path.join( current_path,'..',conf.report_path )  #测试报告存放路径
# print( test_case_path )
# print( test_report_pth )
class Runcase():
    def __init__(self):
        self.test_case_path= test_case_path
        self.report_path = test_report_pth
        self.title = 'P1P2接口自动化测试报告'  #测试报告标题
        self.description = '自动化接口测试框架学习用'  #描述
        self.tester = '测试开发组全体成员'   #作者

    def load_test_suite(self):
        '''
        加载所有测试套件
        start_dir=self.test_case_path, 起始目录路径一般和top_level_dir一样
        pattern='api_test.py',#只有一个excel，可以写死
        '''
        discover = unittest.defaultTestLoader.discover( start_dir=self.test_case_path,
                                                        pattern='api_test.py',
                                                        top_level_dir=self.test_case_path)
        all_suite = unittest.TestSuite() #创建测试套件对象
        all_suite.addTest( discover )    #加载discover中的东西
        return  all_suite                #搜索用例加载测试用例,可以优化写成方法

    def run(self):
        '''运行所有测试用例'''
        report_dir = HTMLTestReportCN.ReportDirectory( self.report_path )      #创建测试报告的目录对象,传入测试报告路径
        report_dir.create_dir( self.title )    #创建测试报告存放文件夹 create_dir() 起一个标题
        report_file_path = HTMLTestReportCN.GlobalMsg.get_value( 'report_path' )  #创建路径,每次都会创建最新的文件
        fp = open( report_file_path,'wb' )  #创建文件
        runner = HTMLTestReportCN.HTMLTestRunner( stream=fp,
                                                  title=self.title,
                                                  description=self.description,
                                                  tester=self.tester)
        runner.run( self.load_test_suite() )
        fp.close()
        return report_file_path  #返回最新的测试报告路径供邮件调用

if __name__ == '__main__':
    report_path = Runcase().run()  #运行测试用例
    EmailUtils('<h3 align="center">自动化测试报告</h3>',report_path).send_mail()  #发送邮件
    # EmailUtils(open(report_path, 'rb').read(), report_path).send_mail()  # 发送邮件

