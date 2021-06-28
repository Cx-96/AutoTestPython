# @Time：2021/6/11 16:49
# @File: page_ml_cart.py
# @Software: PyCharm
from base.base import Base
import page
from time import sleep
class PageMlCart(Base):
    # 进入购物车页
    def page_to_cart(self):
        self.base_click(page.ml_cart)

    # 点击结算按钮
    def page_click_pay(self):
        self.base_click(page.ml_jiesuan_btn)

    # 点击提交订单按钮
    def page_submit_order(self):
        self.base_click(page.ml_submit_order)

    # 获取支付页面中“选择支付方式”文本
    def page_get_pay_text(self):
        sleep(0.5)
        return self.base_get_text(page.ml_pay_way)

    # 组合业务方法
    def page_ml_cart(self):
        self.page_to_cart()
        self.page_click_pay()
        self.page_submit_order()
