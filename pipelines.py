# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import re
from scrapy.pipelines.images import ImagesPipeline
import scrapy


# class PracticePipeline(object):
#     def __init__(self):
#         self.file = open('text.csv', 'a+')
#
#     def process_item(self, item, spider):
#         # os.chdir('lolskin')
#         # for title in item['titles']:
#         #     os.makedirs(title)
#         skin_name = item['skin_name']
#         skin_jpg = item['skin_jpg']
#         for i in range(len(skin_name)):
#             self.file.write(f'{skin_name[i]},{skin_jpg}\n')
#         self.file.flush()
#         return item
#
#     def down_bizhi(self, item, spider):
#         self.file.close()


class LoLPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url, meta={'image_name': item['image_name']})

    # 修改下载之后的路径以及文件名
    def file_path(self, request, response=None, info=None):
        image_name = re.findall('/skin/(.*?)/', request.url)[0] + "/" + request.meta[f'image_name'][0] + '.jpg'
        return image_name
