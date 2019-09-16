# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class HousepricespiderPipeline(object):
    def open_spider(self,spider):
        self.f = open('5i5j.txt','a')
    def process_item(self, item, spider):
        data = dict(item)
        print json.dumps(data).decode("unicode-escape")
        if spider.name == '5i5j':
            self.f.write(json.dumps(data).decode("unicode-escape")+'\n')
            item.save()


        return item
    def close_spider(self,item):
        self.f.close()

