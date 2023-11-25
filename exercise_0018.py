#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 第 0018 题： 将 第 0015 题中的 city.xls 文件中的内容写到 city.xml 文件中，如下所示：
# <?xmlversion="1.0" encoding="UTF-8"?>
# <root>
# <citys>
# <!--
#     城市信息
# -->
# {
#     "1" : "上海",
#     "2" : "北京",
#     "3" : "成都"
# }
# </citys>
# </root>

import xml.etree.ElementTree as ET
import json
import xlrd
xls = xlrd.open_workbook('city.xls')
table = xls.sheet_by_name('city')
# get json string
d = {}
for i in range(table.nrows):
    row = table.row_values(i)
    d[row[0]] = row[1]
json_str = json.dumps(d, ensure_ascii=False,indent=4)
# save to xml
root = ET.Element('root')
citys = ET.SubElement(root, 'citys')
citys.append(ET.Comment('城市信息'))
citys.text = json_str
tree = ET.ElementTree(root)
tree.write('citys.xml', encoding = 'utf-8', xml_declaration = True)
