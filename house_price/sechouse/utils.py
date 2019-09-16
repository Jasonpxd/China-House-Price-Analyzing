# -*- coding: utf-8 -*-

import time
import uuid


def current_time_millis():
    return round(1000 * time.time())

def getDateStr():
    return time.strftime("%Y%m%d")

def uuid_pk():

    return str(uuid.uuid4()).replace('-', '')