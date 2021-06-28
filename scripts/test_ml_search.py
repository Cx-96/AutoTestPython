#@Time：2021/6/11 9:27
#@File: test_ml_search.py
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
class TestMlCart:
    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_web_driver(page.url_ml)
        # 通过统一入口类
        self.page_in=PageIn(driver)
        # 获取PageMlLogin对象并调用成功登录依赖方法
        self.page_in.page_get_PageMlLogin().page_ml_login(username='user123',password='user123')
        # 获取PageMlSelect对象
        self.seacrh=self.page_in.page_get_PageMlSelect()

    # 结束
    def teardown_class(self):
        # 调用关闭driver
        sleep(1)
        GetDriver.quit_web_driver()

    # 测试业务方法
    @pytest.mark.parametrize('keyword,expect',read_yaml('ml_search.yaml'))
    def test_ml_order(self,keyword, expect):
        self.seacrh.page_ml_seacrh(keyword)
        try:
            # 断言
            assert expect == self.seacrh.page_get_goodsname()
        except Exception as e:
            log.error('断言出错，错误信息: {}'.format(e))
            # 输出错误
            print('错误原因：',e)
            # 截图
            self.seacrh.base_get_img()
            # 抛出异常
            raise




if __name__ == '__main__':
    pytest.main(['-vs', 'test_ml_search.py'])
    os.system('allure generate report -o ../report --clean')