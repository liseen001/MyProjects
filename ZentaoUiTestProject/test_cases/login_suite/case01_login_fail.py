# --*utf-8*--
import time
import unittest
from selenium.webdriver.common.by import By
from common import set_driver,login,loginout

class LoginFail(unittest.TestCase):
    def setUp(self):
        self.driver =set_driver.set_driver()


    def test01_login(self):
        '''这是一个测试登陆失败的用例'''
        login.login(self.driver,'adms232in','adfas')
        alter = self.driver.switch_to_alert()
        alter_text =alter.text
        print(alter_text)
        self.assertEqual(alter_text,'登录失败，请检查您的用户名或密码是否填写正确。','test01_login用例执行失败')



    def tearDown(self):
        self.driver.quit()
if __name__=="__main__":
    unittest.main()