#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc: 封装日志模块
import os
import logging
import time
from  API_TEST_LINE_Frame.utils.config_utils import conf


current_path = os.path.dirname(__file__)
log_path = os.path.join(current_path,'..',conf.log_path)

class LogUtil(object):
    def __init__(self,logger=None):
        self.log_name = os.path.join(log_path,'接口测试日志_%s.log'%time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger(logger)  #设置logger对象
        self.logger.setLevel(conf.log_level)  #设置日志级别，读取配置文件


        self.fh = logging.FileHandler(self.log_name,encoding='utf-8')
        self.fh.setLevel(conf.log_level)
        self.ch = logging.StreamHandler()
        self.ch.setLevel(conf.log_level)

        formatter = logging.Formatter(
            '[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s'
        )
        self.fh.setFormatter(formatter)
        self.ch.setFormatter(formatter)
        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.ch)
        self.fh.close()
        self.ch.close()

    def get_log(self):
        return self.logger

logutils = LogUtil().get_log()

if __name__=="__main__":
    logging.info('liseen')