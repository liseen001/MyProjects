#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
'''
1、获取整个网页的HTML信息
2、解析HTML信息
'''
from bs4 import BeautifulSoup
import requests


















if __name__=="__main__":
    target="http://www.biqukan.com/1_1094/5403177.html"
    req=requests.get(url=target)
    html=req.text
    bf=BeautifulSoup(html)
    texts=bf.find_all('div',class_='showtxt')
    print(texts)