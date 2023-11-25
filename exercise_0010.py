#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 第 0010 题： 使用 Python 生成类似于下图中的字母验证码图片
# https://blog.csdn.net/qq_24822271/article/details/102609456


import random
import string
from PIL import Image,ImageDraw,ImageFont,ImageFilter

def get_char():
    return random.choice(string.ascii_letters)
def generator_font_color():
    return (random.randint(32,255),random.randint(32,255),random.randint(32,255))
def generator_bgcolor():
    return (random.randint(64,355),random.randint(64,355),random.randint(64,355))
def img_produce():
    w = 60*4
    h = 60
    img = Image.new('RGB',(w,h),(255,255,255))
    font = ImageFont.truetype(r'C:\Windows\Fonts\Arial.ttf',60)
    draw = ImageDraw.Draw(img)
    for i in range(w):
        for j in range(h):
            draw.point((i,j),fill=generator_bgcolor())
    for i in range(4):
            draw.text((i*60+10,0),get_char(),font=font,fill=generator_font_color())
    img.save('0010.jpg','jpeg')

if __name__ == '__main__':
    img_produce()