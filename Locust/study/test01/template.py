#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc: http://wap.lemfix.com/topics/44318
import random
from locust import HttpUser,task,between,SequentialTaskSet,tag
#定义个一任务类，这个类名称自己随便定义，类继承SequentialTaskSet 或 Taskset类，所以要从locust中引入SequentialTaskSet或TaskSet
#当类里面的任务请求有先后顺序是，继承类继承SequentialTaskSet类，没有先后顺序，可以使用继承TaskSet类
class MyTaskCase(SequentialTaskSet):
    #初始化方法，相当于setup
    def on_start(self):
        pass
    #@task python中的装饰器，告诉下面的方式一个任务，任务就可以是一个接口与请求，这个装饰器和下面的方法被复制多次，改动一下就能写出多个接口
    #装饰器后面带上(数字)代表在所以任务中，执行比例，要用这个装饰器，需要头部引入  从locust中引入task
    @task
    @task('leave_1')
    def regist_(self): #一个方法，方法名可以自己改
        url = '.erp.regist'  #接口请求的URL地址
        self.headers={"Content-Type": "application/json"} #定义请求头为类变量，这样其他任务也可以调用该变量
        self.username = 'locust_'+str(random.randint(10000,100000))
        self.pwd = '123456789'
        data = {"name":self.username,"pwd":self.pwd}  #post请求的请求体
        #使用 self.client发起请求，请求的方法根据接口实际选
        #catct_response值为True 允许为失败，name设置任务标签名称  ----可选参数
        with self.client.post(url,json=data,headers=self.headers,catch_response=True) as rsp:
            if rsp.status_code > 400:
                print(rsp.text)
                rsp.failure('regist_接口失败！')

    @task   #装饰器，说明下面是一个任务
    def login_(self):
        url = '/erp/loginIn'  #接口请求的URL地址
        data={'name':self.username,'pwd':self.pwd}
        with self.client.post(url,json=data,headers=self.headers,catch_response=True) as rsp:
            self.token =rsp.json()['token']  #提取响应json中的信息，定义为变量类
            if rsp.status_code < 400 and rsp.json()['code'] =='200':
                rsp.success()
            else:
                rsp.failure('login_接口失败')
    @task  #装饰器，说明下面是一个任务
    def getuser_(self):
        url = '/erp/user' #接口请求的URL地址
        headers ={'Token':self.token}  #引用上一个任务的类变量值，实现参数关联
        with self.client.get(url,headers=self.headers,catch_response=True) as rsp:  #使用self.client请求，请求的方法根据实际选择
            if rsp.status_code < 400:
                rsp.success()
            else:
                rsp.failure('getuser_接口测试失败！')
    #结束方法，相当于teardown
    def on_stop(self):
        pass

    #定义一个运行类，继承HttpUser类，所以要从locust中引用HttpUser类
class UserRun(HttpUser):
    tasks =  [MyTaskCase]
    wait_time = between(0.1,3)   #设置运行过程中间隔时间，需要从locust中引入 between

'''
运行：
    在终端中输入：locust -f 被执行的locust.py文件 --host=http://被测服务器名或ip端口地址，也可以不指定host
    命令执行成功，会提示服务端口，如：*:8089
    此时，则可以通过浏览器访问机器ip:8089
'''

