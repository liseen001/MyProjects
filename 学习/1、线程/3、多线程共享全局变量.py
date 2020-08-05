#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import threading
import time

# 多个线程可以同时操作一个全局变量（多个线程共享全局变量）

# 线程安全问题：解决方案：加锁====>衍生的问题：  运行速度变慢 GIL（不可变）===>调整锁的作用域
# 线程并不是越多越好

ticket =20
lock=threading.Lock()  #创建一把锁

def sell_ticket():
    global ticket
    while True:
        lock.acquire()  #获得锁
        if ticket >0:
            time.sleep(1)
            ticket -=1
            lock.release()  #释放锁
            print( '{}卖出一张票，还剩下{}张'.format(threading.current_thread().name,ticket) )
        else:
            lock.release()
            print('票卖完了')
            break


t1 = threading.Thread(target=sell_ticket,name='线程1')
t2 = threading.Thread(target=sell_ticket,name='线程2')

t1.start()
t2.start()