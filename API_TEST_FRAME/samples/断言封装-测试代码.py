#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: 断言封装-测试代码.py
# @time: 2020/8/10 22:39
# @desc: 封装断言
# 期望结果类型：1、无 2、json键是否存在 3、json键值对  4、正则匹配
# 期望结果
import re,ast

#1、正则匹配测试
#实际结果
str1 = '{"access_token":"3_sdf45dffg456","expires_in":7200}'
#期望结果
# str2 ='{"access_token":"(.+?)","expires_in":(.+?)}'
# print( re.findall( str2,str1 ) )
# if re.findall( str2 , str1 ):
#     print( True )
# else:
#     print( False )

#2、是否包含json键(key)  access_token,expires_in  考虑递归把复杂的json数据判断
jsondata1 = ast.literal_eval( str1 )
# str2 = 'access_token,expires_in'
# check_key_list = str2.split(',')
# # print(check_key_list)
# for check_key in check_key_list:
#     result = True
#     if check_key in jsondata1.keys():
#         result = True
#     else:
#         result = False
#     if not result:
#         break1
# print(result)

#3、json键值对相等  '{"expires_in":720}'
str2 = '{"expires_in":7200}'
for v in ast.literal_eval( str2 ).items():
    result = True
    if v in jsondata1.items():
        result =True
    else:
        result = False
    if not result:
        break
print( result )