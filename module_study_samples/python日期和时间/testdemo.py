#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
'''
1、python提供了一个time和calender模块可以用于格式化日期和时间
2、时间间隔是以秒为单位的浮点小数
3、每个时间戳都以自从1970.1.1午夜经过了多长时间来表示
4、python的time模块下有很多可以转换常见日期格式，如函数time.time()用于获取当前时间戳
'''
import time
ticks=time.time()
print(ticks)

localtime=time.localtime(time.time())
print(localtime)

localtime=time.asctime(time.localtime(time.time()))
print(localtime)
