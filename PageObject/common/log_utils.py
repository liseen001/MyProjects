# -*- coding utf-8 -*-
import os
from PageObject.common.config_utils import conf
import logging

current_path=os.path.dirname(__file__)
log_path=os.path.join(current_path,conf.log_file_path)

class LogUtils(object):
    '''传入log_path参数'''
    def __init__(self,log_path=log_path):
        self.log_path=log_path
        '''定义logger对象'''
        self.logger=logging.getLogger('logger')
        '''设置对象打印的日志级别'''
        self.logger.setLevel(level=logging.INFO)
        '''设置打印日志的输入文件对象,即日志收集器,传入日志文件路径和编码格式'''
        file_log=logging.FileHandler(self.log_path,encoding='utf-8')
        '''设置日志输入的格式'''
        formatter=logging.Formatter('file:%(asctime)s,%(name)s,%(levelname)s,%(message)s')
        '''把上面设置的输入格式加载输出到日志文件中'''
        file_log.setFormatter(formatter)
        '''把需要打印的日志输入到文件对象中'''
        self.logger.addHandler(file_log)

    '''打印info级别日志的方传入参数message法'''
    def info(self,message):
        self.logger.info(message)

    def error(self,message):
        self.logger.error(message)

logutils=LogUtils()

if __name__=="__main__":
    logutils.info('liseen')