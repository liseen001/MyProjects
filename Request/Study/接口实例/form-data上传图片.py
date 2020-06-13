#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc: form-data上传图片
import requests
import re

base ='http://192.168.103.251:9192'  #后台服务器地址
loginUrl = base +'/admin/login'

headerinfo={'Accept':'application/json, text/plain, */*','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
            'Content-Type':'application/json;charset=UTF-8','Referer':'http://192.168.103.251:88/tx-admin/login'}
post_data = {"loginName":"liseen1","password":"123456"}
session_request = requests.session()
loginUrl_request = session_request.post(url=loginUrl,json=post_data,headers=headerinfo)
body_value =loginUrl_request.content.decode('utf-8')
token = re.findall('"token":"(.+?)"',body_value)[0]

headerinfo1={'Accept':'*/*','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
            'Content-Type':'multipart/form-data; boundary=----WebKitFormBoundaryOAL0HKciDkla1ESh','Referer':'http://192.168.103.251:88/tx-admin/system-manage/sys-webcom-img','x-Token':token,'sid':'0'}


f = {'localUrl':(None,'2.png'),'imgFile':('2.png',open('d:\\2.png','rb'),'multipart/form-data')}

updatephoto_request=session_request.post(url='http://192.168.103.251:9192/admin/unuser/common/upload/file',files=f,headers=headerinfo1)
print(updatephoto_request.content.decode('utf-8'))