import json

import scrapy


class T1Spider(scrapy.Spider):
    name = 't1'
    base_url = 'http://httpbin.org/post'

    def start_requests(self):
        data = {'a': 'aa', 'b': 'bb'}
        yield scrapy.FormRequest(url=self.base_url, callback=self.parse,
                                 headers={'Content-Type': 'application/json'},
                                 method='POST', body=json.dumps(data), dont_filter=True)

        yield scrapy.FormRequest(url=self.base_url, callback=self.parse,
                                 method='POST', formdata=data, dont_filter=True)

        yield scrapy.FormRequest(url=self.base_url, callback=self.parse,
                                 headers={'Content-Type': 'application/json'},
                                 method='POST', formdata=data, dont_filter=True)
        # for i in range(100):
        #     url = self.base_url + str(i)
        #     yield scrapy.Request(url, callback=self.parse)

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

{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "a": "aa", 
    "b": "bb"
  }, 
  "headers": {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
    "Accept-Encoding": "gzip,deflate", 
    "Accept-Language": "en", 
    "Connection": "close", 
    "Content-Length": "9", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "Scrapy/1.5.0 (+https://scrapy.org)"
  }, 
  "json": null, 
  "origin": "106.37.212.73", 
  "url": "http://httpbin.org/post"
}

{
  "args": {}, 
  "data": "a=aa&b=bb", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
    "Accept-Encoding": "gzip,deflate", 
    "Accept-Language": "en", 
    "Connection": "close", 
    "Content-Length": "9", 
    "Content-Type": "application/json", 
    "Host": "httpbin.org", 
    "User-Agent": "Scrapy/1.5.0 (+https://scrapy.org)"
  }, 
  "json": null, 
  "origin": "106.37.212.73", 
  "url": "http://httpbin.org/post"
}
"""
