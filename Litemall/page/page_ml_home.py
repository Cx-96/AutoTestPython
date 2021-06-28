#@Time：2021/6/11 19:26
#@File: page_ml_home.py
#@Software: PyCharm
from time import sleep

from base.base import Base
import page

class PageMlHome(Base):
    # 点击我的进入个人页面
    def page_to_home(self):
        self.base_click(page.ml_home)

    # 点击全部订单
    def page_click_all_order(self):
        self.base_click(page.ml_all_order)
    # 点击待付款
    def page_click_obligation(self):
        self.base_click(page.ml_obligation)
    # 点击去支付
    def page_go_pay(self):
        sleep(0.5)
        self.base_click(page.ml_go_pay_btn)
    # 选择支付方式
    def page_choose_pay(self):
        self.base_click(page.ml_alipay)
    # 点击支付
    def page_click_pay_btn(self):
        self.base_click(page.ml_pay_btn)

    # 获取支付信息
    def page_get_pay_info(self):
        sleep(1)
        return self.base_get_text(page.ml_pay_info)

    # 组合业务方法
    def page_ml_pay(self):
        self.page_to_home()
        self.page_click_all_order()
        self.page_click_obligation()
        self.page_go_pay()
        self.page_choose_pay()
        self.page_click_pay_btn()
