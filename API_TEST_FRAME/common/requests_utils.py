#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc: 二次封装requests
import requests
import ast
import re
import jsonpath
from API_TEST_FRAME.common.config_utils import conf

class RequestsUtils():
    def __init__(self): #构造方法
        self.hosts = conf.url
        self.headers = {"ContentType":"application/json;charset=utf-8"}
        self.session = requests.session()
        self.temp_variables = {}


    def __get(self,get_info):
        url = self.hosts+ get_info["请求地址"]
        response = self.session.get(url=url,
                                    params =ast.literal_eval(get_info["请求参数(get)"])
                                    ) #ast.literal_eval：把请求参数字符串转换为json
        response.encoding = response.apparent_encoding    #根据返回body的编码格式去编码避免乱码,下面返回的结果时text
        if get_info["取值方式"] =="json取值":
            value = jsonpath.jsonpath(response.json(),get_info["取值代码"])[0]
            self.temp_variables[get_info["传值变量"]] =value
        elif get_info["取值方式"] =="正则取值":
            value = re.findall(get_info["取值代码"],response.text)[0]
            self.temp_variables[get_info["传值变量"]] = value


        result = {
            'code': 0,  #请求是否成功的标志位
            'response_reson': response.reason,
            'response_code': response.status_code,
            'response_headers': response.headers,
            'response_body': response.text
        }
        return  result

    def __post(self,post_info):
        url = self.hosts+ post_info["请求地址"]
        response = self.session.post(url=url,
                                     params = ast.literal_eval(post_info["请求参数(post)"]),
                                     # data = post_info["提交数据(post)"],
                                     json=ast.literal_eval(post_info["提交数据(post)"])
                                     )
        response.encoding =response.apparent_encoding
        if post_info["取值方式"]=="json取值":
            value = jsonpath.jsonpath(response.json(),post_info["取值代码"])[0]
            self.temp_variables[post_info["传值变量"]] = value
        elif post_info["取值方式"] =="正则取值":
            value = re.findall(post_info["取值代码"], response.text)[0]
            self.temp_variables[post_info["传值变量"]] = value  #判断取值方式

        result = {
            'code': 0,
            'response_reason': response.reason,
            'response_headers': response.headers,
            'response_body': response.text
        }
        return result

    def request(self,step_info):
        request_type = step_info["请求方式"]
        if request_type == "get":
            result = self.__get(step_info)
        elif request_type == "post":
            result = self.__post(step_info)
        else:
            result = {"code":3,"result":"请求方式不支持"}
        return result

    def request_by_step(self,step_infos):
        for step_info in step_infos:
            temp_result = self.request(step_info)
            if temp_result["code"] !=0:
                break
        return temp_result

if __name__=="__main__":
    get_inf0 ='{"测试用例编号": "case01", "测试用例名称": "测试能否正确执行获取access_token接口", "用例执行": "是", "测试用例步骤": "step_01", "接口名称": "获取access_token接口", "请求方式": "get", "请求地址": "/cgi-bin/token", "请求参数(get)": "{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}", "提交数据（post）": '', "取值方式": "无", "传值变量": '', "取值代码": "", "期望结果类型": "json键是否存在", "期望结果": "access_token,expires_in"}'