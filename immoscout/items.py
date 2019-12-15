# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import re
from scrapy.loader.processors import MapCompose

def remove_currency_separator(price):
    if price:
        return re.sub("\,|\.","",price)

class ImmoscoutItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ObjectItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field(
        input_processor = MapCompose(remove_currency_separator)
    )
    currency = scrapy.Field()
    date_added = scrapy.Field()
    date_updated = scrapy.Field()
    address = scrapy.Field()
    country = scrapy.Field()
    city = scrapy.Field()
    neighborhood = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    url = scrapy.Field()
