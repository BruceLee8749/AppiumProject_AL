from time import sleep

from base.base_driver import init_driver  # 按道理说这样导入语法没错。但是但是但是，需要在当前文件夹中建立一个__init__.py文件 或者sys中添加目录
from page.page import Page


class TestLogin:
    def setup(self):
        # 定义同一个变量 保证后面的若干对象使用同一个driver
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        sleep(10)
        self.driver.quit()

    # 虽然单元测试一组方法不太好，但测的是仅仅一个功能 原则可以接受
    def test_login(self):
        self.page.home.click_me()
        self.page.register.click_login()
        self.page.login.input_username('itheima_test')
        self.page.login.input_password('itheima')
        self.page.login.click_login()
        assert self.page.me.get_nick_name_text() == 'itheima_test'
