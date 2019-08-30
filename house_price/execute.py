#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@author: pxd
@contact: peixudong@herobt.com
@file: debug.py
@time: 2019/7/17 0017 11:05
'''

from scrapy.cmdline import execute
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

print os.path.dirname(os.path.abspath(__file__))
def run(task_id,redis_key,title,min_price,check):
    # cmd = 'scrapy crawl keyword -a sku_id=%s -a task_id=%s ' % (sku_id,task_id)
    cmd = 'scrapy crawl keyword -a task_id=%s -a redis_key=%s -a min_price=%s -a check=%s -a' % (task_id,redis_key,min_price,check)
    cmd = cmd.split()
    cmd.append("title=" + title.encode('utf-8'))
    print cmd
    execute(cmd)

def run_association(task_id, url, redis_key):
    cmd = 'scrapy crawl association -a task_id=%s -a url=%s -a redis_key=%s' % (task_id,url, redis_key)
    cmd = cmd.split()
    print cmd
    execute(cmd)

def run_search_sku(keyword,redis_key):
    cmd = 'scrapy crawl search_sku -a redis_key=%s -a' % redis_key
    cmd = cmd.split()
    cmd.append("keyword="+keyword.encode('utf-8'))
    print cmd
    execute(cmd)

def run_schedule(task_id, website, url_list, page_count, code):

    cmd = 'scrapy crawl %s -a task_id=%s -a page_count=%s -a code=%s -a' % (website,task_id, page_count, code)
    cmd = cmd.split()
    cmd.append("url_list="+url_list)
    print cmd
    execute(cmd)


def run_classification(task_id,url,redis_key):
    cmd = 'scrapy crawl class_indicator -a task_id=%s -a url=%s -a redis_key=%s' % (task_id,url,redis_key)
    cmd = cmd.split()
    print cmd
    execute(cmd)

if __name__ == '__main__':
    # sku_id = '024128dc5495498fae5f7417d462d358'
    # task_id = '123'
    #
    # url = 'https://www.mysmartprice.com/mobile/apple-iphone-xr-256gb-msp15218'
    # run_association(sku_id,task_id,url)
    # run_search_sku('iphone x')

    # run(sku_id,task_id)
    # execute(["scrapy","crawl","tatacliq"])
    # url = 'https://www.mysmartprice.com/mobile/apple-iphone-xr-256gb-msp15218'
    # run_association(sku_id,task_id,url)

    # url = 'https://www.mysmartprice.com/mobile/apple-iphone-xr-256gb-msp15218'
    # run_association(sku_id,task_id,url)
    # # run_search_sku('iphone')
    # execute(["scrapy","crawl","tatacliq"])
    # url = 'https://www.mysmartprice.com/mobile/apple-iphone-xr-256gb-msp15218'
    # run_association(sku_id,task_id,url)

    url = "https://www.flipkart.com/realme-3-pro-lightning-purple-64-gb/p/itmfgzr2jckcttnx?pid=MOBFFMG3H499XJZY&lid=LSTMOBFFMG3H499XJZYZUF0U4&marketplace=FLIPKART&srno=b_2_68&otracker=browse&fm=organic&iid=fef73194-4ab6-4b7c-9888-9041559b8d89.MOBFFMG3H499XJZY.SEARCH&ssid=fp0d2ht26o0000001566443258315"
    run_classification(111,url,'lll')

