# -*- coding: utf-8 -*-

from pymongo.collection import Collection
from pymongo.read_preferences import ReadPreference

from model import db


class User(object):
    """
    * `_id` (string)
    * `name` (string) - 用户名
    * `create_time` (date) - 事件创建时间
    * `update_time` (date) - 事件创建时间
    """
    COL_NAME = 'user'
    p_col = Collection(
        db, COL_NAME, read_preference=ReadPreference.PRIMARY_PREFERRED
    )
    s_col = Collection(
        db, COL_NAME, read_preference=ReadPreference.SECONDARY_PREFERRED
    )

    class Field(object):
        _id = '_id'
        name = 'name'
        create_time = 'create_time'
        update_time = 'update_time'

    p_col.create_index(Field.name, unique=True, sparse=False)
