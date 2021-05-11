from page.home_page import HomePage
from page.login_page import LoginPage
from page.me_page import MyPage
from page.register_page import RegisterPage


# 所有page的入口类
class Page:
    def __init__(self, driver):
        # 定义同一个变量 保证后面的若干对象使用同一个driver
        self.driver = driver

    # @property将方法变成属性调用方式
    @property
    def home(self):
        return HomePage(self.driver)

    @property
    def login(self):
        return LoginPage(self.driver)

    @property
    def register(self):
        return RegisterPage(self.driver)

    @property
    def me(self):
        return MyPage(self.driver)