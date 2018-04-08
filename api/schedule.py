#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from flask import jsonify, request, abort
import traceback

from api import api
from logic.schedule import (
    logic_get_schedules,
    logic_add_schedule,
    logic_delete_schedule
)


@api.route('/schedules', methods=['GET'])
def api_get_schedules():
    year = month = None
    try:
        year = request.args.get('year').strip()
        month = request.args.get('month').strip()
        if not re.match(u'\d{4}$', year) or not re.match(u'\d{1,2}$', month):
            raise ValueError('year or month is wrong')
        if re.match(u'\d$', month):
            month = '0%s' % month
    except:
        print traceback.print_exc()
        return jsonify(stat=0, msg="参数错误"), 400, {"Access-Control-Allow-Credentials": "true"}

    # 判断用户
    user_name = request.cookies.get('username')
    if user_name:
        schedules = logic_get_schedules(year, month, user_name)
        return jsonify(stat=1, schedules=schedules), 200, {"Access-Control-Allow-Credentials": "true"}
    else:
        return jsonify(stat=0, msg="请先登录"), 403, {"Access-Control-Allow-Credentials": "true"}


@api.route('/schedules/add', methods=['POST'])
def api_add_schedule():
    title = s_type = start_date = end_date = None
    try:
        title = request.form.get('title').strip()
        s_type = request.form.get('type').strip()
        start_date = request.form.get('startdate').strip()
        end_date = request.form.get('enddate').strip()

        if not re.match(u'\d{4}-\d{2}-\d{2}$', start_date) or not re.match(u'\d{4}-\d{2}-\d{2}$', end_date):
            raise ValueError('start_date or end_date is wrong')

    except:
        print traceback.print_exc()
        return jsonify(stat=0, msg="参数错误"), 400, {"Access-Control-Allow-Credentials": "true"}

    # 判断用户
    user_name = request.cookies.get('username')
    if user_name:
        event_id = logic_add_schedule(title, s_type, start_date, end_date, user_name)
        if event_id:
            return jsonify(stat=1, id=event_id), 200, {"Access-Control-Allow-Credentials": "true"}
        return jsonify(stat=0, msg="新增事件失败"), 403, {"Access-Control-Allow-Credentials": "true"}
    else:
        return jsonify(stat=0, msg="请先登录"), 403, {"Access-Control-Allow-Credentials": "true"}


@api.route('/schedules/remove', methods=['DELETE'])
def api_delete_schedule():
    s_id = None
    try:
        s_id = request.form.get('id').strip()
    except:
        print traceback.print_exc()
        return jsonify(stat=0, msg="参数错误"), 400, {"Access-Control-Allow-Credentials": "true"}

    # 判断用户
    user_name = request.cookies.get('username')
    if user_name:
        status = logic_delete_schedule(s_id, user_name)
        if status:
            return jsonify(stat=1, msg="SUCCESS"), 200, {"Access-Control-Allow-Credentials": "true"}
        else:
            return jsonify(stat=0, msg="用户名与事件id不对应"), 403, {"Access-Control-Allow-Credentials": "true"}
    else:
        return jsonify(stat=0, msg="请先登录"), 403, {"Access-Control-Allow-Credentials": "true"}

