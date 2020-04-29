# --*utf-8*--
import logging
from common.config_utils import conf

class LogUtils:
    def __init__(self,log_path=conf.get_log_path()):
        self.log_path=log_path
        self.logger=logging.getLogger(__name__)
        self.logger.setLevel(level=logging.INFO)
        file_log=logging.FileHandler(self.log_path)
        formatter=logging.Formatter('file:%(asctime)s,%(name)s,%(levelname)s,%(message)s')
        file_log.setFormatter(formatter)
        self.logger.addHandler(file_log)

    def info(self,message):
        self.logger.info(message)

    def error(self,message):
        self.logger.error(message)

log_print=LogUtils()

if __name__=="__main__":
    log_print.info('python')
