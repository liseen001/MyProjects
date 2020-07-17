#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:基础数据类型

import keyword
print(keyword.kwlist)
print(keyword.__all__)

a=111
print(isinstance("a",str))
print(eval('123456'),type(eval('123456')))
print(chr(89))
print(ord('Y'))
print(hex(789))
print(repr('(.+?)'),type(repr('(.+?)')))

set1 ={1,23,4,5}
print(set1)
print(frozenset(set1))
print(set1)

