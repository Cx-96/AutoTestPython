#@Time：2021/6/11 9:24
#@File: page_ml_select.py
#@Software: PyCharm
from time import sleep
from base.base import Base
import page

class PageMlSelect(Base):
    # 进入精选页面
    def page_into_select(self):
        self.base_click(page.ml_select)

    # 点击搜索框
    def page_click_search(self):
        self.base_click(page.ml_search)

    # 搜索框内输入文字并点击查询
    def page_input_keyword(self, keyword):
        self.base_input(page.ml_search_box, keyword)
        self.base_press_enter(page.ml_search_box)

    # 点击搜索到的商品进入详情页
    def page_click_goods(self):
        sleep(0.5)
        self.base_click(page.ml_goods)

    # 进入商品详情页点击加入购物车,确认加入购物车
    def page_click_add_cart(self):
        self.base_click(page.ml_add_cart)
        sleep(0.5)
        self.base_click(page.ml_confirm_add_cart)

    # 点击详情页购物车按钮进入购物车页面
    def page_click_goods_to_cart(self):
        self.base_click(page.ml_goods_to_cart)

    # 获取购物车页面商品名称
    def page_get_goodsname(self):
        return self.base_get_text(page.ml_goodsname)


    # 组合业务方法：测试脚本层调用
    def page_ml_seacrh(self,keyword):
        self.page_into_select()
        self.page_click_search()
        self.page_input_keyword(keyword)
        self.page_click_goods()
        self.page_click_add_cart()
        self.page_click_goods_to_cart()
        self.page_get_goodsname()

# t=PageMlSeletc(Base)
# t.page_ml_seacrh('电子')