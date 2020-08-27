#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc: 封装断言,可扩展
import re
import ast
from common.nblog_utils import logger
class CheckUtils():
    def __init__(self, check_response=None):  # 构造的时候传一个requests的响应正文
        self.ck_response = check_response
        self.ck_rules = {
            "无": self.no_check,
            "json键是否存在": self.check_key,
            "json键值对": self.check_keyvalue,
            "正则匹配": self.check_regexp
        }
        self.pass_result = {
            'code': 0,  # 标志位，请求是否成功的标志位
            'response_reason': self.ck_response.reason,  # 响应行
            'response_code': self.ck_response.status_code,  # 响应状态码
            'response_headers': self.ck_response.headers,  # 响应头
            'response_body': self.ck_response.text,  # 响应正文
            'check_result': True,  # 断言结果
            'message': ''  # 保留字段，作为日志输出等
        }
        self.fail_result = {
            'code': 2,  # 标志位，表示请求失败
            'response_reason': self.ck_response.reason,  # 响应行
            'response_code': self.ck_response.status_code,  # 响应状态码
            'response_headers': self.ck_response.headers,  # 响应头
            'response_body': self.ck_response.text,  # 响应正文
            'check_result': False,  # 断言结果
            'message': '断言失败'  # 保留字段，作为日志输出等
        }

    def no_check(self, check_data=None):
        '''
        断言结果为无
        :return:
        '''
        return self.pass_result

    def check_key(self, check_data=None):
        '''
        是否包含json键
        :return:
        '''
        check_data_list = check_data.split(',')
        res_list = [ ]  # 存放每次比较的结果
        wrong_key = [ ]  # 存放比较失败的key
        for check_data in check_data_list:
            if check_data in self.ck_response.json().keys():
                res_list.append(self.pass_result)
            else:
                res_list.append(self.fail_result)
                wrong_key.append(check_data)
        # print( reslist,wrongkey )

        if self.pass_result in res_list:
            return self.fail_result
        else:
            return self.pass_result

    def check_keyvalue(self, check_data=None):
        '''
        判断json键值对是否正确
        :param check_data:
        :return:
        '''
        res_list = [ ]
        wrong_items = [ ]
        for check_item in ast.literal_eval(check_data).items():  # 把字符串转成字典，excel表格的数据为字符串
            if check_item in self.ck_response.json().items():
                res_list.append(self.pass_result)
            else:
                res_list.append(self.fail_result)
                wrong_items.append(self.fail_result)
        # print( res_list , wrong_items )
        if self.pass_result in res_list:
            return self.fail_result
        else:
            return self.pass_result

    def check_regexp(self, check_data=None):
        '''
        判断正则是否正确
        :return:
        '''
        pattern = re.compile(check_data)
        if re.findall(pattern=pattern, string=self.ck_response.text):  # 空列表为False
            return self.pass_result
        else:
            return self.fail_result

    def run_check(self, check_type=None, check_data=None):  # 检查类型和检查值
        '''
        让断言运行的方法
        :return:
        '''
        code = self.ck_response.status_code
        if code == 200:
            if check_type in self.ck_rules.keys():
                result = self.ck_rules[ check_type ](check_data)
                return result
            else:
                self.fail_result[ 'message' ] = '不支持%s判断方法' % check_type
                return self.fail_result
        else:
            self.fail_result[ 'message' ] = '请求的响应状态码非%s' % str(code)
            return self.fail_result


if __name__ == '__main__':
    # CheckUtils({"access_token":"hello","expires_in":7200}).check_key("access_token,expires_in")
    # CheckUtils({"access_token": "hello", "expires_in": 7200}).check_keyvalue('{"expires_in":720}')
    CheckUtils({"access_token": "hello", "expires_in": 7200}).check_regexp('"access_token": "(.+?)"')
    # s = {"access_token":"hello","expires_in":7200}
    # print(list(s.keys()))
