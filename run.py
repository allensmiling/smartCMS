#!/usr/bin/env python3.6
# -*- coding:utf-8 -*-


import os.path
import tornado.ioloop
import tornado.web
import tornado.httpserver
from tornado.options import define, options
from settings import *
from router import urls

define("port", default=APP_PORT, type=int, help="run app on specific port")
t = os.path.join(os.getcwd(), "template")
s = os.path.join(os.getcwd(), "static")

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers = urls, template_path = t, static_path = s, debug = DEBUG, cookie_secret = COOKIE_SECRET)
    if DEBUG:
        app.listen(options.port)
    else:
        server = tornado.httpserver.HTTPServer(app)
        server.bind(options.port)
        server.start(0)
    tornado.ioloop.IOLoop.current().start()
