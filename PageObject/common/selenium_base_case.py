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

    def setUp(self):
        logutils.info('-------------测试方法开始执行-------------')
        self.base_page=BasePage(Browser().get_default_driver())
        self.base_page.set_browser_max()
        self.base_page.implicitly_wait()
        self.base_page.open_url(self.url)

    def tearDown(self):
        logutils.info('-------------测试方法执行完毕-------------')
        self.base_page.close_tab()
        '''可以加测试用例失败截图'''

    @classmethod
    def tearDownClass(cls):
        logutils.info('==============测试类执行完毕==============')