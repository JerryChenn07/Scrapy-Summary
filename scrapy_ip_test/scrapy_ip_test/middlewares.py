

class TestProxyMiddleware(object):
    def process_response(self, request, response, spider):
        spider.logger.info(response.text)
        # h = request.headers['Proxy-Authorization']
        # p = request.meta['proxy']
        # del h
        # del p
        # time.sleep(10)
        return response
