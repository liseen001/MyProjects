#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
'''
一、使用threading 模块实现新线程的的必须操作
1、定义thread类的新子类；2、覆盖 __init__(self [,args]) 方法添加其他参数
3、重写 run(self [,agrs]) 方法来实现新城在启动时应该执行的操作
4、当创建新的thread的子类后，就可以创建一个实例，然后调用start() 方法来调用 run() 方法来启动一个新的线程
'''
import  threading
# from  threading import Thread

class MyThread(threading.Thread):
    def __init__(self,thread_name):
        super(MyThread,self).__init__(name=thread_name)

    def run(self):
        print('%s正在运行中..........'% self.name)


if __name__=="__main__":
    for i in range(10):
        MyThread('thread-'+str(i)).start()

