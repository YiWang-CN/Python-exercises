#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 第 0001 题： 做为 Apple Store App 独立开发者，
# 你要搞限时促销，为你的应用生成激活码（或者优惠券），
# 使用 Python 如何生成 200 个激活码（或者优惠券）？

# 参考
# https://blog.csdn.net/qq_24822271/article/details/102579663
# https://zhuanlan.zhihu.com/p/32895663

import string
import random

def gen_key(num,len=8):
    result=[]
    base_str = string.ascii_letters + string.digits    # 所有的大小写字母和数字
    for i in range(num):
        key_list = [random.choice(base_str) for i in range(len)]
        # print(key_list)
        key_str = ''.join(key_list)   # 将列表用join形成字符串
        # print(key_str)
        result.append(key_str)
    return result

if __name__  ==  '__main__':
    keys = gen_key(200)
    print(keys)
