import scrapy


class T1Spider(scrapy.Spider):
    name = 't1'
    custom_settings = {
        'COOKIES_ENABLED': True,
    }

    def start_requests(self):
        headers = {
            "user-agent": "from t cookie",
            # "cookie": 'set_cookie_success1=mgjwFVx/kPKOJ66GAzv3Ag==; set_cookie_success2=110;'
        }
        cookies = {'set_cookie_success1': 'mgjwFVx/kPKOJ66GAzv3Ag==', 'set_cookie_success2': '110'}
        yield scrapy.Request(url='http://httpbin.org/get?a=1',
                             callback=self.parse_cookie,
                             headers=headers,
                             cookies=cookies
                             )

    def parse_cookie(self, response):
        self.logger.info(response.text)
        '''
        "headers": {
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
                    "Accept-Encoding": "gzip, deflate", 
                    "Accept-Language": "en", 
                    "Cookie": "set_cookie_success1=mgjwFVx/kPKOJ66GAzv3Ag==; set_cookie_success2=110", 
                    "Host": "httpbin.org", 
                    "User-Agent": "from t cookie", 
                    "X-Amzn-Trace-Id": "Root=1-5fd96e37-28dd1dd32cc6f4f176e03cf1"
                  }
        '''
        yield scrapy.Request(url='http://httpbin.org/get?a=2',
                             callback=self.parse_cookie2,
                             )

    def parse_cookie2(self, response):
        self.logger.info(response.text)
