#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import os
import xlrd

file_path_01 = r'C:\Users\Administrator\Desktop\opencagent\photo\h5lunbo\\'
file_path_02= r'C:\Users\Administrator\Desktop\opencagent\photo\h5youhui\rukou\\'

# for filename01 in os.listdir(file_path_01):
#     for filename02 in os.listdir(file_path_02):
#         image_path1 = os.path.join(file_path_01, filename01)
#         image_pat2=os.path.join(file_path_02,filename02)
#         count=0
#         for i in  len(os.listdir(file_path_01)):
#             count +=i
#             image_pat2=image_pat2[i]
#     print( image_path1,image_pat2 )

# for i in  os.listdir(file_path_01):
#     list=[i]
#     lista=list[int(i)]
#     print(lista)

# wb=xlrd.open_workbook(r'C:\Users\Administrator\Desktop\newadmin\dtqp.xls','r')
# sheet1 = wb.sheet_by_name('dtqp')
# print(sheet1.cell_value(0,0))
# # for col in sheet1.gridline_colour_index:
# #     print(col)
#
# for i in range(sheet1.ncols):
#         print(sheet1.cell_value(i,2))

import os
import requests
import re
from urllib.request import urlretrieve
hraders={"Accept":"application/json, text/plain, */*","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
         "Connection":"keep-alive","Referer":"http://192.168.101.2:8073/m/home"}
content= requests.get(url='http://192.168.101.2:8073/api/unauthor/sys/menu?terminal=1&id=0',headers=hraders).text
# print(content)
results = re.findall('"href":"(.+?).png"',content)
for result in results:
        print(result+'.png')
# print(len(results))



def save_img(imgurl,file_name,file_path='book/img'):
        try:
                if not os.path.exists(file_path):
                        print('文件夹',file_path,'不存在，重新建立')
                        os.mkdir( file_path )
                #获得图片后缀
                file_suffix = os.path.split( imgurl )[1]
                #拼接图片名(包含路径)
                file_name = '{}{}{}{}'.format( file_path,os.sep,file_name,file_suffix )
                #下载图片，并保存到文件中
                if  imgurl:
                        urlretrieve(imgurl,filename=file_name)
                else:
                        print('404')
        except IOError as e:
                print('文件操作失败',e)
        except Exception as e:
                print('错误',e)
print(save_img(result,'test'))