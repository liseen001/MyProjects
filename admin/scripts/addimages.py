#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import os
import glob
# with open(r"C:\Users\Administrator\Desktop\newadmin\addphtot\chess",'rb') as file:
#     for i in file:
#         print(glob.glob(r"C:\Users\Administrator\Desktop\newadmin\addphtot\chess\*.png"))

# print(glob.glob(r"C:\Users\Administrator\Desktop\newadmin\addphtot\chess\*.png"))
a=glob.glob(r"C:\Users\Administrator\Desktop\newadmin\addphtot\*\*.png")
# count=0
print(a)
for i in range(len(a)):
    print(a[i])

