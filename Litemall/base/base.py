#@Time：2021/6/11 9:19
#@File: base.py
#@Software: PyCharm
import allure
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from tools.get_log import GetLog

log = GetLog.get_logger()

class Base:
    # 初始化driver
    def __init__(self, driver):
        log.info('正在初始化driver: {}'.format(driver))
        self.driver = driver

    # 查找 方法封装
    def base_find_element(self, loc, timeout=30, poll=0.5):
        log.info('正在查找元素: {}'.format(loc))
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 输入 方法封装
    def base_input(self, loc, value):
        # 获取元素
        el = self.base_find_element(loc)
        # 清空操作
        log.info('正在对{}元素进行清空操作'.format(loc))
        el.clear()
        # 输入操作
        log.info('正在对{}元素进行输入操作'.format(loc))
        el.send_keys(value)

    # 点击 方法封装
    def base_click(self, loc):
        log.info('正在对{}元素进行点击操作'.format(loc))
        self.base_find_element(loc).click()

    # 获取 元素文本
    def base_get_text(self, loc):
        log.info('正在对{}元素获取文本操作，获取的文本值为{}'.format(loc, self.base_find_element(loc).text))
        return self.base_find_element(loc).text

    # 截图
    def base_get_img(self):
        log.error('断言出错，正在执行截图操作操作')
        self.driver.get_screenshot_as_file('../image/err.png')
        log.error('断言出错，正在将错误图片写入报告')
        self.__base_write_img()

    # 将图片写入报告方法(私有)
    def __base_write_img(self):
        # 获取图片文件流
        with open('../image/err.png', 'rb') as f:
            file = f.read()
            # 调用allure.attach附加方法
            allure.attach(file, '错误原因：', allure.attachment_type.PNG)

    #enter键封装
    def base_press_enter(self,loc):
        el=self.base_find_element(loc)
        el.send_keys(Keys.ENTER)

