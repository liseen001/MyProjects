#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import threading
def worker():
    '''thread worker function'''
    print( 'worker' )

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()