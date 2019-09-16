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
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def run():
    # cmd = 'scrapy crawl keyword -a sku_id=%s -a task_id=%s ' % (sku_id,task_id)
    cmd = 'scrapy crawl 5i5j '
    cmd = cmd.split()
    print cmd
    execute(cmd)

if __name__ == '__main__':
    run()

