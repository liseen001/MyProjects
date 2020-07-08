#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import unittest
from API_TEST_LINE_Frame.utils import HTMLTestReportCN
from API_TEST_LINE_Frame.utils.config_utils import conf

def get_testsuite():  #加载所有测试用例
    discover = unittest.defaultTestLoader.discover(start_dir='./testcases',
                                                   pattern='*_testcase.py',
                                                   top_level_dir='./testcases')
    all_suite = unittest.TestSuite()
    all_suite.addTest(discover)
    return all_suite

report_dir = HTMLTestReportCN.ReportDirectory(conf.report_parh+'./')  #配置测试报告路径
report_dir.create_dir('API_TEST')  #测试报告名称
dir_path = HTMLTestReportCN.GlobalMsg.get_value('dir_path')  #为了发送邮件
report_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')
fp = open(report_path,'wb')
runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                     title='API_TEST',
                                     description='基于测试环境的部分后台接口测试用例',
                                     tester='二蛋')

runner.run(get_testsuite())
fp.close()