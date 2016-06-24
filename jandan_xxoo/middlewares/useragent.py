import random
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from jandan_xxoo.settings import USER_AGENT_LIST

class RandomUserAgentMiddleware(UserAgentMiddleware):
    def process_request(self, request, spider):
        ua = random.choice(USER_AGENT_LIST)
        if ua:
            request.headers.setdefault("User-Agent", ua)
