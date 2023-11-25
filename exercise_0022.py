#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 第0022题： iPhone 6、iPhone 6 Plus多次上市开卖。请查看你写得第0005题的代码是否可以复用。

from exercise_0005 import exercise_0005


PHONE = {'iPhone5':(1136,640), 'iPhone6':(1134,750), 'iPhone6P':(2208,1242)}


if __name__ =='__main__':
    exercise_0005.picture(r'F:\python_file\exercise\img',1134,750,phone='iPhone6')
    exercise_0005.picture(r'F:\python_file\exercise\img',2208,1242,phone='iPhone6P')



