#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 第0017题：将第0014题中的student.xls文件中的内容写入到student.xml文件中，如

# <?xml version="1.0" encoding="UTF-8"?>
# <root>
# <students>
# <!--
# 	学生信息表
# 	"id" : [名字, 数学, 语文, 英文]
# -->
# {
# 	"1" : ["张三", 150, 120, 100],
# 	"2" : ["李四", 90, 99, 95],
# 	"3" : ["王五", 60, 66, 68]
# }
# </students>
# </root>

import xlrd
import json
from lxml import etree

# 读取 Excel 文件
workbook = xlrd.open_workbook('student.xls')
sheet = workbook.sheet_by_index(0)

# 从 Excel 中提取数据并生成字典
data = {}
for row in range(sheet.nrows):  # Assuming the first row contains headers
    student_id = str(int(sheet.cell_value(row, 0)))
    name = sheet.cell_value(row, 1)
    math = int(sheet.cell_value(row, 2))
    chinese = int(sheet.cell_value(row, 3))
    english = int(sheet.cell_value(row, 4))
    data[student_id] = [name, math, chinese, english]
print(data)
# 创建 XML 结构
root = etree.Element("root")
students = etree.SubElement(root, "students")
comment = etree.Comment(
    ''' 
    学生信息表
    "id" : [名字, 数学, 语文, 英文]
    '''
)
students.append(comment)
students.text = json.dumps(data, ensure_ascii=False, indent=4, sort_keys=True)

tree = etree.ElementTree(root)
tree.write("student.xml", pretty_print=True,encoding='utf-8')
print("已生成 XML 文件 'student.xml'，内容来自 Excel 文件。")
