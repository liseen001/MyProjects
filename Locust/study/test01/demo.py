#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
from locust import HttpLocust,TaskSet,task

class BlogDemo(TaskSet):
    '''用户行为：打开我的博客首页demo'''
    @task(5)
    def open_blog(self):
        # 定义requests的请求头
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}

        r = self.client.get("/yoyoketang",  headers=header, verify=False)
        print(r.status_code)
        assert r.status_code == 200

class websitUser(HttpLocust):
    task_set = BlogDemo
    min_wait = 3000  # 单位毫秒
    max_wait = 6000  # 单位毫秒

if __name__ == "__main__":
    import os
    os.system("locust -f demo.py --host=https://www.cnblogs.com")