#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:python 自带的Mock模块使用
from  unittest import mock
import requests

def add(num1,num2):
    return  num1 + num2

add_value = mock.Mock(return_value=200)
add = add_value
print(add(30,30))


def send_request(url):
    r = requests.get(url=url)
    return r.status_code

def visit_newdream():
    return  send_request('http://www.hnxmxit.com/')

print(visit_newdream())