BOT_NAME = 'scrapy_middlewares_init_test'

SPIDER_MODULES = ['scrapy_middlewares_init_test.spiders']
NEWSPIDER_MODULE = 'scrapy_middlewares_init_test.spiders'

DOWNLOADER_MIDDLEWARES = {
    'scrapy_middlewares_init_test.middlewares.RandomUserAgentMiddleware': 100,
}

ROBOTSTXT_OBEY = False
