#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:  生产者与消费者模式

import threading
import queue
import time


def produce():
    for i in range(10):
        time.sleep(0.5)
        print('生产++++++面包{} {}'.format(threading.current_thread().name,i))
        q.put('{}{}'.format(threading.current_thread().name,i))  #生产的面包放入队列


def consumer():
    while True:
        time.sleep(1)
        print("{}买到------面包{}".format(threading.current_thread().name,q.get()))  #q.get() 方法是一个sort方法

q=queue.Queue()  #创建一个q (队列)

#一条生产线
pa=threading.Thread(target=produce,name='pa')
pb=threading.Thread(target=produce,name='pb')
pc=threading.Thread(target=produce,name='pc')
#一条消费线
ca= threading.Thread(target=consumer,name='ca')
cb= threading.Thread(target=consumer,name='cb')
cc= threading.Thread(target=consumer,name='cc')

pa.start()
pb.start()
pc.start()

ca.start()
cb.start()
cc.start()