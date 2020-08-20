#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: loh_demo_nb.py
# @time: 2020/8/20 22:10
# @desc:
import os
from  nb_log import LogManager
current_path = os.path.join( os.path.dirname(__file__)+'test/log' )
print( current_path )
logger = LogManager('newdream').get_logger_and_add_handlers(log_level_int=1,log_filename='APITEST.log')

logger.info('你好')
logger.warning('警告')
logger.error('错误日志')