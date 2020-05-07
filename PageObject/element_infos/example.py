# -*- coding utf-8 -*-
import os
from selenium import webdriver
from PageObject.common.config_utils import conf
from PageObject.common.browser import browser
from PageObject.common.base_page import BasePage

e=browser.get_default_driver
url=conf.zend_path
e.get(url)
e.back()