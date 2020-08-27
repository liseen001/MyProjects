#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import requests
import ast,jsonpath,re,time,random
from common.testdata_utils import TestdataUtils
from requests.exceptions import RequestException
from requests.exceptions import ProxyError
from requests.exceptions import ConnectionError
from common.config_utils import conf
from common.nblog_utils import logger
from common.check_utils import CheckUtils

class RequestsUtils():
    def __init__(self):
        self.hosts = conf.host
        self.session = requests.session()
        self.temp_variables = {}  #存放临时变量


    def __get(self,get_info):
        '''封装get方法'''
        try:
            url = self.hosts + get_info['请求地址']
            response = self.session.get( url=url,
                                         params=ast.literal_eval( get_info['请求参数(get)'] ),
                                         headers = get_info['请求头'])

            logger.info('{}接口调用成功'.format(get_info[ '接口名称' ]))
            logger.info('\n正在执行的测试用例名称：{}\n正在请求的接口名称：{}\n测试用例编号：{}\n正在执行的测试用例步骤：{}\n请求方式：{}\n请求地址：{}\n请求参数：{}\n请求头是：{}\n'
                        .format(get_info['测试用例名称'],get_info[ '接口名称' ], get_info[ '测试用例编号' ], get_info[ '测试用例步骤' ], get_info[ '请求方式' ],
                                get_info[ '请求地址' ], get_info[ '提交数据（post）' ], get_info[ '请求头' ]))

            response.encoding = response.apparent_encoding
            if get_info['取值方式'] == 'json取值':
                value = jsonpath.jsonpath( response.json(),get_info['取值代码'])[0]
                self.temp_variables[get_info['传值变量']] = value
            elif get_info['取值方式'] == '正则取值':
                value = re.findall( get_info['取值代码'],response.text )[0]
                self.temp_variables[get_info['传值变量']] = value

                #  此段代码为对新增的头部列做正则与传参处理
            if get_info['头部取值方式'] == 'json取值':
                value = jsonpath.jsonpath( response.json(),get_info['头部取值代码'] )
                self.temp_variables[get_info['头部传值变量']] = value
            elif get_info['头部取值方式'] == '正则取值':
                value = re.findall( get_info['头部取值代码'],response.text )[0]
                self.temp_variables[get_info['头部传值变量']] = value


            result = CheckUtils(response).run_check(get_info['期望结果类型'],get_info['期望结果'])
        except ProxyError as e:
            result = {'code': 4, 'result': '[%s]请求：代理错误异常' % (get_info['接口名称'],)}
            logger.error( '[%s]请求：代理错误异常' % (get_info['接口名称'],) )
        except ConnectionError as e:
            result = {'code': 4, 'result': '[%s]请求：连接超时异常' % (get_info['接口名称'])}
            logger.error( '[%s]请求：连接超时异常' % (get_info['接口名称']) )
        except RequestException as e:
            result = {'code': 4, 'result': '[%s]请求：Request异常，原因是：%s' % (get_info[ '接口名称' ], e.__str__())}
            logger.error( '[%s]请求：Request异常，原因是：%s' % (get_info[ '接口名称' ], e.__str__()) )
        except Exception as e:
            result = {'code': 4, 'result': '[%s]请求：系统异常，原因是：%s' % (get_info[ '接口名称' ], e.__str__())}
            logger.error( '[%s]请求：系统异常，原因是：%s' % (get_info[ '接口名称' ], e.__str__()) )
        return result

    def __post(self,post_info):
        '''封装post请求，可以将post提交数据判断是json还是文本格式进行优化'''
        try:
            url = self.hosts + post_info['请求地址']
            response = self.session.post( url=url,
                                          headers =ast.literal_eval(post_info['请求头']),
                                          params=ast.literal_eval( post_info['提交数据（post）'] )
                                          )
            logger.info('{}接口调用成功'.format(post_info[ '接口名称' ]))
            logger.info('\n正在执行的测试用例名称：{}\n正在请求的接口名称：{}\n测试用例编号：{}\n正在执行的测试用例步骤：{}\n请求方式：{}\n请求地址是：{}\n请求参数：{}\n请求头：{}\n'.
                        format( post_info['测试用例名称'],post_info['接口名称'],post_info['测试用例编号'],post_info['测试用例步骤'],post_info['请求方式'],post_info['请求地址'],post_info['提交数据（post）'],post_info['请求头']  ))
            response.encoding = response.apparent_encoding
            if post_info['取值方式'] == 'json取值':
                value = jsonpath.jsonpath( response.json(),post_info['取值代码'] )[0]
                self.temp_variables[ post_info['传值变量'] ] = value
            elif post_info['取值方式'] == '正则取值':
                value = re.findall( post_info['取值代码'],response.text )[0]
                self.temp_variables[ post_info['传值变量'] ] = value

                #  此段代码为对新增的头部列做正则与传参处理
            if post_info[ '头部取值方式' ] == 'json取值':
                value = jsonpath.jsonpath(response.json(), post_info[ '头部取值代码' ])
                self.temp_variables[ post_info[ '头部传值变量' ] ] = value
            elif post_info[ '头部取值方式' ] == '正则取值':
                value = re.findall(post_info[ '头部取值代码' ], response.text)[ 0 ]
                self.temp_variables[ post_info[ '头部传值变量' ] ] = value
            result = CheckUtils(response).run_check(post_info['期望结果类型'],post_info['期望结果'])
        except ProxyError as e:
            result = {'code': 4, 'result': '[%s]请求：代理错误异常' % (post_info['接口名称'],)}
            logger.error( '[%s]请求：代理错误异常' % (post_info['接口名称'],) )
        except ConnectionError as e:
            result = {'code': 4, 'result': '[%s]请求：连接超时异常' % (post_info['接口名称'])}
            logger.error( '[%s]请求：连接超时异常' % (post_info['接口名称']) )
        except RequestException as e:
            result = {'code': 4, 'result': '[%s]请求：Request异常，原因是：%s' % (post_info[ '接口名称' ], e.__str__())}
            logger.error( '[%s]请求：Request异常，原因是：%s' % (post_info[ '接口名称' ], e.__str__()) )
        except Exception as e:
            result = {'code': 4, 'result': '[%s]请求：系统异常，原因是：%s' % (post_info[ '接口名称' ], e.__str__())}
            logger.error( '[%s]请求：系统异常，原因是：%s' % (post_info[ '接口名称' ], e.__str__()) )
        return result

    def request(self,step_info):
        '''封装请求，判断请求方式后调用上面的请求'''
        try:
            request_type = step_info['请求方式']


            #  此段代码为把上个接口获取的变量传入头部中
            header_data_variables_list = re.findall('\\${\w+}', step_info[ '请求头' ])
            if header_data_variables_list:
                for header_data_variables in header_data_variables_list:
                    step_info[ '请求头' ] = step_info[ '请求头' ].replace(header_data_variables,
                                                                    '"%s"'%self.temp_variables.get(
                                                                        header_data_variables[2:-1]))

            param_variable_list = re.findall( '\\${\w+}',step_info['请求参数(get)'] )
            if param_variable_list:
                for param_variable in param_variable_list:
                    step_info['请求参数(get)'] = step_info['请求参数(get)'].replace(param_variable,'"%s"'%self.temp_variables.get( param_variable[2:-1] ))

            if request_type == 'get':
                self.__get(step_info)
                result = self.__get(step_info)
                time.sleep(float('%.1f' % (random.uniform(0, 3))))  #请求等待时间
            elif request_type == 'post':
                data_variables_list = re.findall( '\\${\w+}',step_info['提交数据（post）'] )
                if data_variables_list:
                    for data_variables in data_variables_list:
                        step_info['提交数据（post）'] = step_info['提交数据（post）'].replace(data_variables,'"%s"'%self.temp_variables.get( data_variables[2:-1] ))
                result = self.__post(step_info)
                time.sleep(float('%.1f' % (random.uniform(0, 3))))  #请求等待时间
            else:
                result = {'code':1,'result':"请求方式不支持"}
        except Exception as e:
            result = {'code': 4, 'result': '用例编号[%s]的[%s]步骤出现系统异常，原因是：%s' % (step_info["测试用例编号"],step_info['测试用例步骤'],e.__str__())}
            logger.error( '用例编号[%s]的[%s]步骤出现系统异常，原因是：%s' % (step_info["测试用例编号"],step_info['测试用例步骤'],e.__str__()) )
        return result

    def request_by_step(self,step_infos):
        self.temp_variables = {}
        for step_info in step_infos:
            temp_result = self.request( step_info )
            if temp_result['code'] != 0:
                TestdataUtils().write_result_to_excel( step_info['测试用例编号'],step_info['测试用例步骤'],'测试失败' )
                break
            else:
                TestdataUtils().write_result_to_excel( step_info['测试用例编号'],step_info['测试用例步骤'],'测试通过' )
        return temp_result

    def one(self,post_info):
        '''处理头部传值变量和传值代码'''
        if post_info[ '头部取值方式' ] == '正则取值':
            variables =  post_info['头部传值变量']
        print(type(variables))
            # for variables in post_info[ '头部传值变量' ].split(';'):


    def heard_variables(self,heard_variables_info=None):
        '''头部传值变量'''
        value = heard_variables_info.split(';')


    def heard_access_variables(self,header_access_variables_info=None):
        '''头部取值变量'''
        pass


if __name__ == '__main__':
    get_info = {'测试用例编号': 'case01', '测试用例名称': '测试能否正确登录后台接口', '用例执行': '是', '测试用例步骤':
        'step_01', '接口名称': '登录后台接口', '请求方式': 'post', '请求地址': '/admin/login', '请求参数(get)': '',
                '提交数据（post）': '{"loginName":"liseen1","password":"000000"}', '取值方式': '无', '传值变量': '',
                '取值代码': '', '期望结果类型': 'json键是否存在', '期望结果': '"token"', '测试结果': '', '头部取值方式': '',
                '头部传值变量': '', '头部取值代码': '', '请求头': '{"Accept":"application/json, text/plain, */*","Content-Type": "application/json;charset=UTF-8","User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36","Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8","Accept-Encoding":"gzip, deflate","Connection": "keep-alive"}'}
    post_info ={'测试用例编号': 'case02', '测试用例名称': '测试能否正确查询平台商管理接口', '用例执行': '是',
                '测试用例步骤': 'step_01', '接口名称': '登录后台接口', '请求方式': 'post', '请求地址': '/admin/login', '请求参数(get)': '', '提交数据（post）': '{"loginName":"liseen1","password":"000000"}',
                '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': 'json键是否存在', '期望结果': '"token"', '测试结果': '测试失败', '头部取值方式': '正则取值',
                '头部传值变量': 'token;sid', '头部取值代码': '"token":"(.+?)",;,"cid":(.+?),"name":"', '请求头':
                    '{"Accept":"application/json, text/plain, */*","Content-Type": "application/json;charset=UTF-8","User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36","Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8","Accept-Encoding":"gzip, deflate","Connection": "keep-alive"}'},\
               # {'测试用例编号': 'case02', '测试用例名称': '测试能否正确查询平台商管理接口', '用例执行': '是', '测试用例步骤': 'step_02', '接口名称': '查询平台商管理接口', '请求方式': 'post', '请求地址': '/admin/platform/cagent/listPage',
               #  '请求参数(get)': '', '提交数据（post）': '{"page":1,"limit":10,"cagent":"","status":""}', '取值方式': '正则取值', '传值变量': 'cid', '取值代码': '"id":(.+?),"code"', '期望结果类型': 'json键是否存在', '期望结果': '"msg"',
               #  '测试结果': '', '头部取值方式': '', '头部传值变量': '', '头部取值代码': '', '请求头': '{"Accept":"application/json, text/plain, */*","Content-Type": "application/json;charset=UTF-8","User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36","Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8","Accept-Encoding":"gzip, deflate","Connection":'
               #  ' "keep-alive","X-Token": ${token},"sid":${cid},"terminal":"0"}'}
    # RequestsUtils().request_by_step(post_info)
    # print( RequestsUtils().request_by_step(post_info) )
    # print(RequestsUtils().request(get_info))
    print( RequestsUtils().one(post_info) )

