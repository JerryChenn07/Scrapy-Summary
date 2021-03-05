import scrapy


class T1Spider(scrapy.Spider):
    name = 't1'
    custom_settings = {
        'USER_AGENT': 'cjrcjrcjr (+http://www.yourdomain.com)',
        'REDIRECT_ENABLED': False,
        # 429是代理并发数过多失效的状态码 301，302在禁止定向后，重新抓取
        # 'RETRY_HTTP_CODES': [500, 502, 503, 504, 400, 403, 404, 405, 408, 429, 301]
    }

    def start_requests(self):
        yield scrapy.Request(url='https://httpbin.org/absolute-redirect/1', callback=self.parse_1,
                             dont_filter=True,
                             meta={
                                 'dont_redirect': False,
                                 # 'handle_httpstatus_list': [302]
                             })

    def parse_1(self, response):
        print(response.text)
