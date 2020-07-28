#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:  读写二进制文件  python不进支持文本文件的写入，也支持二进制文件的读写，如图片、声音文件等
import base64
'''
一、读取二进制文件
1、读取二进制文件用 'rb'  模式
'''
with open(r'C:\Users\Administrator\Desktop\开版\1\dtqp\220.png','rb') as file:
    image_data=file.read()
    base64_data=base64.b64encode(image_data)
    print(base64_data)

with open(r'C:\Users\Administrator\PycharmProjects\MyProjects\module_study_samples\文件和目录\test.png','wb') as f:
    f.write(image_data)

'''
二、总结
1、读取二进制文件使用  'rb'  模式
2、写入二进制文件使用  'wb'  模式
'''
