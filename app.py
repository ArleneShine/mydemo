# -*- coding: utf-8 -*-
"""
    app
    ~~~

    Flask app instance.

    :author: Yiming Lin
    :copyright: (c) 2016, Tungee
    :date created: 2016-12-06
    :python version: 2.7
"""
from flask import (
    Flask
)

from configs import (
    DEBUG
)

# Init Flask app
app = Flask(__name__)
app.debug = DEBUG


