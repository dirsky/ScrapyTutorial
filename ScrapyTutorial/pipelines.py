# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json


class ScrapytutorialPipeline(object):

    def open_spider(self, spider):
        self.file = open('movie.txt', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        self.file.write(json.dumps(item, ensure_ascii=False))
        # self.file.flush()
        return item

    def close_spider(self, spider):
        self.file.close()
