#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import requests,json

# get_param_data = {'wd':'湖南软测'}
# headerinfo ={'Connection': 'keep-alive','Content-Type': 'text/html;charset=utf-8',
#              'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
#              'Accept-Encoding':'gzip, deflate, br'}
# res = requests.get(url='https://www.baidu.com/s',params=get_param_data,headers=headerinfo)
# print(res.content.decode('utf-8'))

str1 ='{"name":"test","age":22}'

print(type(str1))
print(json.loads(str1))