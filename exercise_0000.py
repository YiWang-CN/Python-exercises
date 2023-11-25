#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，
# 类似于微信未读信息数量那样的提示效果。 类似于效果
# 参考
# https://zhuanlan.zhihu.com/p/32889858
# https://blog.csdn.net/qq_28790663/article/details/88581931


from PIL import Image, ImageDraw, ImageFont
import random

def put_num_upright(pic, num):
    im = Image.open(pic)
    num = str(num)
    draw = ImageDraw.Draw(im)
    w,h = im.size
    font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 40)
    fillcolor = '#ff0000'
    draw.text((w-25, -1), '%s' % num, font =font, fill = fillcolor)
    im.save(r'F:\python_file\exercise\img\0000.jpg','jpeg')

if __name__ == '__main__':
    pic = r'F:\python_file\exercise\img\1521966572.jpg'
    num = random.randint(1, 10)
    put_num_upright(pic, num)
