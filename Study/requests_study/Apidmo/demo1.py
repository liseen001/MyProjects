#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo1.py
# @time: 2020/6/6 0:04
# @desc:
import requests
response =requests.get('http://www.hnxmxit.com')
# print(response.content.decode('utf-8'))

response.encoding = 'utf-8'
print(response.text)