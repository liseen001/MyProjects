#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import os
import time
import pytest

now_time = time.strftime('%Y_%m_%d_%H_%M_%S')
current_path = os.path.dirname(__file__)
json_report = os.path.join(current_path,'report','json',now_time)
html_report = os.path.join(current_path,'report','html',now_time)

if not os.path.exists(json_report):
    os.makedirs(json_report)
if not os.path.exists(html_report):
    os.makedirs(html_report)

pytest.main(['--alluredir={}'.format(json_report),'-s','-v'])
os.system( 'allure generate {} -o {}--clean'.format(json_report,html_report) )
