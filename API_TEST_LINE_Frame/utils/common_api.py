#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:  封装接口的公告模块
from API_TEST_LINE_Frame.utils.config_utils import conf
import requests

class CommonApi(object):
    def __init__(self):
        self.hosts=conf.hosts_url
        self.report_path = conf.report_parh

    '''封装登录'''
    def logion_in(self):
        api_url = conf.hosts_url+ '/admin/login'
        json_data = {"loginName":conf.login_username,"password":conf.login_password}
        headerinfos ={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
                      'Content-Type':'application/json;charset=UTF-8',}
        response_obj = requests.post(url=api_url,json=json_data,headers=headerinfos)
        return  response_obj

    '''封装获取token'''
    def get_token(self):
        response_obj = self.logion_in()
        return response_obj.json()['data']['token']

    '''封装修改谷歌秘钥接口'''
    def update_google_secret(self):
        api_url = self.hosts+'/admin/sys/google/secret/modify'
        json_data = {"cid":"","username":"3333sdf3","id":42}
        headerinfo = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
                      'Content-Type':'application/json;charset=UTF-8','X-Token':self.get_token(),'sid':'0'}
        response_obj = requests.post(url=api_url,json=json_data,headers=headerinfo)
        return  response_obj



if __name__=="__main__":
    re = CommonApi()
    va = re.update_google_secret().json()
    print(va)