# @Time：2021/6/11 9:21
# @File: page_in.py
# @Software: PyCharm
from page.page_ml_login import PageMlLogin
from page.page_ml_cart import PageMlCart
from page.page_ml_select import PageMlSelect
from page.page_ml_home import PageMlHome

class PageIn:
    def __init__(self, driver):
        self.driver = driver

    # 获取PageMlLogin对象
    def page_get_PageMlLogin(self):
        return PageMlLogin(self.driver)

    # 获取PageMlSelect对象
    def page_get_PageMlSelect(self):
        return PageMlSelect(self.driver)

    # 获取PageMlOrder对象
    def page_get_PageMlCart(self):
        return PageMlOrder(self.driver)

# 获取PageMlOrder对象
    def page_get_PageMlHome(self):
        return PageMlHome(self.driver)