from time import sleep

from base.base_driver import init_driver  # 按道理说这样导入语法没错。但是但是但是，需要在当前文件夹中建立一个__init__.py文件
import sys

sys.path.append('./base')


class TestLogin:
    def setup(self):
        # 务必保证后面的对象使用同一个driver
        self.driver = init_driver()

    def teardown(self):
        sleep(10)
        self.driver.quit()

    def test_login(self):
        print(sys.path)
        pass
