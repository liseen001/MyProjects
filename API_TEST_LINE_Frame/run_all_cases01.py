#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:  运行所有测试用例 方法一  测试报告比较简陋
import os
import time
import unittest
import HTMLTestRunner
from API_TEST_LINE_Frame.utils.config_utils import conf

def get_testsuite():
    discover =unittest.defaultTestLoader.discover(start_dir='./testcases',
                                                  pattern='*_testcase.py',
                                                  top_level_dir='./testcases')
    all_suite = unittest.TestSuite()
    all_suite.addTest(discover)
    return all_suite

now_time = time.strftime('%Y_%m_%d_%H_%M_%S')
html_report = os.path.join(conf.report_parh,'ApiReport_%s.html'% now_time)
file =open(html_report,'wb')
html_runner =HTMLTestRunner.HTMLTestRunner(stream=file,
                                           title='新后台接口测试',
                                           description='基于测试环境的部分后台接口测试用例')
html_runner.run(get_testsuite())