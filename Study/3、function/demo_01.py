# -*- coding utf-8 -*-
# for i in range(6):
#     print('selcc')
import os
from loguru import logger




current_path=os.path.dirname(__file__)
log_path=os.path.join(current_path,'../logs/test.log')

logger.add(log_path,format='{tuime}{level}{message}',filter="my_module",level='INFO')
logger.debug('this is a debug message')

