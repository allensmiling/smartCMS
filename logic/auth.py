#!/usr/bin/env python3.6
# -*- coding:utf-8 -*-



def auth(func):
    def w(self, *args, **kwargs):
        try:
            uid = self.get_secure_cookie('uid')
            token = self.get_secure_cookie('token')
        except:
            self.redirect("/login")
        if not token or not uid:
            self.redirect("/login")
        else:
            if not valid_token(uid, token):
                self.redirect("/login")
            else:
                func(self, *args, **kwargs)
    return w



