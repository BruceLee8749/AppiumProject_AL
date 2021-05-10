from page.home_page import HomePage
from page.login_page import LoginPage
from page.register_page import RegisterPage


# 所有page的入口类
class Page:
    def __init__(self, driver):
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
