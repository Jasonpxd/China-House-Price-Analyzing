# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import time
import utils
from django.db import models

class SecHousePirce(models.Model):
    id = models.UUIDField(primary_key=True, max_length=32,default=utils.uuid_pk)
    add_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)
    house_id = models.CharField(max_length=50)
    detail_url = models.CharField(max_length=1024)
    title = models.CharField(max_length=100)
    house_type = models.CharField(max_length=50)
    orientation = models.CharField(max_length=50)
    floor_level = models.CharField(max_length=50)
    floor_num = models.CharField(max_length=50)
    decoration = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    transportation = models.CharField(max_length=50)
    interest_num = models.CharField(max_length=50)
    watch_num = models.CharField(max_length=50)
    release_date = models.CharField(max_length=50)
    label = models.CharField(max_length=10000)
    price = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    price_per_area = models.CharField(max_length=50)
    community = models.CharField(max_length=50)
    usage = models.CharField(max_length=50)
    commercial_zone = models.CharField(max_length=50)
    total_watch = models.CharField(max_length=50)
    latest_watch_time = models.CharField(max_length=50)
    community_average_price = models.CharField(max_length=50)
    build_time = models.CharField(max_length=50)
    community_building_num = models.CharField(max_length=50)
    community_house_num = models.CharField(max_length=50)
    community_selling_house_num = models.CharField(max_length=50)
    community_renting_house_num = models.CharField(max_length=50)

    def __str__(self):
        return '<sechouse: %s>' % self.title

    class Meta:
        ordering = ['-add_time']
        db_table = 'sec_house_price'





