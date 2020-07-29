#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import os
import requests
import re
import time
import  urllib.request
session=requests.session()
header_info={"Accept": "application/json,text/plain, */*",
             "Accept-Encoding":"gzip, deflate",
             "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
             "Content-Type":"application/json;charset=UTF-8",
             "Referer":"http://192.168.101.2:6069",
             "Connection":"keep-alive",
             "Host": "192.168.101.2:6069",
             "authorization":"",
             "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
url="http://192.168.101.2:6069/api/unauthor/sys/menu?id=0&terminal=0"
res= session.get(url,headers=header_info)
# print(res.content.decode('utf-8'))

regexp='"img":"(.+?)",'
result=re.findall(regexp,res.content.decode('utf-8'))
print(result)

count=0
for img in  result:
    count +=1
    result_out=img
    # print(count,":",img)
    os.chdir("C://Users\Administrator\Desktop\opencagent")
    # if os._exists('1.txt'):
    #     os.write(2,result_out)
    f=open('test.txt','a')
    f.write(str(result_out))
    f.write('\n')
    # print(result)

# a=1
# while a:
#     session.get(url,headers=header_info)
#     print(res.content.decode('utf-8'))
#     print('======================================================================='
#           '======================================================================='
#           '=======================================================================')

# os.mkdir('./images')
# imgae_url=result
# def request_download():
#     for i in result:
#     r=requests.get(i)
#     with open('./images','wb') as f:
#         f.write(r.content)