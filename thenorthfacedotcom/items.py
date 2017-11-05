# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ThenorthfacedotcomItem(scrapy.Item):
    name = scrapy.Field()
    category = scrapy.Field()
    price = scrapy.Field()
    image = scrapy.Field()
    description = scrapy.Field()
    url = scrapy.Field()
