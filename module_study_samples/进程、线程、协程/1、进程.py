#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
'''
一、进程
1、进程(pocess) 时正在运行的程序的实例，但一个程序可能会产生多个进程，丽日打开Chrome浏览器程序，他可能会产生多个进程，主程序需要一个进程，一个网页标签需要一个进程，一个插件也需要一个进程等等
2、每个进程都有自己的地址空间，内存、数据栈以及其他记录其运行状态的辅助数据，不同的进程只能使用消息队列，共享内存等进程间通讯(IPC)方法进行通信，而不能直接共享信息
3、虽然子进程复制了父进程的代码和数据段等，但是一旦子进程开始运行，子进程和父进程就是相互独立的，它们之间不再共享任何数据
'''
# import os
# pid =os.fork()
#
# if pid<0:
#     print('Fail to create process')
# elif pid==0:
#     print('I am child process (%s) and my parent is (%s).'%(os.getpid(),os.getpid()))
# else:
#     print('I (%s) just created a child process (%s).'%(os.getpid(),pid))

'''
二、多进程
python提供了 multiprocessing 模块，可以用来跨平台编写多进程程序，但是需要注意的是multiprocessing 在 windows和Linux平台的不一致性：windows和Linux下运行的结果可能不通，
因为 windosw的进程模型和Linux不一样，windows 下没有fork
'''

#子进程要执行的代码
'''
三、
下面代码中，我们从multiprocessing模块中引用了Process,Process是一个用于创建进程对象的类，其中，target指定了进行要执行的函数，args指定了参数，
在创建了进程实例P之后，调用了start方法开始执行该子进程，接着调用join方法，该方法用于阻塞子进程以外的所有进程(这里指父进程)，当子进程执行完毕后，父进程
才会继续执行，它通常用于进程间的同步
'''
# import  os
# from  multiprocessing import Process
#
# def child_proc(name):
#     print('Run child process %s (%s)...'%(name,os.getpid()))
#
# if __name__=="__main__":
#     print('Parent process %s.'%os.getpid())
#     p=Process(target=child_proc,args=('test',))
#     print('Process will start')
#     p.start()
#     p.join()
#     print('Process end')
#
'''
四、multiprocessing 与平台有关
'''

# import random
# import os
# from  multiprocessing import Process
#
# num = random.randint(0,100)
#
# def show_num():
#     print("pid:{},num is {}".format(os.getpid(),num))
#
# if __name__=="__main__":
#     print("pid:{},num is {}".format(os.getpid(),num))
#     p=Process(target=show_num)
#     p.start()
#     p.join()


'''
五、使用进程池创建多个进程

'''
import os,time
from multiprocessing import Pool
def foo(x):
    print('Run task %s(pid:%s)...'%(x,os.getpid()))
    time.sleep(2)
    print('Task %s result is:%s'%(x,x*x))

if __name__=="__main__":
    print('Parent process %s.'%os.getpid())
    p=Pool(10)
    for i in range(11):
        p.apply_async(foo,args=(i,))
    print('Waiting for all Subprocresses done...')
    p.close()
    p.join()
    print('All subprocesses done.')