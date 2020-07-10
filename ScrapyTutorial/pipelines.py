# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
from pymongo import MongoClient
import pymysql
import scrapy
from scrapy.pipelines.images import ImagesPipeline


class FilePipeline(object):

    def __init__(self):
        self.file = open('movie.txt', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        self.file.write(json.dumps(item, ensure_ascii=False) + ",")
        # self.file.flush()
        return item

    def close_spider(self, spider):
        self.file.close()


class MongoPipeline(object):

    def __init__(self):
        self.client = MongoClient(host='cvm', port=27017)

    def process_item(self, item, spider):
        self.client.douban.movie.insert_one(item)
        return item

    def close_spider(self, spider):
        self.client.close()


'''
msyql需要提前建库和表
'''


class MysqlPipeline:
    def __init__(self):
        self.client = pymysql.connect(
            host='cvm', port=3306, user='root', password='Gz,.9918xu',
            db='douban', charset='utf8')
        self.cursor = self.client.cursor()

    def process_item(self, item, spider):
        args = [int(item['movie_id']), item['movie_name'], item['movie_score']]
        sql = 'insert into t_movie VALUES (%s,%s,%s)'
        self.cursor.execute(sql, args)
        self.client.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.client.close()


class SaveImgPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        '''
        # 如果item[urls]里里面是列表，用下面
        urls= item['urls']
        for url in urls:
            yield scrapy.Request(url,meta={"item",item})
        '''
        # 如果item[urls]里里面是一个图片地址，用这下面的
        yield scrapy.Request(item['img_urls'], meta={"item": item})

    def file_path(self, request, response=None, info=None):
        item = request.meta["item"]
        # 去掉文件里的/,避免创建图片文件时出错
        filename = item["movie_name"].replace("/", "-")+".jpg"

        return filename
