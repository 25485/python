# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WebtoonscraperItem(scrapy.Item):
    # define the fields for your item here like:
    days = scrapy.Field()
    thumbNail = scrapy.Field()
    title = scrapy.Field()
    pass
