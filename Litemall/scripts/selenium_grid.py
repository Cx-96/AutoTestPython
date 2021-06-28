#@Time：2021/6/11 9:25
#@File: selenium_grid.py
#@Software: PyCharm
from time import sleep
from selenium import webdriver

# driver =webdriver.Edge()

cap={
    "browserName":"chrome",
    "version":"",
    "platform":"WINDOWS"
}

driver=webdriver.Remote('http://127.0.0.1:4444/wd/hub',cap)

driver.get('http://www.baidu.com')

driver.find_element_by_id('kw').send_keys('python')

driver.find_element_by_id('su').click()
sleep(3)
driver.quit()
