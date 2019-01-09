# -*- coding: utf-8 -*-
import scrapy
from scrapy_logging import logger_conf

logger = logger_conf.logger


class ShowLogCfgSpider(scrapy.Spider):
    name = 'show_log_cfg'
    allowed_domains = ['cjr.log.com']
    start_urls = ['http://cjr.log.com/']

    def parse(self, response):
        pass
