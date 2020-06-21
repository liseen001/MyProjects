#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: test001.py
# @time: 2020/6/21 12:30
# @desc:
from locust import TaskSet,HttpLocust,task,HttpUser
class Zentao_login(TaskSet):

    @task(1)
    def open_index(self):
        url = '/zentao/cron-ajaxExec-0.html'
        headers= {"Connection":"Keep-Alive","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"}
        self.client.get(url,headers=headers,name="打开首页")

    @task(1)
    def login(self):
        pass

class Zentao_User(HttpUser):
    task_set = Zentao_login
    min_wait = 1000
    max_wait = 3000



if __name__ =="__main__":
    import  os
    os.system('locust -f test001.py --host=http://127.0.0.1')