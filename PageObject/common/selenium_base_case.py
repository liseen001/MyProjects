# --*utf-8*--
import unittest
from PageObject.common.base_page import BasePage
from PageObject.common.browser import Browser
from PageObject.common.config_utils import conf
from PageObject.common.log_utils import logutils

class SeleniumBaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logutils.info('')
        logutils.info('==============测试类开始执行==============')
        cls.url=conf.url

    '''测试执行之前准备工作'''
    def setUp(self):
        logutils.info('-------------测试方法开始执行-------------')
        self.base_page=BasePage(Browser().get_default_driver())   #实例化base_page对象
        self.base_page.set_browser_max()   #设置浏览器最大化
        self.base_page.implicitly_wait()   #设置隐式等待时间,base_page
        self.base_page.open_url(self.url)  #打开浏览器


    '''测试方法执行完毕后关闭浏览器'''
    def tearDown(self):
        #判断测试用例失败截图，如果测试用例执行失败就截图
        # if len(self._outcome.errors)>=1:
        #     self.base_page.screen_shoot_as_file()
        errors = self._outcome.errors
        for test,exc_info in errors:
            if exc_info:
                self.base_page.wait(3)
                self.base_page.screen_shoot_as_file()
        self.base_page.close_tab()
        logutils.info('-------------测试方法执行完毕-------------')

    @classmethod
    def tearDownClass(cls):
        logutils.info('==============测试类执行完毕==============')