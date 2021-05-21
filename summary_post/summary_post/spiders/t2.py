import scrapy
from scrapy.http import JsonRequest


class T2Spider(scrapy.Spider):
    name = 't2'
    base_url = 'http://httpbin.org/post'

    def start_requests(self):
        data = {'a': 'aa', 'b': 'bb'}
        yield JsonRequest(url=self.base_url, callback=self.parse,
                          data=data, dont_filter=True)

    def parse(self, response):
        self.logger.debug('Response of ' + response.url)
        print(response.text)


"""{
  "args": {}, 
  "data": "{\"a\": \"aa\", \"b\": \"bb\"}", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
    "Accept-Encoding": "gzip,deflate", 
    "Accept-Language": "en", 
    "Connection": "close", 
    "Content-Length": "22", 
    "Content-Type": "application/json", 
    "Host": "httpbin.org", 
    "User-Agent": "Scrapy/1.5.0 (+https://scrapy.org)"
  }, 
  "json": {
    "a": "aa", 
    "b": "bb"
  }, 
  "origin": "106.37.212.73", 
  "url": "http://httpbin.org/post"
}
"""
