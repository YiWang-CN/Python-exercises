#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 第 0015 题： 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：
import re
import xlwt

def read2xls(x):
    datatable = xlwt.Workbook(encoding='utf8', style_compression=0)
    newsheet = datatable.add_sheet('city',cell_overwrite_ok=True)
    num = 0
    with open(x, encoding='utf8')as f:
        text = f.read()
        info = re.compile(r'"(\d+)".*?"(.*?)"')
        for x in info.findall(text):
            for i in range(len(x)):
                newsheet.write(num, i, x[i])
            num+=1
        datatable.save('city.xls')
if __name__=='__main__':
    read2xls('city.txt')