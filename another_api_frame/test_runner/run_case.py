#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:  加载并允许所有测试用例
import os,sys
import time
import unittest
from common.config_utils import conf
from common import HTMLTestReportCN
from common.email_utils import EmailUtils
from common.nblog_utils import logger
from common.testdata_utils import TestdataUtils
from samples.xlutils_faker_demo_new import writefakertestdatas

current_path = os.path.dirname(__file__)
test_case_path = os.path.join( current_path,'..',conf.case_path )  #用例存放路径
test_report_path = os.path.join( current_path,'..',conf.report_path )
# print( test_case_path,test_report_path )

class Runcase():
    def __init__(self):
        self.test_case_path = test_case_path
        self.report_path = test_report_path
        self.title = conf.report_title
        self.description = conf.report_description
        self.tester = conf.report_tester

    def load_test_suite(self):
        '''加载所有测试套件
        start_dir=self.test_case_path, 起始目录路径一般和top_level_dir一样
        pattern='api_test.py',#只有一个excel，可以写死
        '''
        try:
            discover = unittest.defaultTestLoader.discover(start_dir=self.test_case_path,
                                                           pattern='api_test.py',
                                                           top_level_dir=self.test_case_path)
            all_suite = unittest.TestSuite()  # 创建测试套件对象
            all_suite.addTest(discover)  # 加载discover中的东西
            logger.info('\n\n====================================================加载所有测试用例完毕====================================================\n\n')
            logger.info('\n\n====================================================开始执行所有测试用例====================================================\n\n')
        except Exception as e:
            logger.error('\n\n===================================================加载所有测试用例失败，失败的原因是：{}====================================================\n\n'.format(e.__str__()))
        return all_suite  # 搜索用例加载测试用例,可以优化写成方法

    def run(self):
        '''运行所有测试用例'''
        report_dir = HTMLTestReportCN.ReportDirectory(self.report_path)  # 创建测试报告的目录对象,传入测试报告路径
        report_dir.create_dir(self.title)  # 创建测试报告存放文件夹 create_dir() 起一个标题
        report_file_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')  # 创建路径,每次都会创建最新的文件
        logger.info('\n\n====================================================创建测试报告文件路径成功====================================================\n\n')
        fp = open(report_file_path, 'wb')  # 创建文件
        runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                                 title=self.title,
                                                 description=self.description,
                                                 tester=self.tester)
        runner.run(self.load_test_suite())
        time.sleep(2)
        fp.close()
        return report_file_path  # 返回最新的测试报告路径供邮件调用

if __name__ == '__main__':

    writefakertestdatas.write_data()
    try:
        logger.info('\n\n====================================================开始清除上次测试结果保留的值====================================================\n\n')
        TestdataUtils().clear_result_from_excel()
        logger.info('\n\n====================================================开始清除上次测试结果保留的值成功====================================================\n\n')
    except Exception as e:
        logger.error('\n\n===================================================清除上次测试结果保留的值失败，失败的原因是：{}==========================================\n\n'.format(e.__str__()))

    try:
        report_path = Runcase().run()
        logger.info('\n\n===================================================已执行完所有测试用例，测试活动结束==========================================\n\n')
    except Exception as e:
        logger.info('\n\n===================================================执行测试用例的过程中出现异常，异常为：{}==========================================\n\n'.format(e.__str__()))

    try:
        logger.info('\n\n===================================================测试活动已结束，是否发送报告===================================================\n\n')
        info=input('请选择是否给各位大佬发送测试报告结果，输入 "是" 则发送，输入其他信息则不发送：')
        if info =="是":
            EmailUtils(open(report_path, 'rb').read(), report_path).send_email()
            # while time.sleep(1):
            #     break
        #     # logger.info('哎呀，忘记输入是否发送报告的指令了0.0')
        # elif time.sleep(3):
        #     sys.exit()
        else:
            logger.info('各位大佬不需要测试报告结果，没有发送测试报告')
    except Exception as e:
        logger.error('出现未知异常，异常报错为：'.format(e.__str__()))




