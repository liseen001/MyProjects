#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import unittest
import requests
class APITest(unittest.TestCase):
    def setUp(self):
        self.hosts='http://192.168.103.251:9192'

    def tearDown(self):
        pass

    '''登录接口与获取token'''
    def test_token(self):
        self.api_url ='/admin/login'
        self.post_data = {"loginName":"liseen1","password":"123456"}
        response_obj = requests.post(url=self.hosts+self.api_url,json=self.post_data)
        self.assertEqual(response_obj.json()['msg'],'登录成功')



    def test_update_googlesectet(self):
        token = requests.post(url=self.hosts+'/admin/login',json={"loginName":"liseen1","password":"123456"}).json()['data']['token']
        api_url = '/admin/sys/google/secret/modify'
        post_data = {"cid":"","username":"3333sdf","id":42}
        headerinfo = {'Accept':'application/json, text/plain, */*','User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
                      'X-Token':token,'sid':'0'}
        response_obj = requests.post(url=self.hosts+api_url,json=post_data,headers=headerinfo)
        self.assertEqual(response_obj.json()['msg'],'修改用户名成功')



if __name__=="__main__":
    unittest.main()