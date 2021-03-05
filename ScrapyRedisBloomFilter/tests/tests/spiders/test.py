# -*- coding: utf-8 -*-
from scrapy import Request, Spider


class TestSpider(Spider):
    name = 'test'
    set_url = []
    base_url = 'http://httpbin.org/get?wd='
    
    def start_requests(self):
        for i in range(10):
            url = self.base_url + str(i)
            self.set_url.append(url)
            yield Request(url, callback=self.parse, meta={'url':url})
        # yield Request('http://httpbin.org/get?wd=1', callback=self.parse, meta={'url':url})  
        for i in range(1000):
            url = self.base_url + str(i)
            self.set_url.append(url)
            yield Request(url, callback=self.parse, meta={'url':url})
    
    def parse(self, response):
        if self.set_url.count(response.meta['url'])!=1:
            self.logger.info('Response of ' + response.url)
