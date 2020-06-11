#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:新后台接口
import requests
import json
import jsonpath
import os
response = requests.get('http://www.hnxmit.com')
print(response.content.decode('utf-8'))