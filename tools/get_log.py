#@Time：2021/6/11 9:28
#@File: get_log.py
#@Software: PyCharm
import logging.handlers
import os

from config import base_path


class GetLog:
    # 新建一个日志器的变量
    __logger=None
    # 新建获取日志器的方法
    @classmethod
    def get_logger(cls):
        # 判断日志器是否为空
        if cls.__logger==None:
            #获取日志器
            cls.__logger=logging.getLogger()
            #修改默认级别
            cls.__logger.setLevel(logging.INFO)
            log_path=base_path+os.sep+'log'+os.sep+'litemall.log'
            #获取处理器
            th=logging.handlers.TimedRotatingFileHandler(filename=log_path,
                                                         when='midnight',
                                                         interval=1,
                                                         backupCount=3,
                                                         encoding='utf-8')
            #获取格式器
            fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s %(funcName)s:%(lineno)d] - %(message)s'
            fm=logging.Formatter(fmt)
            #将格式器添加到处理器种
            th.setFormatter(fm)
            #将处理器添加到日志器中
            cls.__logger.addHandler(th)
        return cls.__logger
