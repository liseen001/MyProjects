#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
from selenium import  webdriver
import time
import os

current_path = os.path.dirname(__file__)
chromedriver = os.path.join(current_path,'../driver/chromedriver.exe')
print(chromedriver)

driver = webdriver.Chrome(executable_path=chromedriver)
url ="http://192.168.101.2:6051/home/index"

driver.get(url)