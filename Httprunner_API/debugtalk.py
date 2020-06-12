#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import  requests
def get_token():
    get_data={"grant_type":"client_credential",
              "appid":"wx0591278088098c56",
              "secret":"ceaab7a476a85194f507c8a00c82ad1f"}
    response = requests.get(url=' https://api.weixin.qq.com/cgi-bin/token',params=get_data)
    return  response.json()['access_token']


def setup_case( case_name ):
    print('测试用例 %s 开始执行'%case_name)

def teardown_case(case_name):
    print('测试用例 %s 执行结束'%case_name)

def setup_step(case_step):
    print('测试步骤 %s 开始执行'%case_step)

def teardown_step(case_step):
    print('测试步骤 %s 执行结束'%case_step)


if __name__=="__main__":
    print(get_token())