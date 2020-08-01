#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import requests,random,string,re,glob,time
from  admin.common.config_utils import conf
from admin.common.log_utils import logger

session=requests.session()
class CommonApi(object):
    def __init__(self):
        self.url=conf.url
        self.report_path=conf.report_path




    def login_in(self):
        try:
            api_url=conf.url+'/admin/login'
            json_data={"loginName":conf.loginName,"password":conf.password}
            headinfos={"Accept":"application/json, text/plain, */*",
                       "Accept-Encoding":"gzip, deflate",
                       "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
                       "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
                       "Content-Type":"application/json;charset=UTF-8",
                       "Connection":"keep-alive",
                       "Host":conf.host}
            res=session.post(url=api_url,json=json_data,headers=headinfos)
            logger.info('%s'%('调用登录接口成功'))
        except Exception as e:
            logger.error('获取调用登录后台接口失败，失败的原因是：%s'%(e.__str__()))
        return res

    def get_xtoken(self):
        try:
            xtoken_info = self.login_in().content.decode('utf-8')
            xtoken = re.findall('"token":(.+?),', xtoken_info)[0][1:-1]
            # print('====='+xtoken)
        except Exception as e:
            logger.error('获取X-token失败,失败的原因是：%s'%e.__str__())
        return  xtoken


    def search_cagent(self):
        try:
            api_url=conf.url+'/admin/platform/cagent/listPage'
            headerinfos={"Accept":"application/json, text/plain, */*",
                       "Accept-Encoding":"gzip, deflate",
                       "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
                       "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
                       "Content-Type":"application/json;charset=UTF-8",
                       "Connection":"keep-alive",
                       "Host":conf.host,
                        "terminal": "0",
                         "sid": "0",
                         # "Referer":"http://192.168.101.2:9192/tx-admin/system-manage/platfor-cagent",
                         # "Origin": "http://192.168.101.2:9192",
                         "X-Token":CommonApi().get_xtoken()}
            json_data={"page":1,"limit":10,"cagent":"","status":""}
            res=session.post(url=api_url,json=json_data,headers=headerinfos)
            logger.info('调用查询平台商管理接口成功')
        except Exception as e:
            logger.error('调用查询平台商管理接口失败,失败的原因是：%s'%e.__str__())
        return res

    def upload_images(self):
        try:
            api_url=conf.url+'/admin/unuser/common/upload/file'
            # image_name=1
            files={'file':('hlqp.png',open(str(CommonApi().return_images_path()),'rb'),"image/jpeg")}
            headerinfos ={"Accept":"application/json, text/plain, */*",
                       "Accept-Encoding":"gzip, deflate",
                       "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
                       "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
                       # "Content-Type":"application/json;charset=UTF-8",
                       "Connection":"keep-alive",
                       "Host":conf.host,
                        "terminal": "0",
                         "sid": "0",
                         # "Referer":"http://192.168.101.2:9192/tx-admin/system-manage/platfor-cagent",
                         # "Origin": "http://192.168.101.2:9192",
                         "X-Token":CommonApi().get_xtoken()}
            res=session.post(url=api_url,headers=headerinfos,files=files)
            logger.info('调用传图接口成功，传图路径为：%s'%str(CommonApi().return_images_path()))
        except Exception as e:
            logger.error('调用传图接口失败,失败的原因是：%s'%e.__str__())
        return res

    def return_images_path(self):
        file_path = r"C:\Users\Administrator\Desktop\newadmin\addphtot\*\*.png"
        all_images_path=glob.glob(file_path)
        count=0
        for i in range(len(all_images_path)):
            print(len(all_images_path))
            imagenames = all_images_path[count]
            count += i
            return imagenames


if __name__=="__main__":
    re=CommonApi().return_images_path()
    # if
    # print(re.content.decode('utf-8'))
    # file_path=r"C:\Users\Administrator\Desktop\newadmin\addphtot\*\*.png"
    # images = glob.glob(file_path)
    # if i <=range(len(images)):
    #     re.content.decode('utf-8')
    #     time.sleep(1)
    # else:
    #     print('传图结束')
    print(re)
    # for i in range(11):
    #     CommonApi().upload_images()


