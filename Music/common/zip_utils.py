#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import os
import zipfile

def zip_dir(dir_path,zip_path):
    '''

    :param dir_path: 目标文件夹路径
    :param zip_path: 压缩后的文件夹路径
    :return:
    '''
    zip = zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED)
    for root,dirnames,filenames in os.walk(dir_path):
        file_path = root.replace(dir_path,'')  #去掉根路径，只对目标文件夹下的文件及文件夹进行压缩
        #循环处一个个文件名
        for filename in filenames:
            zip.write(os.path.join(root,filename),os.path.join(file_path,filenames))
        zip.close()