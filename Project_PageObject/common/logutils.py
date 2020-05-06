# -*- coding utf-8 -*-
import os
import logging
from Project_PageObject.common.config_utils import conf

current_path=os.path.dirname(__file__)
log_path=os.path.join(current_path,conf.get_logs_path())
class LogUtils(object):
    def __init__(self,log_path=log_path):
        self.log_path=log_path
        '''定义一个logger对象'''
        self.logger=logging.getLogger('logger')
        '''设置logger打印的日志级别'''
        self.logger.setLevel(level=logging.INFO)
        '''logger对象打印日志的输入文件对象'''
        file_log=logging.FileHandler(self.log_path,encoding='utf-8')
        '''设置打印日志的格式'''
        formatter=logging.Formatter('file:%(asctime)s,%(name)s,%(levelname)s,%(message)s')
        '''设置打印日志对象文件的日志格式'''
        file_log.setFormatter(formatter)
        '''把需要打印的日志输入到文件对象中'''
        self.logger.addHandler(file_log)

    '''创建打印info级别日志的方法，其中需要传个message'''
    def info(self,message):
        self.logger.info(message)

    def error(self,message):
        self.logger.error(message)

logutils=LogUtils()
if __name__=="__main__":
    logutils.info('liseen')
