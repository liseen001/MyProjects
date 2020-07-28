#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import os
from  multiprocessing import  Process
from  time import sleep

m=1
def task1(s,name):
    global m
    while True:
        sleep(s)
        m+=1
        print('这是任务1.........',os.getpid(),'----------',os.getppid(),name,m)  #得到当前进程、父进程的编号

def task2(s,name):
    global m
    while True:
        sleep(s)
        m +=1
        print('这是任务2.........',os.getpid(),'----------',os.getppid(),name,m)


if __name__=="__main__":
    print(os.getpid())
    #子进程
    p=Process(target=task1,name='任务1',args=(1,'aa'))
    p.start()
    print(p.name)
    p1=Process(target=task2,name='任务2',args=(2,'bb')) #args传递元祖,可以传多个值
    p1.start()
    print(p1.name)
