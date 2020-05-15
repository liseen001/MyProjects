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
        cls.url=conf.zend_path

    '''测试执行之前准备工作'''
    def setUp(self):
        logutils.info('-------------测试方法开始执行-------------')
        self.base_page=BasePage(Browser().get_default_driver())   #实例化base_page对象
        self.base_page.set_browser_max()   #设置浏览器最大化
        self.base_page.implicitly_wait()   #设置隐式等待时间,base_page
        self.base_page.open_url(self.url)  #打开浏览器


    '''测试方法执行完毕后关闭浏览器'''
    def tearDown(self):
        logutils.info('-------------测试方法执行完毕-------------')
        self.base_page.close_tab()
        '''可以加测试用例失败截图'''

    @classmethod
    def tearDownClass(cls):
        logutils.info('==============测试类执行完毕==============')