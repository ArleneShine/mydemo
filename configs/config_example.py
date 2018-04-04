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
PORT = 5700

# --------------------Define Global Error-------------------------
GLOBAL_ERROR = {
    '400': {'err': 0, 'msg': 'Bad Request'},
    '401': {'err': 1, 'msg': 'Unauthorized'},
    '403': {'err': 2, 'msg': 'Forbidden'},
    '404': {'err': 3, 'msg': 'Not Found'},
}
# ----------------------------------------------------------------


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

# -----------------------Sendcloud Config--------------------------
SENDCLOUD_API_KEY = ''
SENDCLOUD_TRIGGER_API_USER = ''
SENDCLOUD_BATCH_API_USER = ''
SENDCLOUD_URL = ''
SENDCLOUD_DEFAULT_ADDRESS = ''
# -----------------------------------------------------------------

NOTICE_TEMPLATE_POOL = "004"
