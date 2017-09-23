#!/usr/bin/env python3.6
# -*- coding:utf-8 -*-

import redis
from settings import *
from .token import *

P = redis.ConnectionPool(host = CACHE_HOST, port = CACHE_PORT, db = 0)
R = redis.StrictRedis(connection_pool = P)

def save_token(uid):
    R.setex("UID-" + uid, TOKEN_EXPIRE_TIME , generate_token())
    return token

def valid_token(uid, token):
    if R.get("UID-" + uid) == token:
        return True
    return False
