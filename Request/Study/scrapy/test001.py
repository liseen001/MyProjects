#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
from urllib import request

res =request.urlopen('https://www.baidu.com/')
# print(res.read())  #返回一个二进制数据
# print(res.read().decode())  #解码显示百度页面远吗
# print(res.geturl())  #请求的url源码
# print(res.getheaders())  #返回响应头
# print(res.getcode())  #返回状态码


url = "https://vd2.bdstatic.com/mda-ji2k1egrakc2yraf/sc/mda-ji2k1egrakc2yraf.mp4?auth_key=1567757266-0-0-352d0aa60522101452bc7c1816d745b2&bcevod_channel=searchbox_feed&pd=bjh&abtest=all"
res =request.urlretrieve(url,'zjl.mp4')

