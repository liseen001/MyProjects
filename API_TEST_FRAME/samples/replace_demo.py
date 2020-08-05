#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: replace_demo.py
# @time: 2020/8/5 23:44
# @desc:  替换正则表达式或jsonpath取值变量
import re,ast
import requests

temp_variables = {"token": "123456"}

params = '{"access_token":${token}}'  #建议考虑一个以上的情况替换值

value = re.findall( '\\${\w+}',params )[0]  #正则表达式替换 \\ 转义 $ 查找以$开头,把找出来的值替换temp_variables中的123465
print( value )

# params = params.replace(value,temp_variables["access_token"])  #替换方式一
params = params.replace( value,temp_variables.get(value[2:-1]) )  #替换方式二
print(params)

temp_variables = {"token": "123456","number":"123","age":"66"}   #替换多个
str1 = '{"access_token":${token},${age}==>${number}}'
for i in re.findall('\\${\w+}',str1):
    print(i)
    str1 = str1.replace(i,temp_variables.get( i[2:-1] ))  #   i[2:-1] = ${token}
print(str1)

# requests.get(url='/cgi-bin/tags/delete',
#              params=ast.literal_eval( params )
#              )