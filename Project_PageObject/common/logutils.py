# -*- coding utf-8 -*-
import os
import logging,loguru
from Project_PageObject.common.config_utils import conf

current_path=os.path.dirname(__file__)
log_path=os.path.join(current_path,conf.get_logs_path())
class LogUtils(object):
    def __init__(self,log_path=log_path):
        self.log_path=log_path
        self.logger=logging.getLogger('logger')
        self.logger.setLevel(level=logging.INFO)
        file_log=logging.FileHandler(self.log_path,encoding='utf-8')
        formatter=logging.Formatter('file:%(asctime)s,%(name)s,%(levelname)s,%(message)s')
        file_log.setFormatter(formatter)
        self.logger.addHandler(file_log)

    def info(self,message):
        self.logger.info(message)

    def error(self,message):
        self.logger.error(message)

logutils=LogUtils()
if __name__=="__main__":
    logutils.info('liseen')
