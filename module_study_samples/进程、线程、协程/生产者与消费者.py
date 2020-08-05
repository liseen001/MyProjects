#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
'''
生产者与消费者： 两个线程之间的通信
python的queue模块中提供了同步的、线程安全的队列类，包括FIFO(先入先出)队列queue.
LIFO（后入先出）队列LifoQueue，和优先级队列PriorityQueue，这些队列都实现了锁原理
(可以理解为原子操作，即要么不做，要么就做完)，能够在多线程中直接使用。
可以使用队列来实现线程间的同步
原理为两个线程之间的通信：queue
'''
import threading
import queue
import random
import time

def produce(q):
    i = 0
    while i <10:
        num = random.randint(1,100)
        q.put("生产者生成数据：%d" % num)
        print("生产者生产数据：%d" % num)
        time.sleep(1)
        i+=1
    q.put(None)
    q.task_done()  #完成任务

def consume(q):
    while True:
        item = q.get()
        if item is None:
            break
        print('消费者获取到：%s' % item)
        time.sleep(4)
    q.task_done()  #完成任务



if __name__ == '__main__':
    q=queue.Queue(10)
    arr = []

    #创建生产者
    th = threading.Thread(target=produce,args=(q,))
    th.start()

    #创建消费者
    tc = threading.Thread(target=consume,args=(q,))
    tc.start()

    th.join()
    tc.join()
    print('END')

'''
线程：Thread
1、创建线程
A、t=Thread(target=func,name='',args=(),kwargs=[])  新建状态
   t.start()   就绪状态，等待CPU分配资源
   
   run()  
   join()
B、自定义线程
class MyThread(Thread):
   def run(self):
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
'''