# 编写读取注册数据的函数
import json

import app


def read_regist_data(filepath):
    # 打开数据文件
    with open(filepath, mode='r', encoding='utf-8') as f:
        # 使用json加载数据文件为json格式
        jsonData = json.load(f)
        # 遍历json格式的数据文件，并把数据处理成列表元组形式（[(),(),()]）添加到空列表中
        result_list = list()
        for login_data in jsonData: #type:dict
            # 把每一组登录数据的所有values转化为元组形式，并添加到空列表当中
            result_list.append(tuple(login_data.values()))

    # print("查看读取的登录数据为：", result_list)
    return result_list
def assert_common(self, http_code, message, response):
    self.assertEqual(http_code, response.status_code)
    self.assertIn(message, response.json().get("message"))