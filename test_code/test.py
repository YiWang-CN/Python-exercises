#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
print("hello, world!")
if True:
    print('ok')
    print('yes')
x = 3
y = 4
print(x + y)

print('Hello world!')
print('hello' + 'world!')
print('hello', 'world!')
print('hello', 'world!', sep='!!!')
print('#' * 50)
print('how are you?', end='')
print()
print('#' * 50)

print(5/2)
print(5//2)
print(5 % 2)
print(5**2)
print(5 > 2)
print(2 > 5)
print(20 > 10 >5)
print(20 > 10 and 10 > 5)
print(not 20 > 10)
print('#'*50)

number = input("请输入数字：")
print(number)
print(type(number))

# print(number + 10)   # 报错，不能把字符和数字做运算
print(int(number) + 10)
print(number + str(10))
print('#' * 50)

username = input('username: ')
print('welcome', username)
print('welcome' + username)
print('#'* 50)

sentence = 'tom\'s pet is a cat'
sentence2 = "tom's pet is a cat"
sentence3 = "tom said: \"hello world!\""
sentence4 = 'tom said:"hello world"'
words ="""
hello
world
abcd
"""
print(words)
print('#'* 50)

py_str = 'python'
len(py_str)
py_str[0]
'python'[0]
py_str[-1]
# py_str[6]  # 错误，下标超出范围
py_str[2:4]
py_str[2:]
py_str[:2]
py_str[:]
py_str[::2]
py_str[1::2]
py_str[::-1]
py_str + 'is good'
py_str * 3
't' in py_str
'th' in py_str
'to' in py_str
'to' not in py_str
print('#'* 50)

alist = [10,20,30,'bob','alice',[1,2,3]]
len(alist)
alist[-1]
alist[-1][-1]
[1, 2, 3][-1]
alist[-2][2]
alist[3:5]
10 in alist
'o' in alist
100 not in alist
alist[-1] = 100
alist.append(200)
print('#' * 50)

atuple = (10,20,30,'bob','alice',[1,2,3])
len(atuple)
10 in atuple
atuple[2]
atuple[3:5]
# atuple[-1] = 100 #错误，元组不可变
print('#' * 50)

adict = {'name': 'bob', 'age': 23}
len(adict)
'bob' in adict
'name' in adict
adict['email'] = 'bob@tedu.cn'
adict['age'] = 25
print('#' * 50)

if 3 > 0:
    print('yes')
if 10 in [10, 20, 30]:
    print('ok')
if -0.0:
    print('ok')
if [1,2]:
    print('yes')
if ' ':
    print('yes')

a= 10
b= 20
if a < b:
    smaller = a
else:
    smaller = b
print(smaller)
s = a if a<b else b
print(s)
print('#'* 50)

import getpass
username = input('username:')
password = getpass.getpass('password:')
if username == 'bob'and password == '123456':
    print('Login successful')
else:
    print('Login incorrect')
print('#'* 50)

sum100 = 0
count = 1
while count < 101:
    sum100 += count
    count += 1
print(sum100)

while True:
    yn = input('Countinue(y/n):')
    if yn in ['n','N']:
        break
    print('running...')

sum100 = 0
counter = 0
while counter < 100:
    counter += 1
    if counter % 2:
        continue
    sum100 += counter
print(sum100)
print('#'* 50)

astr = 'hello'
alist = [10,20,30]
atuple = ('bob','tom','alice')
adict = {'name':'john','age':23}
for ch in astr:
    print(ch)
for i in alist:
    print(i)
for name in atuple:
    print(name)
for key in adict:
    print('%s: %s'%(key, adict[key]))
print('#'* 50)

range(10)
list(range(10))
range(6,11)
range(1,10,2)
range(10,0,-1)
sum100 = 0
for i in range(1,101):
    sum100 += i
print(sum100)

fib = [0,1]
for i in range(8):
    fib.append(fib[-1] + fib[-2])
print(fib)
print('#'* 50)

[10+5]
[10+5 for i in range(10)]
[10 + i for i in range(10)]
[10 + i for i in range(1, 11)]
[10 + i for i in range(1, 11) if i % 2 == 1]
[10 + i for i in range(1, 11) if i % 2]
print(['192.168.1.%s' % i for i in range(1, 255)])
print('#'* 50)

f = open(r'E:\BaiduDownload\151682\Hacknet\Hacknet\Content\BashLogs_StudentSafe.txt', 'r', encoding="utf-8")
data = f.read()
print(data)
data = f.read() # 随着读写的进行，文件指针向后移动。
# 因为第一个f.read()已经把文件指针移动到结尾了，所以再读就没有数据了
# 所以data是空字符串
f.close()

f = open(r'E:\BaiduDownload\151682\Hacknet\Hacknet\Content\BashLogs_StudentSafe.txt')
for line in f:
    print(line, end='')
f.close()

f = open(r'F:\Users\WY\Pictures\壁纸\1.jpg','rb') # 打开非文本文件要加参数b
f.read(4096)
f.close()

f = open(r'F:\Users\WY\Desktop\1.txt','w') # 'w'打开文件，如果文件不存在则创建
f.write('hello world!\n')
f.flush() # 立即将缓存中的数据同步到磁盘
f.writelines(['2nd lin.\n', 'new line.\n'])
f.close() # 关闭文件的时候，数据保存到磁盘

with open(r'F:\Users\WY\Desktop\1.txt') as f:
    print(f.readline())

f = open(r'F:\Users\WY\Desktop\1.txt')
f.tell() # 查看文件指针的位置
f.readline()
f.tell()
f.seek(0,0)   # 第一个数字是偏移量，第2位是数字是相对位置。
              # 相对位置0表示开头，1表示当前，2表示结尾
f.tell()
f.close()

src_fname = r'F:\Users\WY\Pictures\壁纸\1.jpg'
dst_fname = r'F:\Users\WY\Pictures\壁纸\dst_name.jpg'
src_fobj = open(src_fname, 'rb')
dst_fobj = open(dst_fname, 'wb')
while True:
    data = src_fobj.read(4096)
    if not data:
        break
    dst_fobj.write(data)
src_fobj.close()
dst_fobj.close()
print('#'* 50)

import sys
print(sys.argv)  # sys.argv是sys模块里的argv列表

# 在test.py中调用star模块：
import star
print(star.hi)
star.pstar()
star.pstar(30)
print('#'* 50)

py_str = 'hello wrld!'
py_str.capitalize()
py_str.title()
py_str.center(50)
py_str.center(50,'*')
py_str.ljust(50,'*')
py_str.rjust(50,'*')
py_str.count('1')
py_str.count('lo')
py_str.endswith('!')
py_str.startswith('h')
py_str.islower()
py_str.isupper()
'hao123'.isdigit()
'hao123'.isalnum()
print('   hello\t     '.strip())
print('   \thello\t     '.lstrip())
print('   \thello\t     '.rstrip())
'how are you?'.split()
'hello.tar.gz'.split('.')
'.'.join(['hello','tar','gz'])
'-'.join(['hello','tar','gz'])
print('#' * 50)

print("%s is %s years old" % ('bob', 23))
print("%s is %d years old" % ('bob', 23))
print("%s is %d years old" % ('bob', 23.5))
print("%s is %f years old" % ('bob', 23.5))
print("%s is %5.2f years old" % ('bob', 23.5))   # %5.2f是宽度为5，2位小数
print("97 is %c" % 97)
print("11 is %#o" % 11)  # %#o表示有前缀的8进制
print("11 is %#x" % 11)
print("%10s%5s" % ('name', 'age'))  # %10s表示总宽度为10，右对齐, 常用
print("%10s%5s" % ('bob', 25))
print("%10s%5s" % ('alice', 23))
print("%-10s%-5s" % ('name', 'age')) # %-10s表示左对齐, 常用
print("%-10s%-5s" % ('bob', 25))
print("%10d" % 123)
print("%010d" % 123)

"{} is {} years old".format('bob', 25)
print("{1} is {0} years old".format(25,'bob'))
print("{:<10}{:<8}".format('name','age')) #基本语法是通过{}和：来代替以前的%
print('#' * 50)

alist = [1, 2, 3, 'bob', 'alice']
alist[0] = 10
alist[1:3] = [20, 30]
print(alist)
alist[2] = [22, 24, 26, 28] #直接一个替换为列表
print(alist)
alist[2:2] = [22, 24, 26, 28] #替换  作为迭代对象逐个放入
print(alist)
alist.append(100)
alist.remove(24)
alist.index('bob')
blist = alist.copy()
blist[0] = 0
alist.insert(1, 15)
alist.pop()
alist.pop(2)
alist.pop(alist.index('bob'))
alist.pop(alist.index('alice'))
alist.pop(alist.index([22, 24, 26, 28]))
print(alist)
alist.sort()
alist.reverse()
alist.count(20)
print(alist)
print('blist:', blist)
alist.clear()
alist.append('new')
alist.extend('new') #作为迭代对象加入
alist.extend(['hello', 'world', 'here'])
print(alist)
print('#' * 50)

adict = dict()
cdict = {}
ddict = {}
print(dict(['ad', 'cd']))
bdict = dict([('name', 'bob'), ('age', 25)])
# fromkeys 该方法创建字典需要手动保存  Python 字典 fromkeys() 函数用于创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值。
ddict = cdict.fromkeys(['zhangsan', 'lisi', 'wangwu'],[11, 12, 13])
print(cdict)
print(ddict)
for key in bdict:
    print('%s:%s' % (key, bdict[key]))
print("%(name)s: %(age)s" % bdict)
bdict['name'] = 'tom'
bdict['email'] = 'tom@tedu.cn'
del bdict['email']
bdict.pop('age')
bdict.clear()
adict  = dict([('name', 'bob'),('age', '25')])
len(adict)
hash(10) # ？？？判断给定的数据是不是不可变的，不可变数据才能作为key
print(adict.keys())
print(adict.values())
print(adict.items())
# get方法常用，重要
adict.get('name')
print(adict.get('qq'))    # None
print(adict.get('qq', 'not found'))# 没有qq，返回指定内容
print(adict.get('age', 'not found'))
adict.update({'phone': '123456789'})
print('#' * 50)

myset = set('hello')
len(myset)
for ch in myset:
    print(ch)
aset = set('abc')
bset = set('cde')
print(aset & bset)
print(aset.intersection(bset))
print(aset | bset)
print(aset.union(bset))
print(aset - bset)
print(aset.difference(bset))
aset.add('new')
aset.update(['aaa', 'bbb'])
aset.remove('bbb')
cset = set('abcde')
dset = set('bcd')
cset.issuperset(dset) # cset是dset的超集么？
cset.issubset(dset) # cset是dset的子集么？

