#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import requests
from bs4 import BeautifulSoup

url = 'https://www.imooc.com'
headers ={'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36'}
r =requests.get(url=url,headers=headers)
bs = BeautifulSoup(r.text,'html.parser')

mooc_classess = bs.find_all('h3',class_="course-card-name")  #定位课程信息

class_list = []
for i in range(len(mooc_classess)):
    title = mooc_classess[i].text.strip()
    class_list.append("课程名字：{}\n".format(title))

with open('mooc_classess.txt','a+',encoding='utf-8') as f:
    for text in class_list:
        f.write(text)