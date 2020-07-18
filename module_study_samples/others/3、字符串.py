#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:  字符串

# str1 = 'abcdefghijkoasdaHAVC'
# print(str1[2:])
# print('Ki' not in str1)
#
# str2 = R'aaal\000'
# print(str2)
#
# print('%s'%('曹尼玛'))
# print( '我叫%u,今年%d岁'%(2342342,18) )

# name = 'liseen'
# print(f'hellp {name}')
# print(type({1+2}))
#
# print(f'w{"name"}:w{"liseen"}')
#
# str3 = 'liseen'
# str4 = 'Ayang'
# print(str3.capitalize())
# print(str4.lower())
#
# print(str3.center(3))
# print(str3.count('e'))

str1 ='aaAsSSSss'
print(str1.capitalize())
print(str1.lower())
print(str1.islower())
str1 = '&'
print(str1.casefold())
str1 = 'liseen'
print(str1.center(20,'&'))

print(str1.count('e',0,len(str1)))
print(str1.encode(encoding='utf-8',errors='strict'))

str1= 'aaa\tbbb'
print(str1)
print(str1.expandtabs(8))

