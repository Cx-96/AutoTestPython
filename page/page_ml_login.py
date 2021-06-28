#@Time：2021/6/11 9:23
#@File: page_ml_login.py
#@Software: PyCharm
from time import sleep

from base.base import Base
import page
from tools.get_log import GetLog

log = GetLog.get_logger()


class PageMlLogin(Base):
    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.ml_username, username)

    # 输入密码
    def page_input_pwd(self, password):
        self.base_input(page.ml_password, password)

    # 点击登录按钮
    def page_click_login_btn(self):
        sleep(1)
        self.base_click(page.ml_login_btn)

    # 获取昵称封装:测试脚本层断言使用
    def page_get_nickname(self):
        return self.base_get_text(page.ml_nickname)

    # 组合业务方法：测试脚本层调用
    def page_ml_login(self, username, password):
        log.info('正在调用商城登录业务方法，用户名：{}，密码：{}'.format(username, password))
        '''调用相同页面操作步骤，跨页面暂时不考虑'''
        self.page_input_username(username)
        self.page_input_pwd(password)
        self.page_click_login_btn()