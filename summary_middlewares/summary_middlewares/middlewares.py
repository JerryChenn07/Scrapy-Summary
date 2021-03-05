import random

from scrapy.downloadermiddlewares.retry import RetryMiddleware
from scrapy.exceptions import IgnoreRequest


class RandomUserAgentMiddleware():
    def __init__(self, user_agent):
        self.user_agent = user_agent

    @classmethod
    def from_crawler(cls, crawler):
        return cls(user_agent=crawler.settings.get('PC_USER_AGENT'))

    def process_request(self, request, spider):
        ua = random.choice(self.user_agent)
        request.headers["User-Agent"] = ua


class IgnoreRequestMiddleware(object):
    def process_request(self, request, spider):
        # if '/ch90' in request.url or '/ch60' in request.url or '/ch33954' in request.url:
        raise IgnoreRequest


class RandomRetryMiddleware(RetryMiddleware):
    def process_response(self, request, response, spider):
        if response.url == 'http://httpbin.org/get':
            return self._retry(request, f'It is time to retry', spider) or response
        return response


class RandomProxyMiddleware(object):
    def __init__(self, proxies):
        self.proxies = proxies

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        # PROXIES = "http://proxy.domain.cn:6666"
        return cls(proxies=settings.get('PROXIES'))

    def process_request(self, request, spider):
        request.meta['proxy'] = self.proxies
