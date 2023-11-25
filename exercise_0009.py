#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 第 0009 题： 一个HTML文件，找出里面的链接。
from bs4 import BeautifulSoup
def get_html_link(path):
    with open(path,encoding='utf-8') as f:
        soup =BeautifulSoup(f,'html.parser')
        urls = soup.find_all('a')
        for u in urls:
            print(u['href'])



if __name__ == '__main__':
    path = r'F:\python_file\exercise\www_bilibili_default.html'
    get_html_link(path)