# -*- coding: utf-8 -*-
import logging.config
from os import path

# 日志配置  logger.cfg路径
log_file_path = path.join(path.dirname(path.abspath(__file__)), '../logger.cfg')
logging.config.fileConfig(log_file_path, disable_existing_loggers=False)
# 注意这里修改 logShow
logger = logging.getLogger('scrapy_logging')
# scrapyLogger = logging.getLogger('scrapy_logging')
