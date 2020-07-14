#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: re_demo.py
# @time: 2020/7/14 22:25
# @desc:  正表达式
import re
str1 ="neewdream,com on!"
pattern = re.compile(r"newdream")  # r原生字符串   创建一个字符模板
result=re.match(pattern,str1)
print(result)