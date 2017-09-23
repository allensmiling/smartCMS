#!/usr/bin/env python3.6
# -*- coding:utf-8 -*-


import random
from settings import *


def generate_token(length=30, chars=UNICODE_ASCII_CHARACTER_SET):
    rand = random.SystemRandom()
    return ''.join(rand.choice(chars) for x in range(length))
