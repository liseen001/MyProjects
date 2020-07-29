#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import os
fo=open('../../data/1.txt','w',encoding='utf-8')
print(fo.name)                #返回文件名称
print(fo.closed)              #文件是否关闭，关闭返回True
print(fo.mode)                #返回文件的访问模式
print(fo.encoding)            #返回文件的编码格式

# close()  方法
'''
File对象的  close() 方法刷新缓冲区里任何还没有写入的信息，并关闭该文件，这之后变不能在进行写入，
当一个文件对象的引用被重新制定给另一个文件时，python会关闭之前的文件，用close()方法关闭文件是一个很好的习惯
'''
fo.close()
print(fo.closed)
print('===============================')


'''
一、write()方法
写方法可以将任何字符串写入一个打开的文件，需要重点注意的是，python字符串可以是以二进制数据，而不仅仅是文字
write() 方法不会再字符串的结尾添加换行符 ('\n');
如果打开的文件不存在则会新增一个文件
'''
# file = open('../../data/3.txt','a')
# # for i in range(11):
# #     file.write('python\npython\npython\n')
# # file.close()

'''
二、read() 方法从一个打开的文件中读取一个字符串，需要重点注意的是，python字符串可以是二进制数据，而不仅仅是文字
'''
# file = open('../../data/3.txt','r')
# # print(file.read())
#
# with open('../../data/3.txt','r') as f:
#     lista=f.readlines()
#     # print(len(lista))
#     # print(lista)
#     # print(f.readlines())
#     listb=[]
#     for i in range(len(lista)):
#         listb.append(lista[i])
#         print(listb)

'''
三、文件定位
tell() 方法告诉我们文件内的当前位置
seek(offser [,from])  方法改变当前文件的位置，offset 变量表示要移动的字节数，From变量值定开始移动字节的参考位置
如果from被设为0，意味着将文件的开头作为移动字节的参考位置，如果设为1，则使用当前的位置作为参考位置，如果设为2，那么文件的末尾作为参考位置
'''
# with open('../../data/3.txt','r') as file:
#     str = file.read(10)
#     print(str)
#     print(file.tell())
#
# with open('../../data/3.txt','r') as file:
#     position =file.seek(0,2)
#     print(position)
#     file.close()