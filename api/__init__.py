#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Blueprint


api = Blueprint('/api', __name__)


# Web api error codes
ERROR_CHANNEL = 1000
ERROR_TEMPLATE_POOL = 2000
ERROR_TEMPLATE = 3000
ERROR_EMAIL = 4000


from api import schedule
