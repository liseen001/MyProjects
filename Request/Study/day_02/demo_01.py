#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
# import requests
# import json
#
# import jsonpath
# import re
# post_data={"username":"liseen001","password":"a000000","terminal":0}
# headerinfos = {"Accept":"application/json, text/plain, */*","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
#                "Connection":"keep-alive","Referer":"http://192.168.101.2:6053/home/index","Content-Type":"application/x-www-form-urlencoded;charset=UTF-8"}
#
# response_login = requests.post(url='http://192.168.101.2:6053/api/unauthor/gateway/account/login',headers=headerinfos,data=post_data,allow_redirects=False)
# result = response_login.content.decode('utf-8')
# json_data = json.loads(result)
# token=json_data['data']['token']
# print(response_login.content.decode('utf-8'))
# response_login.close()

# import requests
# import urllib3
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# response = requests.get(url='http://www.360buy.com',verify=False)
# print(response.history)
# print(response.url)


# import requests
# from requests.exceptions import ReadTimeout,ConnectionError,RequestException,InvalidURL
# try:
#     response = requests.get(url='http://httpbin.org/get',timeout=1)
#     print(response.status_code)
# except ReadTimeout:
#     print('Timeout')
# except ConnectionError:
#     print('ConnectionError')
# except RequestException:
#     print('RequestException')
# except Exception as e:
#     print('Unknow')

import re
source_str = 'python1class'
value = re.search('thon\dc',source_str).group()
print(value)