from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):
    # 我的 元素
    me_button = By.ID, 'com.yunmall.lc:id/tab_me'

    # 点击 我的
    def click_me(self):
        self.click(self.me_button)
