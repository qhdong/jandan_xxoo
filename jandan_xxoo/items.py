# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class JandanItem(scrapy.Item):
    id = scrapy.Field()
    author = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    like = scrapy.Field()
    dislike = scrapy.Field()
