# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item

class ThenorthfacedotcomItem(Item):
    name = Field()
    category = Field()
    price = Field()
    image = Field()
    description = Field()
    url = Field()
