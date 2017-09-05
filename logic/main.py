#!/usr/bin/env python3.6
# -*- coding:utf-8 -*-

import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello world")
