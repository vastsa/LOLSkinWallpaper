# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PracticeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # titles = scrapy.Field()
    # yxpngs = scrapy.Field()
    urls = scrapy.Field()
    skin_name = scrapy.Field()  # 皮肤名
    image_urls = scrapy.Field()  # 皮肤壁纸url
    images = scrapy.Field()
