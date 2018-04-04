#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    server
    ~~~~~~

    Where flask app starts.

    :author: Yiming Lin
    :copyright: (c) 2016, Tungee
    :date created: 2016-12-06
    :python version: 2.7
"""
from gevent import monkey
import traceback
monkey.patch_all()


import sys
reload(sys)
sys.setdefaultencoding('utf8')

from gevent.wsgi import WSGIServer

from app import app
from configs import PORT
from api import api
# from logic.send_error_email import send_error_email


app.register_blueprint(api, url_prefix='/api')

if app.debug:
    # Run with reloader
    from werkzeug.serving import run_with_reloader

    http_server = WSGIServer(('0.0.0.0', PORT), app)

    @run_with_reloader
    def run_server():
        http_server.serve_forever()
else:
    try:
        http_server = WSGIServer(('0.0.0.0', PORT), app)
        http_server.serve_forever()
    except:
        traceback.print_exc()
        # send_error_email(110)

