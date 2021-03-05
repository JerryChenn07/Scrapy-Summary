import scrapy


class T1Spider(scrapy.Spider):
    name = 't1'

    def start_requests(self):
        headers = {
            'User-Agent': 'hello younger brother',
        }
        # for i in start_urls:
        #     yield scrapy.Request(url=i, dont_filter=True,headers=headers)
        print(type(eval('self.parse_haha')))
        print(type(self.parse_haha))
        for i in range(1):

            yield scrapy.Request(url='http://httpbin.org/get?a=1', callback=eval('self.parse_haha'),
                                 headers=headers, dont_filter=True)

    def parse_haha(self, response):
        if 'User-Agent' not in response.text:
            self.logger.info(response.text)
        self.logger.info(f'{response.url}--->成功了')
