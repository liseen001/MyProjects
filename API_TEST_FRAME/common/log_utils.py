#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: log_utils.py
# @time: 2020/7/7 23:45
# @desc: 封装日志模块
import  os
import  logging
import time
from API_TEST_FRAME.common.config_utils import conf
current_path = os.path.dirname(__file__)
log_output_path = os.path.join(current_path,'..',conf.log_path)

class LogUtils():
    def __init__(self,log_path=log_output_path):
        self.log_name = os.path.join(log_path,'ApiTest_%s.log'%time.strftime('%Y_%m_%d')) #日志文件,每天生成一个
        self.logger = logging.getLogger('ApiTestLog_')
        self.logger.setLevel(conf.log_level)  #设置日志对象名称

        console_handler = logging.StreamHandler()   #控制台日志对象
        file_handler = logging.FileHandler(self.log_name,'a',encoding='utf-8')  #文件输出日志对象。a以追加的方式
        formatter = logging.Formatter(
            '[%(asctime)s] %(filename)s-->%(funcName)s line:%(lineno)d [%(levelname)s]:   %(message)s'
        )  #设置日志格式
        console_handler.setFormatter(formatter)  #控制台输出日志引用上面设置的日志格式
        file_handler.setFormatter(formatter)   #文件输出日志引用日志格式

        self.logger.addHandler( console_handler )  #追加日志对象可以打印日志
        self.logger.addHandler( file_handler )

        console_handler.close()  #记得关掉对象，避免重复打印
        file_handler.close()

    def get_log(self):
        return  self.logger

logger = LogUtils().get_log()  # 避免重复打印日志

if __name__ =="__main__":
    logger.info('hello')