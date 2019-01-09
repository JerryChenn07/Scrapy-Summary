# -*- coding: utf-8 -*-
import scrapy
from DuplicatesFilterPipelineExample.items import DuplicatesFilterPipelineExampleItem


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['httpbin.org']
    base_url = 'http://httpbin.org/post'

    def start_requests(self):
        for i in range(2):
            data = {'t1': 'aa', 't2': 'bb', 'page': str(i)}
            yield scrapy.FormRequest(url=self.base_url, callback=self.parse, method='POST',
                                     formdata=data, meta={'data': data})

    def parse(self, response):
        item = DuplicatesFilterPipelineExampleItem()
        data = response.meta['data']
        item['t1'] = data['t1']
        item['t2'] = data['t2']
        item['page'] = data['page']
        yield item
