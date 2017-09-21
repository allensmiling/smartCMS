#!/usr/bin/env python3.6
# -*- coding:utf-8 -*-

import tornado.web
import xml.etree.cElementTree as ET


class RootHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("root.htm",one="smart",two="CMS")

class AdminHandler(tornado.web.RequestHandler):
    def get(self):
        t = ET.parse('logic/fonts.xml')
        d = {}
        for i in t.findall('map'):
            d[i.get('code')[2:]] = i.get('name')
        self.render("admin.htm",d=d)
