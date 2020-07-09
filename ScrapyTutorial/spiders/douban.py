# -*- coding: utf-8 -*-
import scrapy


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250/']

    def parse(self, response):
        movie_name = response.xpath("//div[@class='item']//a/span[1]/text()").extract()
        movie_core = response.xpath("//div[@class='star']/span[2]/text()").extract()
        for n, c in zip(movie_name, movie_core):
            yield {
                'movie_name': n,
                'movie_core': c
            }
