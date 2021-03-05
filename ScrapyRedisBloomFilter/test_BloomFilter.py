# -*- coding: utf-8 -*-
from redis import StrictRedis
from scrapy_redis_bloomfilter.bloomfilter import BloomFilter

conn = StrictRedis(host='localhost', port=6379, db=1)

bf = BloomFilter(conn, 'testbf30', 30, 10)
result = bf.exists('url')
bool_result = bool(result)
print(bool_result)
for i in range(1000):
    url = f'httphttphttphttphttphttphttphttphttphttphttp://httpbin.org/get?wd={i * 66}'
    result = bf.exists(url)
    bool_result = bool(result)
    if bool_result:
        print(url)
    bf.insert(url)
# for i in range(100000):
#     result = bf.exists('http://httpbin.org/gethttp://httpbin.org/gethttp://httpbin.org/gethttp://httpbin.org/gethttp://httpbin.org/gethttp://httpbin.org/gethttp://httpbin.org/gethttp://httpbin.org/gethttp://httpbin.org/gethttp://httpbin.org/gethttp://httpbin.org/get?wd=%s' % i)
#     bool_result = bool(result)
#     # print(bool_result)
#     if not bool_result:
#         print(bool_result,'http://httpbin.org/get?wd=%s' % i)
