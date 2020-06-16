#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
from locust import HttpLocust,TaskSet,task,events
from gevent._semaphore import  Semaphore
import queue,pymysql,requests,threading

'''
创建集合点，当locust实例产生完成时触发
'''

all_locusts_spawned = Semaphore()
all_locusts_spawned.acquire()

#创建等待方法
def on_hatch_complete(**kwargs):
    all_locusts_spawned.release()
#当用户加载完时触发
events.hatch_complete += on_hatch_complete

#全局队列
q =queue.Queue(maxsize=10)

#token生产函数
def product():
    count =1
    db = pymysql.connect
