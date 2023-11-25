#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 你有一个目录，装了很多照片，把它们的大小变成都不大于iPhone5解析的大小  1136*640。
# https://blog.csdn.net/weixin_48089790/article/details/115186202
# https://blog.csdn.net/u011509971/article/details/70244688
from PIL import Image
import os
def picture(filename, w, h, phone='iPhone5'):
    for i in os.listdir(filename):  # 遍历文件夹中的文件
        # print(i)
        if 'new' not in i:
            if os.path.splitext(i)[1] == '.png' or ".jpg":  # 如果文件后缀名为png，则修改照片尺寸
                im = Image.open(os.path.join(filename, i))  # 利用PIL库修改图片尺寸
                print(im)
                im.thumbnail((w, h))
                im.save(r'F:\python_file\exercise\img\new'+'_'+phone+'_'+i)

if __name__ == '__main__':

    picture(r'F:\python_file\exercise\img', 1136, 640)

