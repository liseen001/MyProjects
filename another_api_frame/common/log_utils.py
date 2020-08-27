#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc: 封装日志模块
import os
import time
import logging
from common.config_utils import conf

cuurent_pat = os.path.dirname(__file__)
log_out_path = os.path.join( cuurent_pat,'..',conf.log_path )

class LogUtils():
    def __init__(self,log_path = log_out_path):
        self.log_name = os.path.join( log_path,'{}{}.log'.format('后台接口测试日志_',time.strftime('%m-%d')  ) )
        self.logger = logging.getLogger( '后台接口测试日志_' )
        self.logger.setLevel( conf.log_level )


        console_handler = logging.StreamHandler()
        file_handler = logging.FileHandler( self.log_name,'a',encoding='utf-8' )
        formatter = logging.Formatter(
            '[%(asctime)s] %(filename)s-->%(funcName)s line:%(lineno)d [%(levelname)s]:   %(message)s'
        )
        console_handler.setFormatter( formatter )
        file_handler.setFormatter( formatter )

        self.logger.addHandler( console_handler )
        self.logger.addHandler( file_handler )

        console_handler.close()
        file_handler.close()


    def get_log(self):
        return self.logger

logger = LogUtils().get_log()

if __name__ == '__main__':
    logger.info( '接口自动化日志@23423$$$$$$$$$$$$$$$$$$^*(!@^*(!@^$_(!@_$!@_*($' )