#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: 异常处理.py
# @time: 2020/8/11 23:24
# @desc:
import requests
from requests.exceptions import RequestException

re = requests.get(url='http://google.com.hk/')
print( re.status_code )