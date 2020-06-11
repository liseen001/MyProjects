#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import requests
import re
# proxy = {'http':'http://localhost:8888','https':'https://localhost:8888'}

# response_111= requests.get(url='http://www.baidu.com')
# print(response_111.content.decode('utf-8'))
#
#
# get_data = {'terminal':1,'id':0}
# headerinfos_01 = {'Accept':'application/json, text/plain, */*','Accept-Encoding':'gzip, deflate',
#                'Referer':'http://192.168.101.2:8053/m/home'}
# response_gamelist = requests.get('http://192.168.101.2:8053/api/unauthor/sys/menu',params=get_data,headers=headerinfos_01)
# print(response_gamelist.content.decode('utf-8'))
# print(response_gamelist.status_code)
#
# post_data = {'terminal':1,"username":"liseen001",'password':'a000000'}
# headerinfos_02 = {'Accept':'application/json, text/plain, */*','Accept-Encoding':'gzip, deflate',
#                   'Referer': 'http://192.168.101.2:8053/m/login'}
# response_login = requests.post(url='http://192.168.101.2:8053/api/unauthor/gateway/account/login',data=post_data,headers=headerinfos_02)
# print(response_login.content.decode('utf-8'))
# token = re.findall('"token":"(.+?)",',response_login.content.decode('utf-8'))[0]
#
#
# post_data_ck = {"terminal":1,'isCj':0,'amount':2222,'channel':1,'id':94,'name':'测试'}
# headerinfos_03={'Accept':'application/json, text/plain, */*','Accept-Encoding':'gzip, deflate',
#                   'Referer': 'http://192.168.101.2:8053/m/capital/deposit','Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
#                 'authorization':token}
# response_ck = requests.post(url='http://192.168.101.2:8053/api/pay/offline/remittance/order',data=post_data_ck,headers=headerinfos_03)
# print(response_ck.content.decode('utf-8'))
#
# post_data_ganme={'terminal':1,'gameCode':'DTQP','gameId':0}
# response_game = requests.post(url='http://192.168.101.2:8053/api/game/forward',data=post_data_ganme,headers=headerinfos_03)
# print(response_game.content.decode('utf-8'))

source_str = 'python1class'
# value = re.match('python\dc',source_str).group()
# value = re.search('thon\dc',source_str).group()
regexp = re.compile('thon\dc')
value = regexp.search(source_str).group()
print(value)