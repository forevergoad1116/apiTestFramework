# 导包
import requests

# 定义封装的类
class TestTpshop_regist_Api:

    def __init__(self):
        # 验证码URL和注册URL
        self.regist_url = "http://localhost/index.php/Home/User/reg.html"
        self.verify_url = "http://localhost/index.php/Home/User/verify/type/user_reg.html"

    # 封装获取验证码
    def get_verify(self, session):
        # 发送获取验证码请求并直接return返回的对象
        return session.get(url=self.verify_url)

    # 封装注册接口
    def regist(self, data, session):
        # 发送注册接口请求，并直接return
        return session.post(url=self.regist_url, data=data)
