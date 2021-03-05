import scrapy


class T1Spider(scrapy.Spider):
    name = 't1'

    def __init__(self, begin_num=None):
        super().__init__()
        self.begin_num = begin_num

    def start_requests(self):
        self.logger.info(f"get begin_num={self.begin_num}, type={type(self.begin_num)}")
        # get begin_num=10, type=<class 'str'>
        urls = ['https://httpbin.org/get']
        for i in urls:
            yield scrapy.Request(url=i, dont_filter=True)

    def parse(self, response):
        self.logger.info(f'{response.url}--->成功了')
