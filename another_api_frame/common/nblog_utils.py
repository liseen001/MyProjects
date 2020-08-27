#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:  利用nb_log 模块封装日志，get_logger_and_add_handlers() 方法中写死日志输出路径

import time
from nb_log import LogManager
from common.config_utils import conf


class NblogUtis():
    def __init__(self):
        self.logger_name = conf.log_name
        self.logger_filename = '{}_{}.log'.format( conf.log_name,time.strftime(conf.logger_filename) )



    def logger(self):
        logger = LogManager(self.logger_name).get_logger_and_add_handlers(log_filename=self.logger_filename)
        return logger


logger = NblogUtis().logger()
if __name__ == '__main__':
        logger.info('接口自动扣测试框架，UI自动化测试框架，appnium自动化测试框架')
        logger.error('接口自动扣测试框架，UI自动化测试框架，appnium自动化测试框架')
        logger.debug('接口自动扣测试框架，UI自动化测试框架，appnium自动化测试框架')
        logger.warning('接口自动扣测试框架，UI自动化测试框架，appnium自动化测试框架')
        logger.critical('接口自动扣测试框架，UI自动化测试框架，appnium自动化测试框架')







