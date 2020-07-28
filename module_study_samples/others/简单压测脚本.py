#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc: 简单压测脚本
'''常用的网站性能测试指标有：并发数、响应时间、吞吐量、性能计数器等。
1、并发数
并发数是指系统同时能处理的请求数量，这个也是反应了系统的负载能力。
2、响应时间
响应时间是一个系统最重要的指标之一，它的数值大小直接反应了系统的快慢。响应时间是指执行一个请求从开始到最后收到响应数据所花费的总体时间。
3、吞吐量
吞吐量是指单位时间内系统能处理的请求数量，体现系统处理请求的能力，这是目前最常用的性能测试指标。
QPS（每秒查询数）、TPS（每秒事务数）是吞吐量的常用量化指标，另外还有HPS（每秒HTTP请求数）。
跟吞吐量有关的几个重要是：并发数、响应时间。
QPS（TPS），并发数、响应时间它们三者之间的关系是：
QPS（TPS）= 并发数/平均响应时间
4、性能计数器
性能计数器是描述服务器或操作系统性能的一些数据指标，如使用内存数、进程时间，在性能测试中发挥着"监控和分析"的作用，尤其是在分析统统可扩展性、进行新能瓶颈定位时有着非常关键的作用。
Linux中可以使用top或者uptime命令看到当前系统的负载及资源利用率情况。
资源利用率：指系统各种资源的使用情况，如cpu占用率为68%，内存占用率为55%，一般使用"资源实际使用/总的资源可用量"形成资源利用率。
'''
# url="http://192.168.101.2:6069/api/unauthor/sys/menu?id=0&terminal=0"
import requests,time,json,threading,random
class Presstest(object):
    headers={"Accept": "application/json,text/plain, */*",
             "Accept-Encoding":"gzip, deflate",
             "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
             "Content-Type":"application/json;charset=UTF-8",
             "Referer":"http://192.168.101.2:6069",
             "Connection":"keep-alive",
             "Host": "192.168.101.2:6069",
             "authorization":"",
             "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}

    def __init__(self,login_url,press_url,phone='1376193000',password='123456'):
        self.login_url=login_url
        self.press_url=press_url
        self.phone=phone
        self.password=password
        self.session=requests.session()
        self.session.headers=self.headers

    def login(self):
        '''获取登录session'''
        


