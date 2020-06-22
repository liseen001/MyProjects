#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:  http://192.168.101.2:3018
from locust import HttpLocust,TaskSet,task,between,HttpUser

class Hta(TaskSet):
    @task(1)
    def open_xinmitmainpage(self):
        url = '/JJF/game/getPageTab?terminal=0&cagent=HTA'
        headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"}
        self.client.get(url=url,headers=headers,name="")


class WebsitUser(HttpUser):
    tasks = [Hta]
    wait_time = between(5,8)


if __name__=="__main__":
    import os
    os.system("locust -f demo.py --host=http://192.168.101.2:3018")