# -*- coding: utf-8 -*-
import scrapy


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    base_url = 'https://movie.douban.com/top250/'
    start_urls = [base_url]

    def parse(self, response):
        movie_id = response.xpath("//div[@class='pic']/em/text()").extract()
        movie_name = response.xpath("//div[@class='item']//a/span[1]/text()").extract()
        movie_core = response.xpath("//div[@class='star']/span[2]/text()").extract()
        movie_img = response.xpath("//div[@class='pic']/a/img/@src").extract()
        # 下一个url的相对路径
        next_href = response.xpath("//span[@class='next']/a/@href").extract_first()
        for mid, name, score, img in zip(movie_id, movie_name, movie_core, movie_img):
            yield {
                'movie_id': mid,
                'movie_name': name,
                'movie_score': score,
                'img_urls': img
            }
        # if next_href != 'index.html':
        #     new_url = self.base_url + next_href
        #     yield scrapy.Request(new_url, callback=self.parse)
