#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import requests
import re
import json
session_req = requests.session()

get_data = {"grant_type":'client_credential','appid':'wx0591278088098c56','secret':'ceaab7a476a85194f507c8a00c82ad1f'}
body=session_req.get(url='https://api.weixin.qq.com/cgi-bin/token',params=get_data)
res_gettoken_body = body.content.decode('utf-8')
print(res_gettoken_body)
token=re.findall('"access_token":"(.+?)"',res_gettoken_body)[0]

json_data={"tag":{"name":"小木屋啊"}}
get_data = {'access_token':token}
res_maketag = session_req.post(url='https://api.weixin.qq.com/cgi-bin/tags/create',params=get_data,json=json_data)
print(res_maketag.content.decode('utf-8'))
