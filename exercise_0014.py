#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 第0014题：纯文本文件student.txt为学生信息，里面的内容（包括花括号）如下所示：
# 将上述内容写入到student.xls文件中，如下图所示：
import re
import xlwt

def read2xls(x):
    datatable = xlwt.Workbook(encoding='utf-8',style_compression=0)
    newsheet = datatable.add_sheet('student',cell_overwrite_ok= True)
    num = 0
    with open(x,'r',encoding='utf8') as f:

        text = f.read()
        info = re.compile(r'"(\d+)":\["(.*?)",(\d+),(\d+),(\d+)]')
        for x in info.findall(text):
            for i in range(len(x)):
                newsheet.write(num,i,x[i])
            num+=1
        datatable.save('student.xls')
if __name__ == "__main__":
    read2xls('student.txt')









