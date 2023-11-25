#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 纯文本文件numbers.txt，里面的内容（包括方括号）如下所示：
# 将上述内容写入numbers.xls文件中，如下图所示：
import re
import xlwt

def read2xls(x):
    datatable = xlwt.Workbook(encoding='utf8', style_compression=0)
    newsheet = datatable.add_sheet('numbers',cell_overwrite_ok=True)
    num = 0
    with open(x, encoding='utf8')as f:
        text = f.read()
        #注意: 正则表达式中[]有明确含义，如需匹配[可以使用\[
        info = re.compile(r'\[(\d+), (\d+), (\d+)\]')
        tem = info.findall(text)
        for x in info.findall(text):
            for i in range(len(x)):
                newsheet.write(num, i, x[i])
            num+=1
        datatable.save('number.xls')
if __name__=='__main__':
    read2xls('numbers.txt')