#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import requests
import threading
import time
from urllib import request,parse
class PostRequests():
    def __init__(self):
        self.url='http://192.168.101.2:6069/api/unauthor/sys/menu?id=0&terminal=0'
        self.headinfos={"Accept": "application/json,text/plain, */*",
             "Accept-Encoding":"gzip, deflate",
             "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
             "Content-Type":"application/json;charset=UTF-8",
             "Referer":"http://192.168.101.2:6069",
             "Connection":"keep-alive",
             "Host": "192.168.101.2:6069",
             "authorization":"",
             "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
        self.params={}

    def post(self):
        try:
            a=1
            for i in range(1000000):
                a+=i
            r=requests.get(self.url,headers=self.headinfos)
            print(r.url+str(a))
            # a=0
            # for i in range(int):
            #     a +=1
            #     print('执行的请求次数为第{}次'.format(a))
        except Exception as e:
            print(e)


if __name__=="__main__":
    try:
        i=0
        tasks_number=150
        print('启动测试')
        time1=time.process_time()
        while i<tasks_number:
            t=threading.Thread(target=PostRequests().post())
            t.start()
            i+=1
        time2=time.process_time()
        times=time2-time1
        print(times/tasks_number)
    except Exception as e:
        print(e)