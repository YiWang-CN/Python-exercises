#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
import urllib.request
url = r'F:\python_file\exercise\8235350165.htm'
# def get_img_url(url):
    # global header
    # request=urllib.request.Request(url,headers=header)
    # reference=urllib.request.urlopen(request)
with open(url,'rb')as f:
    page = f.read()
    # 您可以将decode字节转换为字符串：
    page = page.decode('utf-8')
    # regex = re.compile(r'<img.*?class="BDE_Image" src="(.*?)".*?>')
    regex = re.compile(r'<img class="BDE_Image" src="(.*?)".*?>')
    img_url_list = re.findall(regex, page)
    print(img_url_list)


a='aaa'
b='bbb'
print('%s%s'%(a,b))
