# -*- coding utf-8 -*-
import os
import logging
import time
from PageObject.common.config_utils import conf

current_path=os.path.dirname(__file__)
log_path=os.path.join(current_path,'..',conf.log_path)
print(log_path)

class LogUtil(object):
    def __init__(self,loggr=None):
        self.log_name=os.path.join(log_path,'UITest_%s.log'%time.strftime('%Y_%m_%d'))
        self.logger=logging.getLogger(loggr)
        self.logger.setLevel(conf.log_level)


        self.fh=logging.FileHandler(self.log_name,'a',encoding='utf-8')
        self.fh.setLevel(conf.log_level)
        self.ch=logging.StreamHandler()
        self.ch.setLevel(conf.log_level)

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