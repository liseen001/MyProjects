# -*- coding utf-8 -*-
import os
from Music.common.confing_utils import conf
import logging

current_path=os.path.dirname(__file__)
logs_path=os.path.join(current_path,conf.get_logs_path())

class LogUtils(object):
    '''实例化日志路径'''
    def __init__(self,log_path=logs_path):
        self.log_path=log_path
        '''创建logger对象,可以引用logging中的方法'''
        self.logger=logging.getLogger('logger')
        '''设置对象中的日志级别'''
        self.logger.setLevel(level=logging.INFO)
        '''创建日志输入位置,输入格式为utf-8'''
        file_log=logging.FileHandler(self.log_path,encoding='utf-8')
        '''设置输出日志格式'''
        formatter=logging.Formatter('file:%(asctime)s,%(name)s,%(levelname)s,%(message)s')
        '''把上面设置的日志格式传入日志对象位置'''
        file_log.setFormatter(formatter)
        self.logger.addHandler(file_log)


    '''创建输入日志方法'''
    def info(self,message):
        self.logger.info(message)

    '''创建输入日志方法error'''
    def error(self,message):
        self.logger.error(self,message)

logutils=LogUtils()

if __name__=="__main__":
    logutils.info('test')