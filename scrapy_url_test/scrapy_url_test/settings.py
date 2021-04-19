BOT_NAME = 'scrapy_url_test'

SPIDER_MODULES = ['scrapy_url_test.spiders']
NEWSPIDER_MODULE = 'scrapy_url_test.spiders'

# LOG_FILE = 'hotline_stats.log'
# LOG_LEVEL = "INFO"

REDIRECT_ENABLED = True
# 429是代理并发数过多失效的状态码 301，302在禁止定向后，重新抓取
RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 403, 404, 405, 408, 429]
# DOWNLOAD_DELAY = 0.1
CONCURRENT_REQUESTS = 40
CONCURRENT_REQUESTS_PER_DOMAIN = 40
DOWNLOAD_TIMEOUT = 60
RETRY_TIMES = 5

# REFERER_ENABLED = False  # 关闭spidermiddlewares.referer.RefererMiddleware
ROBOTSTXT_OBEY = False
# COOKIES_ENABLED = False
COOKIES_ENABLED = True

DOWNLOADER_MIDDLEWARES = {
    '{}.middlewares.ParseMiddleware'.format(BOT_NAME): 1,
    # '{}.middlewares.RandomUserAgentMiddleware'.format(BOT_NAME): 100,
}

PC_USER_AGENT = [
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/8.6.1.15524',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2030.400 QQBrowser/9.5.10108.400']
