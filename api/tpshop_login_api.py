# 导包
import requests

# 定义封装的类
class TestTpshopApi:

    def __init__(self):
        # 验证码URL和登录URL
        self.verify_url = "http://localhost/index.php?m=Home&c=User&a=verify"
        self.login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"

    # 封装获取验证码
    def get_verify(self, session):
        # 发送获取验证码请求并直接return返回的对象
        return session.get(url=self.verify_url)

    # 封装登录接口
    def login(self, data, session):
        # 发送登录接口请求，并直接return
        return session.post(url=self.login_url, data=data)
