#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import os
import ast,jsonpath
import requests,re
# print(eval('66+72'))
# print( eval( '{"name":"linux","age":18}' ) )
# print(eval('[1,2,3,4,5,[1,2,3]]'))
# print(eval('(1,2,3,4,5,7,7)'))
# print(eval('{1,2,3,4,5,5,6}'))
#
# print(eval( '{"name":"linux","age":age}',{"age":18} ))
#
# print(ast.literal_eval('{"name":"linux","age":18}'))
# print(ast.literal_eval('[1,2,3,4,5,[1,2,3]]'))
# print(ast.literal_eval('(1,2,3,4,5,7,7)'))
# print(ast.literal_eval('{1,2,2,3,4,4,5}'))

class RequestUtils():
    def __init__(self):
        self.hosts='http://192.168.101.2:6073'
        self.headers={"Accept":"application/json, text/plain, */*","Referer":"http://192.168.101.2:6073/home/index","Host":"192.168.101.2:6073",
                      "Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8","Connection":"keep-alive",
                      "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
                      }
        self.session=requests.session()
        self.temp_variables={}

    def get(self,get_info):
        url = self.hosts+get_info["请求地址"]
        # print(url)
        response = self.session.get( url=url,headers=self.headers,params = ast.literal_eval(get_info[ "请求参数(get)" ]))
        response.encoding = response.apparent_encoding
        # print(response.text)
        if get_info['取值方式']=="json取值":
            value = jsonpath.jsonpath(response.json(),get_info['取值代码'])[0]
            self.temp_variables[get_info["传值变量"]] = value
        elif get_info['取值方式'] == "正则取值":
            value = re.findall( response.text, get_info["取值代码"] )[0]
            self.temp_variables[get_info["传值变量"]] = value

        result = {
            'code':0,                                         #标志位，请求是否成功的标志位
            'response_reson':response.reason,                 #响应行
            'response_code':response.status_code,             #响应状态吗
            'response_headers':response.headers,              #响应头
            'response_body':response.text                     #响应正文
        }
        return result

    def request(self,step_infos):
        requests_step = step_infos["请求方式"]
        if requests_step=="get":
            self.get(step_infos)
            result = self.get( step_infos )
        elif requests_step == "post":
            result = self.post( step_infos )
        else:
            result = {'code':3,'result':'请求方式不支持'}
        print( result['code'] )
        return result

    def request_by_step(self,step_infos):
        for step_info in step_infos:
            temp_result = self.request(step_info)
            if temp_result['code'] !=0:
                break
        return  temp_result





if __name__ == '__main__':
    # get_info={"请求地址":"/api/unauthor/sys/menu","请求参数(get)":'{"id":0,"terminal":0}',"请求方式":"get"}
    # result=RequestUtils().get(get_info)
    # print(result)
    step_infos = {"请求地址": "/api/unauthor/sys/menu", "请求参数(get)": '{"id":0,"terminal":0}', "请求方式": "get"}
    # res = RequestUtils().request(step_infos)
    # print(res)


    import re, ast
    import requests

    tem_variables = {"token": "123456"}
    params = '{"access_token":${token}}'

    value = re.findall('\\${\w+}', params)[ 0 ]
    print(value)

    # params = params.replace( value ,tem_variables["token"] )
    params = params.replace(value, tem_variables.get(value[ 2:-1 ]))
    print(params)

    temp_variables = {"token": "123456", "number": "123", "age": "66"}
    str1 = '{"access_token:${token},${age}==>${number}}'
    for i in re.findall('\\${\w+}', str1):
        print(i)
        str1 = str1.replace(i, temp_variables.get(i[ 2:-1 ]))
    print(str1)