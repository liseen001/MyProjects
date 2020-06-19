#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import  requests,random
def get_token():
    get_data={"grant_type":"client_credential",
              "appid":"wx0591278088098c56",
              "secret":"ceaab7a476a85194f507c8a00c82ad1f"}
    response = requests.get(url=' https://api.weixin.qq.com/cgi-bin/token',params=get_data)
    return  response.json()['access_token']


'''随机生成多个count随机整数，随机整数的最大值和最小值'''
def get_randomint(min,max,count=None):
    randomint_list = []
    for i in range(count):
        randomint_list.append(random.randint(min,max))
    return randomint_list




def setup_case( case_name ):
    print('测试用例 %s 开始执行'%case_name)

def teardown_case(case_name):
    print('测试用例 %s 执行结束'%case_name)

def setup_step(case_step):
    print('测试步骤 %s 开始执行'%case_step)

def teardown_step(case_step):
    print('测试步骤 %s 执行结束'%case_step)


if __name__=="__main__":
    a= get_randomint(1,20,10)
    print(type(a))
    print(a)