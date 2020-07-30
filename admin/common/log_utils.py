#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import os
import logging
import time
from admin.common.config_utils import conf

current_path=os.path.dirname(__file__)
log_path=os.path.join(current_path,'..',conf.log_path)
# print(log_path)

class LogUtils():
    def __init__(self,log_path=log_path):
        self.log_name=os.path.join(log_path,'新后台日志_%s.log'%time.strftime('%Y-%m-%d'))  #创建日志文件名称，每天生成一个
        self.logger=logging.getLogger('新后台日志')
        self.logger.setLevel(conf.log_level)  #设置日志对象名称

        console_handler = logging.StreamHandler() #控制台日志对象
        file_handler = logging.FileHandler(self.log_name,'a',encoding='utf-8') #文件输入日志对象，以追加的方式
        formatter=logging.Formatter(
            '[%(asctime)s] %(filename)s-->%(funcName)s line:%(lineno)d [%(levelname)s]:   %(message)s'
        )  #设置 日志格式
        console_handler.setFormatter(formatter)     #控制台输出日志引用上面设置的日志格式
        file_handler.setFormatter(formatter)        #文件输出日志引用日志格式

        self.logger.addHandler(console_handler)  #追加日志对象可以打印日志
        self.logger.addHandler(file_handler)

        console_handler.close()  #关闭日志对象避免重复打印
        file_handler.close()


    def get_log(self):
        return self.logger

logger=LogUtils().get_log()

if __name__ == "__main__":
    logger.info('test')