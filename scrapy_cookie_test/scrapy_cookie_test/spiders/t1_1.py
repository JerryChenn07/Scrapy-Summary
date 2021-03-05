import scrapy


class T1_1Spider(scrapy.Spider):
    name = 't1_1'
    custom_settings = {
        'COOKIES_ENABLED': True,
    }

    def start_requests(self):
        for i in range(3):
            headers = {
                "user-agent": "from t cookie, range %s" % i,
                # "cookie": 'set_cookie_success1=mgjwFVx/kPKOJ66GAzv3Ag==; set_cookie_success2=110;'
            }
            cookies = {'set_cookie_success1': 'mgjwFVx/kPKOJ66GAzv3Ag==', 'set_cookie_success2': '11%s' % i}
            yield scrapy.Request(url='http://httpbin.org/get?a=%s' % i,
                                 callback=self.parse_cookie,
                                 headers=headers,
                                 cookies=cookies,
                                 meta={'cookiejar': i}  # 保持从始至终的cookie一致性
                                 )

    def parse_cookie(self, response):
        self.logger.info(response.text)
        yield scrapy.Request(url=response.url + '&b=1',
                             callback=self.parse_cookie2,
                             meta={'cookiejar': response.meta['cookiejar']}
                             )

    def parse_cookie2(self, response):
        self.logger.info(response.text)
