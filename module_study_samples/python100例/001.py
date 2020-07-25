#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
count=0
for i in range(1,5):
    for j in range(1,5):
        for k in  range(1,5):
            if i !=j and j!=k and i!=k:
                print(i,j,k)
                count +=1
print(count)