#@Time：2021/6/11 9:28
#@File: get_driver.py
#@Software: PyCharm
from selenium import webdriver


class GetDriver:
    # 声明变量
    __web_driver = None

    # 获取driver
    @classmethod
    def get_web_driver(cls, url):
        # 判断driver是否为空
        if cls.__web_driver == None:
            cls.__web_driver = webdriver.Chrome()
            cls.__web_driver.maximize_window()
            cls.__web_driver.get(url)
        return cls.__web_driver

    # 退出driver
    @classmethod
    def quit_web_driver(cls):
        # 判断driver不为空
        if cls.__web_driver:
            cls.__web_driver.quit()
            cls.__web_driver = None
