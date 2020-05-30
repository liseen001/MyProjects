#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:封装日志模块,这里获取日志配置文件设置的日志级别的时候会有坑，需要把获取的日志参数强转成整型
import os
import logging
import time
from common.config_utils import conf

current_path=os.path.dirname(__file__)
log_path=os.path.join(current_path,'..',conf.log_path)

class LogUtil(object):
    def __init__(self,logger=None):
        self.log_name=os.path.join(log_path,'自动化测日志_%s.log'%time.strftime('%Y_%m_%d'))
        self.logger=logging.getLogger(logger)  #设置logger对象
        self.logger.setLevel(conf.log_level)   #设置日志级别

        self.fh=logging.FileHandler(self.log_name,encoding='utf-8')
        self.fh.setLevel(conf.log_level)
        self.ch=logging.StreamHandler()
        self.ch.setLevel(conf.log_level)

        '''
        %(levelno)s: 打印日志级别的数值
        %(levelname)s: 打印日志级别名称
        %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
        %(filename)s: 打印当前执行程序名
        %(funcName)s: 打印日志的当前函数
        %(lineno)d: 打印日志的当前行号
        %(asctime)s: 打印日志的时间
        %(thread)d: 打印线程ID
        %(threadName)s: 打印线程名称
        %(process)d: 打印进程ID
        %(message)s: 打印日志信息
        '''

        formatter=logging.Formatter(
            '[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s')
        self.fh.setFormatter(formatter)
        self.ch.setFormatter(formatter)
        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.ch)
        self.fh.close()
        self.ch.close()

    def get_log(self):
        return self.logger

logutils=LogUtil().get_log()

if __name__=="__main__":
    logging.info('liseen')