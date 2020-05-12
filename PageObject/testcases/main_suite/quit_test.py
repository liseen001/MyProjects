# --*utf-8*--
import unittest
from PageObject.common.browser import browser
from PageObject.actions.login_action import LoginAction
from PageObject.common.base_page import BasePage
from PageObject.common.config_utils import conf
from PageObject.actions.quit_action import QuitAction
from PageObject.element_infos.main.main_page import MainPage

class QuitTest(unittest.TestCase):
    def setUp(self):
        self.base_page=BasePage(browser.get_default_driver())
        self.base_page.set_browser_max()
        self.base_page.implicitly_wait()
        self.base_page.open_url(conf.zend_path)

    def tearDown(self):
        self.base_page.close_tab()


    def test_quit(self):
        login_action=LoginAction(self.base_page.driver)
        main_page=login_action.default_login()
        quit_action=QuitAction(main_page.driver)
        login_page=quit_action.quit()
        actual_result=login_page.get_title()
        self.assertEqual(actual_result.__contains__('用户登录'),True,'test_quit用例执行失败')


if __name__=="__main__":
    unittest.main()