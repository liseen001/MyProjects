# -*- coding utf-8 -*-
'''这是新增产品最后一个添加产品并提交表单的函数封装'''
from  selenium.webdriver.common.by import By
def add_product(driver):
    '''这是一个添加产品的用例，添加产品的最后步骤'''
    driver.find_element(By.XPATH, '//input[@id="name"]').send_keys('六组第二个产品')  # 产品名称
    driver.find_element(By.XPATH, '//input[@id="code"]').send_keys('95278')  # 产品代号

    driver.find_element(By.XPATH, '//div[@id="line_chosen"]').click()  # 添加产品线
    driver.find_element(By.XPATH, '//div[@id="line_chosen"]/div/ul/li[@data-option-array-index="1"]').click()

    driver.find_element(By.XPATH, '//div[@id="PO_chosen"]').click()  # 产品负责人
    driver.find_element(By.XPATH, '//div[@id="PO_chosen"]/div/ul/li[@data-option-array-index="1"]').click()

    driver.find_element(By.XPATH, '//div[@id="QD_chosen"]').click()  # 测试负责
    driver.find_element(By.XPATH, '//div[@id="QD_chosen"]/div/ul/li[@data-option-array-index="1"]').click()

    driver.find_element(By.XPATH, '//div[@id="RD_chosen"]').click()  # 发布负责人
    driver.find_element(By.XPATH, '//div[@id="RD_chosen"]/div/ul/li[@data-option-array-index="1"]').click()

    driver.find_element(By.XPATH, '//select[@id="type"]').click()
    driver.find_element(By.XPATH, '//select[@id="type"]/option[@value="normal"]').click()

    frame = driver.find_element(By.XPATH, '//iframe[@class="ke-edit-iframe"]')  # iframe 跳入跳出
    driver.switch_to.frame(frame)  # 移动到这个frame上
    driver.find_element(By.XPATH, '//body[@class="article-content"]').click()
    driver.find_element(By.XPATH, '//body[@class="article-content"]').send_keys('这是咱第六组第二个产品项目')
    driver.switch_to.default_content()
    driver.find_element(By.XPATH, '//tr/td/button[@id="submit"]').submit()  # 保存提交