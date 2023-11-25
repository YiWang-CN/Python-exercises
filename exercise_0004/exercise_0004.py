#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 第 0004 题：任一个英文的纯文本文件，统计其中单词出现的个数。
# https://zhuanlan.zhihu.com/p/33007739
# https://blog.csdn.net/yyw794/article/details/78788560
# https://blog.csdn.net/sinat_24091225/article/details/77925473
# https://www.delftstack.com/zh/howto/python/get-first-key-in-dictionary-python/#%e4%bd%bf%e7%94%a8-iter-%e5%87%bd%e6%95%b0%e8%8e%b7%e5%8f%96%e5%ad%97%e5%85%b8%e4%b8%ad%e7%9a%84%e7%ac%ac%e4%b8%80%e4%b8%aa%e9%94%ae
# https://docs.python.org/zh-cn/3.10/library/collections.html?highlight=counter#counter-objects

import re
from collections import Counter
def get_word_num(data):
    exclude_words = ['the', 'in', 'of', 'and', 'to', 'has', 'that', 'this', 'i', 'is', 'are', 'a', 'with', 'as', 'an']
    print(data)
    result = re.split(r'[\W]', data)  # \W 非字母数字及下划线  [^a-zA-Z0-9_]
    print(result)
    # result.remove('') #出错
    # filter(None, your_list)， None代表不输入函数，也就是[x for x in your_list if x]
    result = list(filter(None, result))
    for i in range(len(result)):
        result[i] = result[i].lower()
    print(result)
    num_dic = Counter(result)
    print(num_dic)

    # print(num_dic.most_common(1))
    for word in exclude_words:
        num_dic[word] = 0
    keyword = num_dic.most_common(1)[0][0]
    return keyword

if __name__ == "__main__":
    with open(r'F:\python_file\exercise\test.txt', 'r')as f:
        data=f.read()
    get_word_num(data)