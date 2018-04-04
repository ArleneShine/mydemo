# -*- coding: utf-8 -*-
"""
    configs/configs.example.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Project configuration example file. Should be copied to
    `configs/__init__.py` before running the project.

    :author: Jason Wang
    :copyright: (c) 2016, Tungee
    :date created: 2016-08-15
    :python version: 2.7
"""

DEBUG = True
ROOT_PATH = '~/workthub/email_station/email_station/'
PORT = 12345


EMAIL_API_URL = u'http://112.74.93.18:10255/internal-api/sendcloud'  # Email api

# EMAIL_TYPE = [u'NOTICE', u'WARNING', u'TIMING']  # Email type
# TEMPLATE_VARIABLE = [u'name', u'subject', u'receiver'] # 可以通过api进行修改的属性
# TEMPLATE_POOL_VARIABLE = [u'full_name', u'params', u'html', u'email_type', u'url_type'] # 可以通过api进行修改的属性

# --------------model to url----------------
find_url = {
    u'Sendcloud': u'http://112.74.93.18:10255/internal-api/sendcloud',
}
# url_types = [u'Sendcloud']

PER_NUM = 100