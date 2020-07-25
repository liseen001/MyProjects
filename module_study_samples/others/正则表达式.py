#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
# import _thread
# import time
#
# #为线程定义一个函数
# def print_time(threadName,delay):
#     count =0
#     while count<5:
#         time.sleep(delay)
#         count +=1
#         print("%s：%s" % (threadName,time.ctime(time.time())))
#
# #创建两个进程
# try:
#     _thread.start_new_thread(print_time,('Thread-1',2))
#     _thread.start_new_thread(print_time,('Thread-2',4))
# except:
#     print("Error:无法启动线程")
#
# while 1:
#     pass
from faker import Faker
f=Faker(locale='zh_CN')
# for i in range(5):
#     print(f.name()+":"+f.address()+":"+f.city_suffix()+"===="+f.ssn())
count=0
for i in range(101):
    if i<=101:
       count =i+1
       print("第%s号病人%s"%(str(count),f.name())+"身份照为%s"%f.ssn())

