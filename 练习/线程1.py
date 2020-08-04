#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
# import threading
# from  time import sleep
#
# money = 1000
#
# def run1():
#     global money
#     for i in range(100):
#         money -=1
#         sleep(1)
#         print('线程{}正在运行'.format('线程1'))
#
# def run2():
#     global money
#     for i in range(100):
#         money -=1
#         sleep(1)
#         print('线程{}正在运行'.format('线程2'))
#
# if __name__ == '__main__':
#     th1= threading.Thread(target=run1,name='th1')
#     th2 = threading.Thread(target=run2,name='th2')
#     th1.start()
#     th2.start()
#
#     th1.join()
#     th2.join()
#     print(money)
'''
1、线程是可以共享全局变量的
2、 GIL 全局解释器锁
3、线程同步(加锁)的缺点，速度上不如不加锁，但是可以保证数据安全，python底层只要用线程就会默认加锁(全局解释器锁)，耗时、爬虫、IO操作用线程、计算密集型用进程
'''
import  threading
from time import sleep

n=0
local = threading.Lock()

def task1():
    local.acquire(timeout=5)
    global n
    for i in range(2000000):
        sleep(0.1)
        # print('========>task1中的n的值是: ', n)
        n +=1
    local.release()
    print('========>task1中的n的值是: ',n)


def task2():
    local.acquire(timeout=5)
    global n
    for i in range(2000000):
        sleep(0.1)
        # print('========>task2中的n的值是: ', n)
        n +=1
    local.release()
    print('========>task2中的n的值是: ',n)


if __name__ == '__main__':
    th1 =threading.Thread(target=task1)
    th2 = threading.Thread(target=task2)

    th1.start()
    th2.start()



    print('最后打印n：',n)

