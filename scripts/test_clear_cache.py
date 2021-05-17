from time import sleep

from base.base_driver import init_driver
from page.page import Page


class TestClearCache:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        sleep(5)
        self.driver.quit()

    def test_update(self):
        # 点击登录
        self.page.home.login_if_not(self.page)
        # 点击设置按钮
        self.page.me.click_setting()
        # 进入 设置界面 查找并点击清理缓存
        self.page.setting.click_cache()
        # 查找是否 含有指定toast
        assert self.page.setting.is_toast_exist('清理成功')


