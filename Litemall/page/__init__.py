# @Time：2021/6/11 9:16
# @File: __init__.py.py
# @Software: PyCharm
from selenium.webdriver.common.by import By

'''以下数据为商城登录、后台管理url'''
# 商城登录url
url_ml = 'http://192.168.1.10:6255/#/login'
# 后台管理url
url_mis = ''

'''以下数据为商城模块配置数据'''
# 用户名
ml_username = (By.CSS_SELECTOR, '[type="text"]')
# 密码
ml_password = (By.CSS_SELECTOR, '[type="password"]')
# 登录按钮
ml_login_btn = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/button')
# 昵称
ml_nickname = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[2]')
# 精选
ml_select = (By.XPATH, '//*[@id="app"]/div[3]/div[1]/div[1]/i')
# 购物车页
ml_cart = (By.XPATH, '//*[@id="app"]/div[3]/div[3]/div[1]/i')
# 加入购物车按钮
ml_add_cart = (By.XPATH, '//*[@id="app"]/div[2]/div[5]/button[1]')
# 确认加入购物车按钮
ml_confirm_add_cart = (By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[3]/div[3]/button[1]')
# 商品详情页购物车按钮
ml_goods_to_cart = (By.XPATH, '//*[@id="app"]/div[2]/div[5]/div[1]/div')
# 商品名称
ml_goodsname = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div[1]')
# 结算按钮
ml_jiesuan_btn = (By.XPATH, '//*[@id="app"]/div[2]/div[3]/div/button')
# 提交订单
ml_submit_order = (By.XPATH, '//*[@id="app"]/div[2]/div[5]/div/button')
# 我的
ml_home = (By.XPATH, '//*[@id="app"]/div[3]/div[4]/div[1]/i')
# 搜索
ml_search = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[1]/div/div')
# 搜索输入框
ml_search_box = (By.CSS_SELECTOR, '[placeholder="请输入商品名称"]')
# 商品
ml_goods = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[1]/div/div')
# 选择支付方式文本
ml_pay_way = (By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]')
# 选择支付宝支付
ml_alipay = (By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[2]/div/div[1]/div[2]/div/div/i')
# 支付订单按钮
ml_pay_btn=(By.XPATH,'//*[@id="app"]/div[2]/button')
# 获取支付结果信息
ml_pay_info=(By.XPATH,'/html/body/div[3]/div[1]/div')
# 待付款去支付
ml_go_pay_btn = (By.XPATH, '//*[@id="app"]/div[2]/div/div[2]/div[2]/div/div[1]/div[3]/div/button[2]')
# 全部订单
ml_all_order=(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[1]/div/div[2]/a')
# 待付款
ml_obligation=(By.XPATH,'//*[@id="app"]/div[2]/div/div[1]/div/div[2]')
# //*[@id="app"]/div[2]/div/div[1]/div/div[2]/span
# //*[@id="app"]/div[2]/div/div[1]/div/div[2]