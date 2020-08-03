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

# str1 ='aaAsSSSss'
# print(str1.capitalize())
# print(str1.lower())
# print(str1.islower())
# str1 = '&'
# print(str1.casefold())
# str1 = 'liseen'
# print(str1.center(20,'&'))
#
# print(str1.count('e',0,len(str1)))
# print(str1.encode(encoding='utf-8',errors='strict'))
#
# str1= 'aaa\tbbb'
# print(str1)
# print(str1.expandtabs(8))

#1、字符串是一种序列，因此，通用的序列操作如索引、分片、加法、乘法对它适用
# s='hello'
# print(s[0])
# print(s[1:3])
# print(s+"hello")
#
# #2、字符串和元祖一样都是不可变的，因此不能对它进行复制操作
#
# #3、find方法用于在一个字符串查找子串，它返回子串所在位置的最左端索引，如果没有找到则返回-1
# motto="to be or not to be,that is a question"
# a=motto.find('hehe')
# print(a)
#
# #4、split方法用于将字符串分割成序列
# a='/user/bin/ssh'
# b=a.split('/')
# print(b)
# a='1+2+3+4+5+6'
# b=a.split("+")
# print(b)
#
# #5、join方法可以说是split的逆方法，它用于将序列中的元素连接起来,但是不能是数字
# a='/'.join(['','user','bin','ssh'])
# print(a)
# b='+'.join(['1','b','3','4','6'])
# print(b)
#
# #6、strip方法用于移除字符串左右两侧的空格，但不包括内部，当然也可以指定需要移除的字符串
# a=' hello,world  '
# print(a)
# print(a.strip())
# a='##@% hello,world  #@% '
# print(a.strip('#%@ '))  #移除左右两边的@或#或%或空格
#
# #7、replace方法用于替换字符串中的所有匹配项，前面被匹配的字符串，后面为替代的字符串
# motto="to be or not to be,that is a question"
# motto=motto.replace('to','TO')
# print(motto)
#
# #9、lower/upper  用于返回字符串的大写或小写形式
# x='PYTHON'
# print(x.lower())
# print(x.upper())
# y='python'
# print(y.upper())




import time

print('\033[1;31m')
print('登录信息'.center(46, "*"), "\033[0m")
print('\033[34m*HOST:\t', "192.168.1.10")
print('*PORT:\t', "80")
print('*User:\t', "jack")
print('*TIME:\t', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print('\033[1;31m*' * 50, '\033[0m')
print("\033[32m欢迎登录！\033[0m")