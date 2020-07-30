#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import requests,random,string
from  admin.common.config_utils import conf
from admin.common.log_utils import logger

api_url='http://192.168.101.5:9192/admin/login'
json_data={"loginName":conf.loginName,"password":conf.password}
headinfos={"Accept":"application/json, text/plain, */*",
           "Accept-Encoding":"gzip, deflate",
           "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
           "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
           "Content-Type":"application/json;charset=UTF-8",
           "Connection":"keep-alive",
           "Host":"192.168.101.5:9192"
           }
res=requests.post(url=api_url,json=json_data,headers=headinfos)
# print(res.json())

a="A3+2kGGh67OPkWoRrECUfF9JNUol27eY0JgXlnwUxogRVLHy56/uJpmuAu1vsReR42pEEEOumG6RbkZ2wA852IDe4KI1L35JGZjTh/dIDFB6shPNO03RlqJNIDFWcrjlLeQangLhgwtnZiTPwnRClNZsXF9RWug+APlvs5usIpUyWWQiC3vazn7zQsy/eyjeB97o9Hgp6lEgbOds29eacAylvzLiVD3Tn+8ALLahTe+6H1XbnkWdYv7klFFBqCMHuVHcVE0LLn33VPW3Jb1H2sTj1vkwOzHXKWuBctEME26lKRGHCogO9Q8YPEWewquY+B7C+RetwciHqBDIjlutMJhMFucPTHl83wl1HD9n6s10kcYwbW6mgw5dg5qDC3naOzNfofdQLi3K06JyarPhG6ZVo26f4S/iA70aUoZ3dkK+laPIarQNDKGu8GYvWAyENTjMf+STBA6LjOluhFSGY3P61pM7fm31q5cKZlTdE7CFQA8tKsn54YhyxyRSOljm"
b='123'
print(type(a))
print(b)
print(a)
print(a[0])
