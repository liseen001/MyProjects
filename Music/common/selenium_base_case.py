#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import unittest
from Music.common.base_page import BasePage
from Music.common.browser import Browser
from Music.common.config_utils import conf
from Music.common.log_utils import logutils

class SeleniumBaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logutils.info('==================测试类开始执行==================')
        cls.url = conf.music_url


    def setUp(self):
        logutils.info('------------------测试方法开始执行------------------')
        self.base_page = BasePage(Browser().get_default_driver())
        self.base_page.set_browser_personalized()
        self.base_page.implicity_wait()
        self.base_page.open_url(self.url)

    def tearDown(self):
        errors = self._outcome.errors
        for test,exc_info in errors:
            if exc_info:
                self.base_page.substation_wait()
                self.base_page.screen_shoot_as_file()
        self.base_page.close_current_browser_tab()
        logutils.info('------------------测试方法执行完毕------------------')

    @classmethod
    def tearDownClass(cls):
        logutils.info('==================测试类执行完毕==================')