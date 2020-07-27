#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:  元组 是一种不可变的序列，用圆括号表示

#1、创建空元组，创建只有一个一个值的元祖
a=()
b=(1,)
print(type(a))
print(b)
c=(1,2,3,4,5,6,7,8)
print(c.index(2))

#2、元祖也是一种序列，因此也可以对它进行索引、分片等，由于它是不可变的，因此就没有类似于列表的append\extend\sort等方法
