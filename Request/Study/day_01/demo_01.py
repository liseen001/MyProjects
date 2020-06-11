#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx0591278088098c56&secret=ceaab7a476a85194f507c8a00c82ad1f
import requests
import json
import jsonpath
post_param_data = {"username":"liseen001","password":"a000000","terminal":0}
headinfos = {"Accept":"application/json, text/plain, */*","Accept-Encoding":"gzip, deflate",
             "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8","Connection":"keep-alive",
             "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
             "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
             "Referer":"http://192.168.101.2:6049"}
response = requests.post(url="http://192.168.101.2:6049/api/unauthor/gateway/account/login",params=post_param_data,headers=headinfos)
result = response.content.decode('utf-8')
print(result)

json_data=json.loads(result)
token = jsonpath.jsonpath(json_data,'$.data.token')
print(token)