#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
import os



def get_path(dir_path):
    list=[]
    for path in os.listdir(dir_path):
        list.append(dir_path+'/'+path)
    return list

def read_code(cod_path):
    with open(cod_path, 'r', encoding='utf8')as f:
        lines = f.readlines()
        rows = len(lines)
        space =0
        comm = 0
        for line in lines:
            if line == '\n':
                space+=1
            if line[0] =='#':
                comm+=1
            data ={
                'rows': rows,
                'space': space,
                'comm': comm
            }
    return data

if __name__ == '__main__':
    dir_path = r'F:\python_file\exercise\test_code'
    list = get_path(dir_path)
    all_row = 0
    all_space = 0
    all_comm = 0

    for code in list:
        data = read_code(code)
        all_row+=data.get('rows')
        all_space+=data.get('space')
        all_comm+=data.get('comm')
    print('所有代码的行数：%d' % all_row)
    print('其中注释行数：%d' % all_comm)
    print('其中空行数：%d' % all_space)
