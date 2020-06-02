#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
from Music.element_infos.login.login_page import LoginPage
from Music.element_infos.main.main_page import MainPage
from Music.common.config_utils import conf

class QuitAction:
    def __init__(self,driver):
        self.main_page = MainPage(driver)


    def quit(self):
        pass
