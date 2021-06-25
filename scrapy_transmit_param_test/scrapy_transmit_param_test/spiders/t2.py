import scrapy


class T2Spider(scrapy.Spider):
    name = 't2'

    def __init__(self, settings, *args, **kwargs):
        super().__init__()
        self.begin_num = settings.get('FOR_BEGIN_NUM')

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = cls(crawler.settings, *args, **kwargs)
        spider._set_crawler(crawler)
        return spider

    def start_requests(self):
        self.logger.info(f"get begin_num={self.begin_num}, type={type(self.begin_num)}")
        # get begin_num=666, type=<class 'int'>
        urls = ['https://httpbin.org/get']
        for i in urls:
            yield scrapy.Request(url=i, dont_filter=True)

    def parse(self, response):
        self.logger.info(f'{response.url} --->成功了')
