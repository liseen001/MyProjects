#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import re
import ast

temp_variables = {"token":"123456"}
params = '{"access_token",${token}}'

value = re.findall( '\\${\w+}',params )[0]
# print( value )

'''通过正则表达式取出字典中的${token},然后用${token}替代'''
params = params.replace( value,temp_variables.get( value[2:-1] ) )
# print( params )

temp_variables = { "token":"132456","number":"123","age":"66" }
str1 = '{"access_token":${token},"age":${age},"number",${number}}'
for i in re.findall( '\\${\w+}',str1 ):
    print( i )
    str1 = str1.replace( i,temp_variables.get(i[2:-1]) )
print( str1 )