#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import threading
import time


# class MyThread(threading.Thread):
#     def __init__(self,thread_name):
#         super(MyThread,self).__init__(name=thread_name)
#
#
#     def run(self):
#         print('%s正在运行中.........'%self.name)
#
#
#
# if __name__=="__main__":
#     for i in range(10):
#         MyThread("thread"+str(i)).start()


# def show(arg):
#     time.sleep(1)
#     print('thread'+str(arg)+"running....\n")
#
#
# if __name__=="__main__":
#     for i in range(10):
#         t = threading.Thread(target=show,args=(i,))
#         t.start()

# def doWaiting():
#     print('start waiting:',time.strftime('%H:%M:%S'))
#     time.sleep(3)
#     print('stop waiting',time.strftime('%H:%M:%S'))
#
#
# t =threading.Thread(target=doWaiting)
# t.start()
# time.sleep(1)
# print('start job')
# t.join()
# print('end job')

# def run():
#     print(threading.current_thread().getName(),'开始工作')
#     time.sleep(2)
#     print('子线程工作完毕')
#
# for i in range(3):
#     t=threading.Thread(target=run,)
#     t.setDaemon(True)
#     t.start()
#
# time.sleep(1)
# print('主线程结束了')
# print(threading.active_count())

class MyThreading(threading.Thread):

    def __init__(self,func,arg):
        super(MyThreading,self).__init__()
        self.func = func
        self.arg = arg

    def run(self):
        self.func(self.arg)

def my_func(args):
    pass