# --*utf-8*--
import os
import logging
import loguru
from common.config_utils import conf

curren_path=os.path.dirname(__file__)
log_path=os.path.join(curren_path,conf.get_log_path())

logger=logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)

console=logging.StreamHandler()
formatter=logging.Formatter('file:%(asctime)s,%(name)s,%(levelname)s,%(message)s')
console.setFormatter(formatter)
console.setLevel(level=logging.ERROR)

file_log=logging.FileHandler(log_path)
formatter=logging.Formatter('file:%(asctime)s,%(name)s,%(levelname)s,%(message)s')
file_log.setFormatter(formatter)

# logger.addHandler(console)
logger.addHandler(file_log)

# logger.info('liseen')
loguru.logger.info('helloworld')
loguru.logger.error('helloworld,liseen')