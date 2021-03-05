import random


class RandomUserAgentMiddleware():
    def __init__(self, user_agent):
        self.user_agent = user_agent

    @classmethod
    def from_crawler(cls, crawler):
        return cls(user_agent=crawler.settings.get('PC_USER_AGENT'))

    def process_request(self, request, spider):
        ua = random.choice(self.user_agent)
        request.headers["User-Agent"] = ua
