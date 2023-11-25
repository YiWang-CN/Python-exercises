#!/usr/bin/env python 
# -*- coding:utf-8 -*-
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
　　　'CHARSET':'utf-8',
　　　'COLLATION':'utf8_general_ci',
　　   #注意有中文时设置该utf8格式，同时建立数据库时：CREATE DATABASE mydb DEFAULT CHARACTER SET utf8 COLLATION utf8_general_ci;
    }
}
