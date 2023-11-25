#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 第 0008 题： 一个HTML文件，找出里面的正文。

from bs4 import BeautifulSoup

def read_html_body(path):
    with open(path, 'r',encoding='utf-8') as f:
        html_note = f.read()
        # 使用 beautifulsoup 解析功能，解析器使用lxml
        soup = BeautifulSoup(html_note,"html.parser")
        # 输出标题
        print(soup.title)
        # 输出p标签的内容
        print(soup.p)
        # 输出a连接
        print(soup.a)
        # 输出body标签的内容即正文
        print(soup.find_all("body"))
        # 输出整个文件
        print(soup.get_text)
if __name__ =='__main__':
    path = r'F:\python_file\exercise\www_bilibili_default.html'
    read_html_body(path)




