#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: requests_utils.py
# @time: 2020/7/13 22:26
# @desc:  封装requests
import requests
from  API_TEST_FRAME.common.config_utils import conf
class RequestsUtils():
    def __init__(self):  #构造
        self.hosts = conf.url
        self.headers = {"ContemtType":"application/json;charset=utf-8"}
        self.session = requests.session()


    def get(self,get_infos):
        url = self.hosts +get_infos["请求地址"]
        response = self.session.get(url=url,
                                    params=""
                                    )



















if __name__=="__main__":
    get_infos={"excel读取的测试用例数据"}  #请求地址