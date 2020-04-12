# -*- coding: utf-8 -*-
import scrapy
from practice.items import PracticeItem
from urllib import parse


class LolskinSpider(scrapy.Spider):
    name = 'lolskin'
    allowed_domains = ['lolskin.cn']
    start_urls = ['https://lolskin.cn/champions.html']

    # 获取所有英雄链接
    def parse(self, response):
        item = PracticeItem()
        item['urls'] = response.xpath('//div[2]/div[1]/div/ul/li/a/@href').extract()
        for url in item['urls']:
            self.csurl = 'https://lolskin.cn'
            yield scrapy.Request(url=parse.urljoin(self.csurl, url), dont_filter=True, callback=self.bizhi)
        return item

    # 获取所有英雄皮肤链接
    def bizhi(self, response):
        skins = (response.xpath('//td/a/@href').extract())
        for skin in skins:
            yield scrapy.Request(url=parse.urljoin(self.csurl, skin), dont_filter=True, callback=self.get_bzurl)

    # 采集每个皮肤的壁纸，获取壁纸链接
    def get_bzurl(self, response):
        item = PracticeItem()
        image_urls = response.xpath('//body/div[1]/div/a/@href').extract()
        image_name = response.xpath('//h1/text()').extract()
        yield {
            'image_urls': image_urls,
            'image_name': image_name
        }
        return item
