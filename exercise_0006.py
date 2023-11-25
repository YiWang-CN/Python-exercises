#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 你有一个目录，放了你一个月的日记，都是txt，
# 为了避免分词的问题，假设内容是英文，请统计出你认为每篇日记最重要的词。
# https://blog.csdn.net/Lockey23/article/details/79435789
# https://www.runoob.com/note/27030
# https://blog.csdn.net/lilongsy/article/details/99853925
from exercise_0004 import exercise_0004
import os

def get_diary_path(dir_path):
    list=[]
    for path in os.listdir(dir_path):
        list.append(dir_path+'/'+path)
    return list

def read_diary(dia_path):
    with open(dia_path, 'r')as f:
        data=f.read()
    return data

if __name__ == '__main__':
    dia_list = get_diary_path('./diary')
    for dia_path in dia_list:
        data = read_diary(dia_path)
        keyword = exercise_0004.get_word_num(data)
        with open(dia_path, 'r+') as f:
            content = f.read()
            # 将文件指针移动到文件开头  fileObject.seek(offset[, whence])
            f.seek(0, 0)
            f.write('Keyword: '+keyword +'\n'+ content)
            (file, ext) = os.path.splitext(dia_path)
        os.rename(dia_path, file+'_Keyword_'+keyword+'.txt')