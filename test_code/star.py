#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 在test.py中调用star模块：
hi = 'hello world!'
def pstar(n=50):
    print('*' * n)

if __name__ == '__main__':
    pstar()
    pstar(30)