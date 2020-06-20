#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: debugtalk.py
# @time: 2020/6/12 21:25
# @desc:
import requests
import random
import string

def get_access_token():
    '''
    返回access_token的方法
    :return: access_token
    '''
    get_params={'grant_type':'client_credential','appid':'wx0591278088098c56',
                'secret':'ceaab7a476a85194f507c8a00c82ad1f'}
    response =requests.get(url='https://api.weixin.qq.com/cgi-bin/token',params=get_params)
    return response.json()['access_token']


'''生成随机字符串'''
def ranstr():
    '''
    生成随机字符串的函数
    :return: salt
    '''
    salt = ''.join(random.sample(string.ascii_letters + string.digits, 5))
    return salt

def add_tags():
    '''
    新增用户标签
    :return:
    '''
    get_params={'access_token':get_access_token()}
    json_data = {"tag": {"name":str(ranstr())}}
    response =requests.post(url='https://api.weixin.qq.com/cgi-bin/tags/create',params=get_params,json=json_data)
    return response.json()['tag']['id']



if __name__=="__main__":
    print(add_tags())
