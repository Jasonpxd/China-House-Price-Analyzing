# -*- coding: utf-8 -*-
import scrapy


class LianjiaspiderSpider(scrapy.Spider):
    name = 'LianjiaSpider'
    allowed_domains = ['lianjian.com']
    start_urls = ['http://lianjian.com/']

    def parse(self, response):
        pass
