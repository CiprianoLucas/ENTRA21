# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from random import choice
import requests
from urllib.parse import urlencode
from urllib.error import HTTPError

class ScrapeOpsFakeBrowserHeaderAgentMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        return cls(crawler.settings)
    
    def __init__(self, settings):
        self.scrapeops_api_key = settings.get("SCRAPEOPS_API_KEY")
        self.scrapeops_endpoint = settings.get("SCRAPEOPS_ENDPOINT")
        self.headers_list = self.__get_headers_list()

    def __get_headers_list(self):
       try:
           response = requests .get(self.scrapeops_endpoint, params=urlencode({"api_key": self.scrapeops_api_key}))
           response.raise_for_status()
           
           json_responde = response.json()
           return json_responde.get("result",[])
       except HTTPError as err:
           print(f"Error featching headers: {err}")
           return[]

    def process_request(self, request, spider):
        if not self.headers_list:
            return
        
        random_browser_header = choice(self.headers_list)
        request.headers.setdefault("User-Agent", random_browser_header)
        print("** Novo User-Agent **")
        print(request.headers)
    

