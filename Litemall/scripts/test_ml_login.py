#@Time：2021/6/11 9:26
#@File: test_ml_login.py
#@Software: PyCharm
import os
from time import sleep
import pytest
import page
from tools.get_driver import GetDriver
from page.page_in import PageIn
from tools.read_yaml import read_yaml
from tools.get_log import GetLog

log = GetLog.get_logger()
class TestMlLogin:
    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_web_driver(page.url_ml)
        # 通过统一入口类获取PageMlLogin对象
        self.ml = PageIn(driver).page_get_PageMlLogin()

    # 结束
    def teardown_class(self):
        # 调用关闭driver
        sleep(1)
        GetDriver.quit_web_driver()

    # 测试业务方法
    @pytest.mark.parametrize('username,password,expect',read_yaml('ml_login.yaml'))
    def test_ml_login(self, username, password, expect):
        # 调用登录业务方法
        self.ml.page_ml_login(username, password)
        sleep(1)
        try:
            # 断言
            assert expect == self.ml.page_get_nickname()
        except Exception as e:
            log.error('断言出错，错误信息: {}'.format(e))
            # 输出错误
            print('错误原因：',e)
            # 截图
            self.ml.base_get_img()
            # 抛出异常
            raise




if __name__ == '__main__':
    pytest.main(['-vs', 'test_ml_login.py'])
    os.system('allure generate report -o ../report --clean')
