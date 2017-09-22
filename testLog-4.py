# -*- encoding:utf-8 -*-
import logging
import logging.config

logging.config.fileConfig("./logging.conf")

# create logger
# logger_name = "example"
logger = logging.getLogger('example01')

logger.debug('debug message AB')
logger.info('AB info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
