import logging
import random


class RandomUserAgentMiddleware(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.sid_list = []
        if not self.sid_list:
            for i in range(5):
                self.sid_list.append(self.get_sid())
            self.logger.info(f"phone sid init done. {self.sid_list}")

    def process_request(self, request, spider):
        # add cookies
        # self.sid_list.append(self.get_sid())
        # spider.logger.info(self.sid_list)
        request.cookies = {'session_id': random.choice(self.sid_list)}

    def get_sid(self):
        s = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        return random.choice(s)
