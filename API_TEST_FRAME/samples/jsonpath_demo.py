#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: jsonpath_demo.py
# @time: 2020/8/5 0:00
# @desc:
import jsonpath

data={"access_token":
          "35__nZXHjUbxhptJMuGJvWTAf2Dtlgh7gfjZbXIUizW4OIxhj_Kgccz7-RINr11f5H324UhOK-p016XF3dU7z_vjZTnmIflYfjuemRa2cL-m1EU2qmBvjYHeZUaIUMbQP9M-P8SzA83HdjEM4wnIHBaAHALKE",
      "expires_in":7200}
print(jsonpath.jsonpath(data,'$.access_token')[0])  #jsonpath返回的是一个列表，需要加下标
