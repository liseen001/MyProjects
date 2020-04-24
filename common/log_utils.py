# -*- coding utf-8 -*-
import logging,time
import os
current_path = os.path.dirname(__file__)
log_path = os.path.join(current_path,'../logs/test')
'''如果不存在这个test文件就自动新建一个'''
if not os.path.exists(log_path):os.mkdir(log_path)

class Log(object):

    def __init__(self):
        #文件的命名
        self.name = os.path.join(log_path,'%s.log'%time.strftime('%Y_%m_%d'))
        self.logger=logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        #日志输出格式
        self.formater = logging.Formatter('[%(asctime)s]-%(levelname)s:%(message)s')

    def _console(self,level,message):
        #创建一个FileHandler，用于写到本地
        fh =None
