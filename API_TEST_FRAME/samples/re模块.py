#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: re模块.py
# @time: 2020/8/5 22:30
# @desc:
import re

# str1 = 'newdream,com on!'
# pattern = re.compile( r"(\w+),(\w+)(\w+)(?P<sign>.*)" )
# result1 = re.match( pattern , str1 )
# print(result1.expand( r"\2 \3 \1 \4" ))

# str2 = "china1usa2german3english"
# pattern2 = re.compile(r"\d")
# result2=re.split(pattern2,str2)
# print(result2)
#
# result3 = re.finditer(pattern2,str2)
# for i in result3:
#     print(i.group())

str1 = "summer hot~~"
pattern = re.compile(r"(\w+) (\w+)")
# print(re.sub( pattern,r"\2 \1",str1 ))  #r"\2 \1"可以写成任意想要替换的值 如：r"hello"
# print(str1)

result=re.match(pattern,str1)
print(result.group(1).title())

def fun(m):
    return m.group(1).title() + '' + m.group(2).title()
str1 = re.sub(pattern,fun,str1)
print(str1)