#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 第0019题：将第0016题中的numbers.xls文件中的内容写入到numbers.xml文件中，如下
# '''
# <?xml version="1.0" encoding="UTF-8"?>
# <root>
# <numbers>
# <!--
# 	数字信息
# -->
#
# [
# 	[1, 82, 65535],
# 	[20, 90, 13],
# 	[26, 809, 1024]
# ]
#
# </numbers>
# </root>
# '''

import xlwt,xlrd
import json
from lxml import etree

def read_exl(file):
    exl = xlrd.open_workbook(file)
    exl_sheet = exl.sheet_by_name('numbers')
    data = []
    for i in range(exl_sheet.nrows):
        temp = [int(x) for x in exl_sheet.row_values(i)]
        data.append(temp)
    return json.dumps(data, ensure_ascii=False, indent=4, sort_keys=True)

def save_to_xml(data,new_name):
    root = etree.Element('root')
    students = etree.SubElement(root,'numbers')
    students.append(etree.Comment(u'''数字信息'''))
    students.text = data

    student_xml = etree.ElementTree(root)
    student_xml.write(new_name, pretty_print=True,xml_declaration=True,encoding='utf8')

if __name__ =='__main__':
    content = read_exl('number.xls')
    save_to_xml(content,'number.xml')

