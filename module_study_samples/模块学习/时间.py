#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
'''
一、在python中，由三种方式来标识时间，分别是时间戳、格式化时间字符串、结构化时间
1、时间戳(timestamp)：也就是1970.1.1日后的秒，可以通过time.time() 获得，时间戳是一个浮点型，可以进行加减运算，但不要让结果超出取值范围
2、格式化的时间字符串(strin_time)：是年月日时分秒我们常见的时间字符串，可以通过 time.strftime('%Y:%m:%d') 获得
3、结构化时间(struct_time)： 报了年月日是分娩的多元元组，可以通过 time.localtime() 获得
'''

'''二、结构化时间
使用 time.localtime() 可以获得一个结构化时间元祖
索引
'''
import time
# print(time.ctime())
# print(time.asctime(time.localtime()))

def process():
    time.sleep(3)

time1=time.clock()
process()
print(time.clock() - time1,'测试')