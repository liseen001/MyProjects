#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: run_all_cases.py
# @time: 2020/5/16 22:32
# @desc:运行所有测试用例的文件
import os
import unittest
from PageObject.common import HTMLTestReportCN
from PageObject.common.config_utils import conf
from PageObject.common import zip_utils
from PageObject.common.email_utils import EmailUtils

current_path=os.path.abspath(os.path.dirname(__file__))
case_path=os.path.join( current_path,'..',conf.case_path )
report_path=os.path.join( current_path,'..',conf.report_path )

class RunAllCases:
    def __init__(self):
        self.test_case_path= case_path  #测试用例路径
        self.report_path= report_path   #测试报告路径
        self.title='禅道自动化测试报告'    #测试用例标题
        self.description='newdream'    #描述

    def run(self):
        discover= unittest.defaultTestLoader.discover(start_dir= self.test_case_path,
                                                      pattern='*_test.py',
                                                      top_level_dir=self.test_case_path)
        all_suite =unittest.TestSuite()
        all_suite.addTest(discover)

        report_dir= HTMLTestReportCN.ReportDirectory(self.report_path)  #配置测试报告路径，把测试报告全部打印在reports里面
        report_dir.create_dir(self.title)    #report下面创建一个文件夹
        dir_path =HTMLTestReportCN.GlobalMsg.get_value('dir_path')
        report_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')
        fp = open(report_path,'wb')
        runner= HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                                title=self.title,
                                                description=self.description,
                                                tester='MrLiu')

        runner.run(all_suite)
        fp.close()
        return dir_path

if __name__=="__main__":
    dir_path = RunAllCases().run()
    EmailUtils('python自动化测试报告',dir_path).zip_send_mail()