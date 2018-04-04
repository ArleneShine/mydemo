#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    __init__.py
    ~~~~~~~~~~~

    Module description here.

    :author: djj
    :copyright: (c) 2016, Tungee
    :date created: 2016-10-19
    :python version: 2.7
"""
from pymongo import MongoClient

from configs.mongo_config import (
    MONGO_DATABASE,
    MONGO_HOST,
    MONGO_PWD,
    MONGO_REPLICA,
    MONGO_USER,
    IS_MONGO_AUTH,
    IS_MONGO_REPLICA,
)


if IS_MONGO_REPLICA:
    mongo_url = 'mongodb://%s/?replicaSet=%s' % (MONGO_HOST, MONGO_REPLICA)
else:
    mongo_url = MONGO_HOST

client = MongoClient(mongo_url, connect=False)
db = client[MONGO_DATABASE]

if IS_MONGO_AUTH:
    db.authenticate(MONGO_USER, MONGO_PWD)

