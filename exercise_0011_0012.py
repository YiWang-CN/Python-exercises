#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，
# 当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

# 第 0012 题： 敏感词文本文件 filtered_words.txt，
# 里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，
# 例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
# https://blog.csdn.net/qq_24822271/article/details/102609500
import re

def filtered_words(path):
    words=[]
    with open(path,'r',encoding='utf8') as f:
        data = f.read()
        list_data = data.split('\n')
        return list_data
def get_input():
    path = r'F:\python_file\exercise\filtered_words.txt'
    inputword = input('please input:')
    for word in filtered_words(path):
        if word in inputword:
            print('Freedom')
            p = re.sub(word,'*',inputword)
            return p
    return 'Human Rights'
if __name__ =="__main__":
    print(get_input())

