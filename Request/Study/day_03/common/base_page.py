#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import requests
import json

url = 'http://www.taobao.com'
def send_get(url):
    response =requests.get(url)
    return  response
print(send_get(url).content.decode('utf-8'))

url='https://api.weixin.qq.com/cgi-bin/tags/create'
data ={"grant_type":'client_credential','appid':'wx0591278088098c56','secret':'ceaab7a476a85194f507c8a00c82ad1f'}

def send_post(url):
    response = requests.post(url)



