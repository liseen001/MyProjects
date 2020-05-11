# --*utf-8*--
from selenium.webdriver.common.by import By
import time
def loginout(driver):
    driver.find_element(By.XPATH,'//li/a/span[@class="user-name"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH,'//a[text()="退出"]').click()
    time.sleep(1)
    driver.quit()




