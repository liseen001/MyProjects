#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import os
import unittest
from Music.common import HTMLTestReportCN
from Music.common.config_utils import conf
from Music.common.email_utils import EmailUtils

cuurent_path = os.path.abspath(os.path.dirname(__file__))
case_path = os.path.join(cuurent_path,'..',conf.case_path)
report_path = os.path.join(cuurent_path,'..',conf.report_path)

class RunAllCases:
    def __init__(self):
        self.test_case_path = case_path
        self.report_path =report_path
        self.title = 'Musci自动化测试报告'
        self.description = '基于Musci的测试报告'

    def run(self):
        discover = unittest.defaultTestLoader.discover(start_dir=self.test_case_path,
                                                       pattern='*_test.py',
                                                       top_level_dir=self.test_case_path)
        all_suite = unittest.TestSuite()
        all_suite.addTest(discover)

        report_dir = HTMLTestReportCN.ReportDirectory(self.report_path)
        report_dir.create_dir(self.title)
        dir_path = HTMLTestReportCN.GlobalMsg.get_value('dir_path')
        report_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')
        fp = open(report_path, 'wb')
        runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                                 title=self.title,
                                                 description=self.description,
                                                 tester='liseen')
        runner.run(all_suite)
        fp.close()
        return dir_path

if __name__ == "__main__":
    dir_path = RunAllCases().run()
    EmailUtils('python自动化测试报告',dir_path).zip_send_mail()