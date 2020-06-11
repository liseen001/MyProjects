#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
from Music.element_infos.login.login_page import LoginPage
from Music.element_infos.main.main_page import MainPage
from Music.common.config_utils import conf
from Music.common.log_utils import logutils

class LoginAction:
    def __init__(self,driver):
        self.login_page = LoginPage(driver)

    def login_action(self,username,password):
        self.login_page.input_username(username)
        self.login_page.input_password(password)
        self.login_page.click_login()

    def login_success(self,username,password):
        try:
            self.login_action(username, password)
            logutils.info('登录成功')
        except Exception as e:
            logutils.error('登录失败，失败的原因是：%s'%e.__str__())
        return MainPage(self.login_page.driver)

    def default_login(self):
        return self.login_success(conf.username,conf.password)

    def login_fail(self,username,password):
        self.login_action(username, password)
        logutils.info('登录失败,返回登录失败的提示信息为：%s'%self.login_page.get_login_fail_return_content())
        return self.login_page.get_login_fail_return_content()

    def login_by_cookie(self):
        pass