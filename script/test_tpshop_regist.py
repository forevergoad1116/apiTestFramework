# 导包
import json

import requests
import unittest

# 创建测试函数继承unittest.TestCase
from parameterized import parameterized

import app
from api.tpshop_regist_api import TestTpshop_regist_Api
from utils import read_regist_data, assert_common


class TestTpshopRegist(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 实例化封装的注册接口类
        cls.regist_api = TestTpshop_regist_Api()
        # 实例化session
        # cls.session = requests.Session()

    # @classmethod
    # def tearDownClass(cls):
    #     # 关闭session
    #     if cls.session !=None:
    #         cls.session.close()

    def setUp(cls):
        # # 实例化封装的注册接口类
        # cls.regist_api = TestTpshop_regist_Api()
        # 实例化session
        cls.session = requests.Session()

    def tearDown(cls):
        # 关闭session
        if cls.session != None:
            cls.session.close()
    # 定义登录数据文件的路径
    filepath = app.BASE_DIR + "/data/regist.json"

    @parameterized.expand(read_regist_data(filepath))
    def test01_regist_success(self, case_name, request_body, http_code, message):
        # 发送获取验证码的接口请求
        response = self.regist_api.get_verify(self.session)
        # 断言验证码的返回数据
        self.assertIn("image", response.headers.get("Content-Type"))
        # 发送注册接口请求
        # data = request_body
        response = self.regist_api.regist(request_body, self.session)

        # 打印登录结果
        print("注册的结果为：", response.json())
        # 断言注册
        self.assertIn(message, response.json().get("msg"))


