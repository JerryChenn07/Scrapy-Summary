import scrapy


class T1Spider(scrapy.Spider):
    name = 't1'
    custom_settings = {
        'COOKIES_ENABLED': False,
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy_ip_test.middlewares.TestProxyMiddleware': 100,
        }
    }

    def start_requests(self):
        yield scrapy.Request(url='https://httpbin.org/get?a=test', callback=self.parse_1, dont_filter=True)

    def parse_1(self, response):
        # self.logger.info('我在这')
        self.logger.info(response.text)
