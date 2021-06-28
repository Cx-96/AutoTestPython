#@Time：2021/6/11 9:29
#@File: read_yaml.py
#@Software: PyCharm
import os
import yaml
from config import base_path

# 定义函数
def read_yaml(filename):
    file_path=base_path+os.sep+'data'+os.sep+filename
    #定义空列表
    arr=[]
    #获取文件流
    with open(file_path,'r',encoding='utf-8') as f:
    # 遍历 调用yaml.safe_load(f).values()方法
        for datas in yaml.safe_load(f).values():
            arr.append(tuple(datas.values()))
    # 返回结果
    return arr

if __name__ == '__main__':
    print(read_yaml('ml_order.yaml'))