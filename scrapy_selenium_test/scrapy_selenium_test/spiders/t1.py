import scrapy


class T1Spider(scrapy.Spider):
    name = 't1'

    def start_requests(self):
        base_url = ['http://www.luhua.cn', 'https://www.hyatt.com/zh-CN/home/', 'http://www.blackswancake.com',
                    'http://www.bjwatergroup.com.cn', 'http://www.hayaoliu.com/home.asp',
                    'http://www.fang.com', 'http://www.5i5j.com', 'http://www.hazq.com', 'http://www.zhenai.com/',
                    'http://www.tjbus.com']
        base_url = ['http://xbwl.com/']

        for i in base_url:
            yield scrapy.Request(url=i, callback=self.parse, dont_filter=True)

    def parse(self, response):
        self.logger.info(f"我在response{response.url}-->>{response.status}")
