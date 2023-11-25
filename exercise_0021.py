#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# https://github.com/Yixiaohan/show-me-the-code
# 第0021题：通常，登陆某个网站或者APP，需要使用用户名和密码。
# 密码是如何加密后存储起来的呢？请使用Python对密码加密。
# https://github.com/amusi/python-1/blob/master/Lyndon1994/0021.py
import os
from hashlib import sha256
from hmac import HMAC

def encry_password(password,salt=None):
    if salt is None:
        salt=os.urandom(8)

    if isinstance(salt,str):
        salt=salt.encode('utf-8')

    result=password.encode('utf-8')
    for i in range(10):
        result=HMAC(result,salt,sha256).digest()
    return salt+result

if __name__ =='__main__':
    print(encry_password('123456','a'))
