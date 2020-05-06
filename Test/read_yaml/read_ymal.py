# -*- coding utf-8 -*-
import os
import yaml

current_path=os.path.dirname(__file__)
yaml_path=os.path.join(current_path,'../read_yaml/test.yaml')

file=open('test.yaml','r',encoding='utf-8')

data=yaml.load(file)
print(data)

from selenium import  webdriver

foxfir_option=webdriver.FirefoxOptions()
foxfir_option.add_argument('disable-infobars')

driver=webdriver.Firefox(firefox_options=foxfir_option)