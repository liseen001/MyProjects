#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: requests_utils.py
# @time: 2020/7/13 22:26
# @desc:  封装requests
import requests
import ast,jsonpath,re
from  requests.exceptions import RequestException
from  requests.exceptions import ProxyError
from requests.exceptions import ConnectionError
from  API_TEST_FRAME.common.config_utils import conf
from API_TEST_FRAME.common.check_utils import CheckUtils


class RequestsUtils():
    def __init__(self):
        self.hosts = conf.url
        self.headers = {"Content-Type":"application/json;charset=utf-8"}
        self.session = requests.session()
        self.temp_variables={}

    #封装get方法，需要结合测试用例数据
    def __get(self,get_info):
        try:
            url = self.hosts + get_info["请求地址"]
            response = self.session.get(url = url,
                                        params = ast.literal_eval( get_info["请求参数(get)"] )
                                        )
            response.encoding = response.apparent_encoding
            if get_info["取值方式"] == "json取值":
                value = jsonpath.jsonpath( response.json(),get_info["取值代码"] )[0]
                self.temp_variables[get_info["传值变量"]] = value  # 将变量传入临时变量
            elif get_info["取值方式"] == "正则取值":
                value = re.findall( get_info["取值代码"], response.text )[0]
                self.temp_variables[get_info["传值变量"]] = value
            result = CheckUtils(response).run_check(get_info["期望结果类型"], get_info["期望结果"])
        except ProxyError as e:
            result = {'code': 4, 'result': '[%s]请求：代理错误异常' % (get_info['接口名称'],)}
        except ConnectionError as e:
            result = {'code': 4, 'result': '[%s]请求：连接超时异常' % (get_info['接口名称'])}
        except RequestException as e:
            result = {'code': 4, 'result': '[%s]请求：Request异常，原因是：%s' % (get_info['接口名称'], e.__str__())}
        except Exception as e:
            result = {'code':4,'result':'[%s]请求：系统异常，原因是：%s'%( get_info['接口名称'],e.__str__() )}
        return result

    #封装post请求
    def __post(self,post_info):
        try:
            url = self.hosts + post_info["请求地址"]
            response = self.session.post(url=url,
                                         headers=self.headers,
                                         params = ast.literal_eval(post_info["请求参数(get)"]),
                                         json=ast.literal_eval(post_info["提交数据（post）"])
                                         )
            response.encoding = response.apparent_encoding
            if post_info["取值方式"] == "json取值":
                value = jsonpath.jsonpath( response.json(), post_info["取值代码"] )[0]
                self.temp_variables[ post_info["传值变量"] ] = value  # 将变量传入临时变量
            elif post_info["取值方式"] == "正则取值":  # 正则表达式取值
                value = re.findall( post_info["取值代码"], response.text )[0]  # 取值代码放正则表达式,取列表中的第一个值
                self.temp_variables[post_info["传值变量"]] = value
            result = CheckUtils(response).run_check(post_info["期望结果类型"], post_info["期望结果"])
        except ProxyError as e:
            result = {'code': 4, 'result': '[%s]请求：代理错误异常' % (post_info['接口名称'],)}
        except ConnectionError as e:
            result = {'code': 4, 'result': '[%s]请求：连接超时异常' % (post_info['接口名称'])}
        except RequestException as e:
            result = {'code': 4, 'result': '[%s]请求：Request异常，原因是：%s' % (post_info['接口名称'], e.__str__())}
        except Exception as e:
            result = {'code': 4, 'result': '[%s]请求：系统异常，原因是：%s' % (post_info['接口名称'], e.__str__())}
        return result

    #判断请求方式，并发送请求
    def request(self,step_info):
        try:
            requests_type = step_info["请求方式"]
            param_variable_list = re.findall('\\${\w+}', step_info["请求参数(get)"])
            if param_variable_list:
                for param_variable in param_variable_list:
                    step_info["请求参数(get)"] = step_info["请求参数(get)"]. \
                        replace(param_variable, '"%s"' % self.temp_variables.get(param_variable[2:-1]))
            if requests_type == 'get':
                self.__get(step_info)
                result = self.__get(step_info)
            elif requests_type == 'post':
                data_variable_list = re.findall('\\${\w+}', step_info["提交数据（post）"])
                if data_variable_list:
                    for param_variable in data_variable_list:
                        step_info["提交数据（post）"] = step_info["提交数据（post）"]. \
                            replace(param_variable, '"%s"' % self.temp_variables.get(param_variable[2:-1]))
                result = self.__post(step_info)
            else:
                result = {'code': 1, 'result': '请求方式不支持'}
        except Exception as e:
            result = {'code': 4, 'result': '用例编号[%s]的[%s]步骤出现系统异常，原因是：%s' % (step_info["测试用例编号"],step_info['测试用例步骤'],e.__str__())}
        return  result

    def request_by_step(self,step_infos):
        self.temp_variables = {}
        for step_info in step_infos:
            temp_result = self.request(step_info)
            # print(temp_result)
            if temp_result['code'] !=0:
                break
        return temp_result


if __name__ == '__main__':
    get_info = {'测试用例编号': 'case01', '测试用例名称': '测试能否正确执行获取access_token接口', '用例执行': '是',
                '测试用例步骤': 'step_01', '接口名称': '获取access_token接口',
                '请求方式': 'get', '请求地址': '/cgi-bin/token',
                '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}',
                '提交数据（post）': '', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': 'json键是否存在',
                '期望结果': 'access_token,expires_in'}
    post_info={'测试用例编号': 'case03', '测试用例名称': '测试能否正确删除用户标签', '用例执行': '是',
               '测试用例步骤': 'step_02', '接口名称': '删除标签接口', '请求方式': 'post',
               '请求地址': '/cgi-bin/tags/delete', '请求参数(get)': '{"access_token":${token}}',
               '提交数据（post）': '{"tag":{"id":408}}', '取值方式': '无', '传值变量': '',
               '取值代码': '', '期望结果类型': 'json键值对', '期望结果': '{"errcode":0,"errmsg":"ok"}'}
    # RequestsUtils().__get(get_info)
    RequestsUtils().request(post_info)
    RequestsUtils().request(get_info)


















