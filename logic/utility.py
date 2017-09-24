#!/usr/bin/env python3.6
# -*- coding:utf-8 -*-


from tornado.web import RequestHandler
import xml.etree.cElementTree as ET
from .cache import *
from .auth import auth


class RootHandler(RequestHandler):
    def get(self):
        self.render("root.htm")

class LoginHandler(RequestHandler):
    def get(self):
        self.render("login.htm")

class AdminHandler(RequestHandler):
    @auth
    def get(self):
        self.render("admin.htm")





#        t = ET.parse('logic/fonts.xml')
#        d = {}
#        for i in t.findall('map'):
#            d[i.get('code')[2:]] = i.get('name')
#        self.render("admin.htm",d=d)
