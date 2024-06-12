# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    url =  scrapy.Field()
    image = scrapy.Field()
    name = scrapy.Field()
    rating = scrapy.Field()
    price_excl = scrapy.Field()
    price_incl = scrapy.Field()
    tax = scrapy.Field()
    availability = scrapy.Field()
    category = scrapy.Field()