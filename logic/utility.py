#!/usr/bin/env python3.6
# -*- coding:utf-8 -*-

import tornado.web


class RootHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("root.htm",one="smart",two="CMS")

class AdminHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("admin.htm",one="smart",two="CMS")
