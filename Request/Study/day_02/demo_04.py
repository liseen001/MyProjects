#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
from locust import HttpLocust,TaskSet,task

class BlogDemo(TaskSet):
    '''用户行为：打开网站首页'''
    @task(1)
    def open_blog(self):
        #定义requests的请求头
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
        r =self.client.get('/yoyoketang',headers=header,verify=False)
        print(r.status_code)
        assert  r.status_code == 200

class WebsiteUser(HttpLocust):
    task_set =BlogDemo
    main_wait = 3000
    max_wait = 6000


if __name__=="__main__":
    import os
    os.system('locust -f demo_04.py --host=https://www.cnblogs.com')