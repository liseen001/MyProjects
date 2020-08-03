#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:  迭代器与生成器
list=[1,2,3,4]
it = iter(list)
print(next(it))
for i in it:
    print(next(it))
