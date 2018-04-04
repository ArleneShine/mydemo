#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bson import ObjectId
import traceback
from datetime import datetime

from model.schedule import Schedule


def logic_get_schedules(year, month):
    this_month = '%s-%s' % (year, month)
    schedules = Schedule.s_col.find(
        {
            Schedule.Field.startMonth: {
                '$lte': this_month
            },
            Schedule.Field.endMonth: {
                '$gte': this_month
            }
        },
        [
            Schedule.Field.title,
            Schedule.Field.type,
            Schedule.Field.startDate,
            Schedule.Field.endDate
        ]
    )
    return [_ for _ in schedules]


def logic_add_schedule(title, s_type, start_date, end_date):
    try:
        start_month = start_date[:7]
        end_month = end_date[:7]
        schedule = Schedule.p_col.insert_one(
            {
                '_id': str(ObjectId()),
                Schedule.Field.title: title,
                Schedule.Field.type: s_type,
                Schedule.Field.startDate: start_date,
                Schedule.Field.endDate: end_date,
                Schedule.Field.startMonth: start_month,
                Schedule.Field.endMonth: end_month,
                Schedule.Field.create_time: datetime.now().strftime('%Y-%m-%d')
            }
        )
        if schedule:
            return True
        else:
            return False
    except:
        print traceback.print_exc()
        return False


def logic_delete_schedule(s_id):
    try:
        schedule = Schedule.p_col.delete_one(
            {
                '_id': s_id
            }
        )
        if schedule:
            return True
        else:
            return False
    except:
        print traceback.print_exc()
        return False
