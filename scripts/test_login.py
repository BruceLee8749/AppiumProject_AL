from time import sleep

from base.base_driver import init_driver


class TestLogin:
    def setup(self):
        # 务必保证后面的对象使用同一个driver
        self.driver = init_driver()

    def teardown(self):
        sleep(10)
        self.driver.quit()

    def test_login(self):

        pass
