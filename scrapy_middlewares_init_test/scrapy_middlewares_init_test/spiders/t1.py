import scrapy


class T1Spider(scrapy.Spider):
    name = 't1'

    def start_requests(self):
        for i in range(1):
            yield scrapy.Request(url='https://httpbin.org/get?laowang=%s' % i, callback=self.parse, dont_filter=True)

    def parse(self, response):
        self.logger.info(response.text)
