# -*- coding: utf-8 -*-
import scrapy


class ToScrapeCSSSpider(scrapy.Spider):
    name = "day5"
    start_urls = [
        'https://www.brainyquote.com/topics/love-quotes',
    ]

    def parse(self, response):
        for quote in response.css("div.qll-bg"):
            yield {
                'text': quote.css("a.b-qt::text").extract_first(),
                'author': quote.css("a.bq-aut::text").extract_first(),
                'tags': quote.css("div.kw-box > a.qkw-btn::text").extract()
            }
