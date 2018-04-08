# -*- coding: utf-8 -*-
import traceback
from bson import ObjectId
from datetime import datetime

from model.user import User


def logic_get_user_id(user_name):
    user = logic_get_one_user(user_name)
    if user:
        return user['_id']
    else:
        return logic_add_user(user_name)


def logic_get_one_user(user_name):
    user = User.s_col.find_one({'name': user_name})
    return user


def logic_add_user(user_name):
    user_id = str(ObjectId())
    try:
        User.p_col.insert_one({
            '_id': user_id,
            User.Field.name: user_name,
            User.Field.create_time: datetime.now().strftime('%Y-%m-%d'),
            User.Field.update_time: datetime.now().strftime('%Y-%m-%d')
        })
        return user_id
    except:
        print traceback.print_exc()
        return None
