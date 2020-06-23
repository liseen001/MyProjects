#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import random
from locust import task,HttpUser,between,SequentialTaskSet,tag
class WebSsiteTasks(SequentialTaskSet):
    def on_start(self):
        self.client.post("/login", {
            "username": "test",
            "password": "123456"
        })

    @task(2)
    def index(self):
        self.client.get('./')

    @task(1)
    def about(self):
        self.client.get('/about/')

class WebsiteUser(HttpUser):
    tasks = [WebSsiteTasks]
    wait_time = [1,5]
    host = "https://debugtalk.com"