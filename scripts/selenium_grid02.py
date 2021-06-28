#@Time：2021/6/11 9:26
#@File: selenium_grid02.py
#@Software: PyCharm
from time import sleep
import threading
from selenium import webdriver


# 封装百度
def get_baidu(driver):
    driver.get('http://www.baidu.com')
    driver.find_element_by_id('kw').send_keys('python')
    driver.find_element_by_id('su').click()
    sleep(3)
    driver.quit()


# 封装driver
def get_driver(browser):
    # 定义空变量
    cap = None
    # 判断浏览器类型
    if browser == 'chrome':
        cap = webdriver.DesiredCapabilities.CHROME.copy()
    elif browser == 'MicrosoftEdge':
        cap = webdriver.DesiredCapabilities.EDGE.copy()
    # 修改默认平台名称
    cap["platform"] = "WINDOWS"
    return webdriver.Remote('http://127.0.0.1:4444/wd/hub', cap)


# 遍历多线程
# 定义浏览器列表
browserName = ['chrome', 'MicrosoftEdge']
# 遍历浏览器列表
for browser in browserName:
    driver = get_driver(browser)
    # 实例化线程及启动
    threading.Thread(target=get_baidu, args=(driver,)).start()
