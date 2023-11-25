#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 第 0013 题： 用 Python 写一个爬图片的程序
# https://blog.csdn.net/wy9xqd58/article/details/115732503
# https://blog.csdn.net/z2431435/article/details/
# https://blog.csdn.net/wds2006sdo/article/details/52730863
# https://www.cnblogs.com/onefine/p/10499342.html
# https://www.cnblogs.com/liyang93/p/6669874.html
# https://stackoverflow.com/questions/31019854/typeerror-cant-use-a-string-pattern-on-a-bytes-like-object-in-re-findall
import re
import urllib
import urllib.request

# 头信息
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}

def get_img_url(url):
    global header
    request=urllib.request.Request(url,headers=header)
    reference=urllib.request.urlopen(request)
    page = reference.read()
    # 您可以将decode字节转换为字符串：
    page = page.decode('utf-8')
    # print(page)
    # regex = re.compile(r'<img.*?class="BDE_Image" src="(.*?)".*?>')
    # 直接下载的html文件和请求得到的page的内容不一样；建议从浏览器检查源码来查看
    # (.*?): 这是一个捕获组，它用括号括起来的部分会被提取出来。在这里，它会捕获图片链接，因为.*? 匹配了链接的内容。
    regex = re.compile(r'<img class="BDE_Image".*?src="(.*?)".*?>')
    img_url_list = re.findall(regex, page)
    # print(img_url_list)
    return img_url_list
def download_img(url_list,img_path):
    for img_url in url_list:
        urllib.request.urlretrieve(img_url,r'%s/%s.jpg' %(img_path,img_url[-8:-5]))
    print('done')
# todo


if __name__ =='__main__':
    url = r'https://tieba.baidu.com/p/8663000503'
    # https://tieba.baidu.com/p/8235350165
    path = r'./tieba0013_img'
    urllist = get_img_url(url)
    download_img(urllist,path)