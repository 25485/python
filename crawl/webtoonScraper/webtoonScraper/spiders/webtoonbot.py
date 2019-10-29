# -*- coding: utf-8 -*-
import scrapy

from webtoonScraper.items import WebtoonscraperItem


class WebtoonbotSpider(scrapy.Spider):
    name = 'webtoonbot'
    # allowed_domains = ['http://comic.naver.com']
    start_urls = ['https://comic.naver.com/webtoon/weekday.nhn']

    def parse(self, response):
        for href in response.css("ul > li > a::attr('href')"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_contents)

    def parse_contents(self, response):
        for sel in response.css('div.list_area.daily_all'):
            item = WebtoonscraperItem()
            for data in response.xpath('//*[@id="content"]/div[4]/div/div'):
                item['days'] = data.xpath('h4/span/text()').extract()[0]
                item['thumbNail'] = data.xpath('ul/li/div/a/img/@src').extract()
                item['title'] = data.xpath('ul/li/a/@title').extract()
                yield item
