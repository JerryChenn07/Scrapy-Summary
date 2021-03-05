BOT_NAME = 'scrapy_selenium_test'

SPIDER_MODULES = ['scrapy_selenium_test.spiders']
NEWSPIDER_MODULE = 'scrapy_selenium_test.spiders'

ROBOTSTXT_OBEY = False

DOWNLOADER_MIDDLEWARES = {
    'scrapy_selenium_test.middlewares.SeleniumDownloaderMiddleware': 543,
}
