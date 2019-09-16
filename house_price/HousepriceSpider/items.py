# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from sechouse.models import SecHousePirce

class HousepricespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Woi5jItem(DjangoItem):
    django_model = SecHousePirce
    # house_id = scrapy.Field()
    # detail_url = scrapy.Field()
    # title = scrapy.Field()
    # house_type = scrapy.Field()
    # orientation = scrapy.Field()
    # floor_level = scrapy.Field()
    # floor_num = scrapy.Field()
    # decoration = scrapy.Field()
    # position = scrapy.Field()
    # transportation = scrapy.Field()
    # interest_num = scrapy.Field()
    # watch_num = scrapy.Field()
    # release_date = scrapy.Field()
    # label = scrapy.Field()
    # price = scrapy.Field()
    # area = scrapy.Field()
    # price_per_area = scrapy.Field()
    # community = scrapy.Field()
    # usage = scrapy.Field()
    # commercial_zone = scrapy.Field()
    # total_watch = scrapy.Field()
    # latest_watch_time = scrapy.Field()
    # community_average_price = scrapy.Field()
    # build_time = scrapy.Field()
    # community_building_num = scrapy.Field()
    # community_house_num = scrapy.Field()
    # community_selling_house_num = scrapy.Field()
    # community_renting_house_num = scrapy.Field()

