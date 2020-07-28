#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc: 读写文本文件
'''
一、读文件
1、在python中，读文件主要分为三个步骤：1、打开文件；2、读取内容；3、关闭文件
2、读取文件的集中方式：1、一次性读取完所有内容 read()或readlines() ；2、按字节读取 read(size)；3、按行读取 readline()
'''
try:
    f =open(r'../.\data\1.txt','r',encoding='utf-8')
    data=f.read()
    # print(data)
finally:     #代码中的try....finally是因为如果打开的和读取的文件出现错误时，文件就没有被关闭，为了确认任何情况下，文件都能被关闭
    if f:
        f.close()

with open(r'../.\data\1.txt','r',encoding='utf-8') as f:
    data1=f.readlines()  #可以with语句帮助我们自动调用close方法，不进简洁而且还能在出现异常的情况下自动关闭文件
    # print(data1)

'''
二、文件 open()  函数常用的模式
open函数的常用模式有：1、r:读模式；2、w：写模式；3、a：追加模式；4、b：二进制模式(可添加到其他模式中使用)；5、+：读/写模式，可以添加到其他模式中使用
'''

'''
三、文件迭代器
在python中，文件对象是可迭代的，这意味着我们可以直接在for循环中使用它们，而且是逐行迭代的，也就是说，效果和readline()是一样的
'''


'''四、写文件的方法
1、如果文件已经存在，则会情况原内容并且覆盖；2、如果路径是正确的但是文件不存在，则会新建一个文件，并写入指定内容；3、如果路径不正确，会抛出异常；4、往已存在的文件追加内容 +
'''
with open(r'../.\data\2.txt','a',encoding='utf-8') as file:
    file.write('我是你大爷a\n')
    file.write('我是你二大爷a\n')
    for i in range(10):
        file.write('嘿咻嘿咻\n')
    file.close()


'''五、总结
1、使用  with 语句操作文件 IO
2、如果文件较大，可以按字节读取或者按行读取
3、使用文件迭代器进行逐行迭代
'''