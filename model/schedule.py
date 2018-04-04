# -*- coding: utf-8 -*-

from pymongo.collection import Collection
from pymongo.read_preferences import ReadPreference

from model import db


class Schedule(object):
    """
    * `_id` (string)
    * `title` (string) - 事件名
    * `type` (string) - 事件分类
    * `startDate` (string) - 事件开始时间
    * `endDate` (string) - 事件结束时间
    * `startMonth` (string) - 事件开始月份
    * `endMonth` (string) - 事件结束月份
    * `create_time` (date) - 事件创建时间
    """
    COL_NAME = 'schedule'
    p_col = Collection(
        db, COL_NAME, read_preference=ReadPreference.PRIMARY_PREFERRED
    )
    s_col = Collection(
        db, COL_NAME, read_preference=ReadPreference.SECONDARY_PREFERRED
    )

    class Field(object):
        _id = '_id'
        title = 'title'
        type = 'type'
        startDate = 'startDate'
        endDate = 'endDate'
        startMonth = 'startMonth'
        endMonth = 'endMonth'
        create_time = 'create_time'

    p_col.create_index(Field.startMonth, unique=False, sparse=False)
    p_col.create_index(Field.endMonth, unique=False, sparse=False)
