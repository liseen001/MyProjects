#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:  封装接口的公告模块
import requests
import random
import string
import re
from API_TEST_LINE_Frame.utils.config_utils import conf
from API_TEST_LINE_Frame.utils.log_utils import logutils


class CommonApi(object):
    def __init__(self):
        self.hosts=conf.hosts_url
        self.report_path = conf.report_parh

    '''生成随机字符串'''
    def ranstr(self,num):
        self.num=num
        self.num=5
        self.salt = ''.join(random.sample(string.ascii_letters + string.digits, self.num))
        return self.salt


    '''封装调用获取access_token接口'''
    def get_access_token(self):
        try:
            api_url = conf.hosts_url + '/cgi-bin/token'
            get_params = {"grant_type": conf.weixin_grant_type, "appid": conf.weixin_appid,
                          'secret': conf.weixin_secret}
            headerinfos = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
                'Content-Type': 'application/json;charset=UTF-8'}
            response_obj = requests.post(url=api_url, params=get_params, headers=headerinfos)
            logutils.info('调用获取access_token接口成功')
        except Exception as e:
            logutils.error('调用获取access_token接口失败，失败的原因是:[%s]'%e.__str__())
        return  response_obj

    '''封装封装获取token接口，返回access_token值'''
    def get_default_access_token(self):
        try:
            response_obj = self.get_access_token()
            logutils.info('获取access_token成功，access_token为：[%s]'%(response_obj.json()['access_token']))
        except Exception as e:
            logutils.error('获取access_token失败，失败的原因是:[%s]'%e.__str__())
        return response_obj.json()['access_token']

    '''封装新增用户标签接口'''
    def add_tags(self):
        try:
            api_url =conf.hosts_url+'/cgi-bin/tags/create'
            get_params={"access_token":str(CommonApi().get_default_access_token())}
            headerinfos = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
                'Content-Type': 'application/json;charset=UTF-8'}
            json_data = {"tag" : {"name" : str(CommonApi().ranstr(5))}}
            response_obj = requests.post(url=api_url,params=get_params,headers=headerinfos,json=json_data)
            logutils.info('新增用户标签成功，新增的标签为：[%s]'%json_data['tag']['name'])
            logutils.info('创建的标签id为：[%s]'%str(response_obj.json()['tag']['id']))
        except Exception as e:
            logutils.error('新增用户标签失败，失败的原因是:[%s]'%e.__str__())
        return response_obj

    '''封装获取公众号已创建的标签接口'''
    def look_for_makedtags(self):
        try:
            api_url=self.hosts+'/cgi-bin/tags/get'
            get_params = {"access_token":str(CommonApi().get_default_access_token())}
            headerinfos = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
                            'Content-Type': 'application/json;charset=UTF-8'}
            response_obj =requests.post(url=api_url,params=get_params,headers=headerinfos)
            logutils.info('获取公众号已创建的标签成功')
        except Exception as e:
            logutils.error('获取公众号已创建的标签失败，失败的原因是[%s]'%e.__str__())
        return  response_obj

    '''封装编辑标签接口'''
    def edit_tags(self):
        try:
            api_url = self.hosts+'/cgi-bin/tags/update'
            get_params = {"access_token": str(CommonApi().get_default_access_token())}
            headerinfos = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
                            'Content-Type': 'application/json;charset=UTF-8'}
            body_info = CommonApi().look_for_makedtags()
            id =body_info.json()['tags'][random.randint(0,90)]['id']
            json_data = {"tag": {"id": id, "name": str(CommonApi().ranstr(5))}}
            response_obj = requests.post(url=api_url,params=get_params,json=json_data,headers=headerinfos)
            logutils.info('编辑标签成功')
        except Exception as e:
            logutils.error('编辑标签失败，失败的原因是：[%s]'%e.__str__())
        return response_obj

    '''封装删除标签接口'''
    def delete_tags(self):
        try:
            api_url = '/cgi-bin/tags/delete'
            get_params = {"access_token": str(CommonApi().get_default_access_token())}
            headerinfos = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
                            'Content-Type': 'application/json;charset=UTF-8'}
            body_info = CommonApi().add_tags()
            id = body_info.json()['tag']['id']
            json_data = {   "tag":{        "id" : id   } }
            response_obj = requests.post(url=self.hosts+api_url,params=get_params,headers=headerinfos,json=json_data)
            logutils.info('删除标签id: [%s] 成功'%id)
        except Exception as e:
            logutils.error('删除标签：[%s] 失败'%id,'失败的原因是:%s'%e.__str__())
        return response_obj









if __name__=="__main__":
    re = CommonApi().add_tags()
    print(re.content.decode('utf-8'))