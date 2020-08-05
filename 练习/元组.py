#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
''''
元祖是序列结构，但是是一种不可变序列，可以简单的理解为内容不可变的列表，除了在内部元素不可修改的区别外，元祖和列表的用法差不多
1、使用方括号加下标访问元素
2、切片(形参新元祖对象)
3、count() /  index()
4、len() / max() /min() / tuple
元组中不允许的操作
1、修改、新增元素
2、删除某个元素（但可以删除整个元祖）
3、所有会对元组内部元素发生修改动作的方法，例如，元祖没有remove、append、pop等方法
'''

# dic={'name':'jack','age':7,'class':'first'}
# print(dic.setdefault('sex'))
# print(dic.items())
# print(dic.keys())
# print(dic.values())
# for  i in dic:
#     print(i,dic[i])
# for key,value in dic.items():
#     print(key,value)
# dic={'name':'jack','age':7,'class':'first'}
# print(len(dic))
# dic['address']="shanghai"
# dic["address"]='beijing'
# print(dic)
# del dic['address']
# print(dic)
# dic.pop('age')
# print(dic)
# dic={'name':'jack','age':7,'class':'first'}
# for key in dic:
#     print(key,dic[key])

# for key,value in dic.items():
#     print(key,value)
#
# for key in dic.keys():
#     print(key)
#
# for value in dic.values():
#     print(value)
#
# dic = {}
# for i in 'adilwste':
#     dic[i]=ord(i)
#     print(dic)