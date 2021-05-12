from selenium.webdriver.common.by import By


# 关于百年奥莱 页面
from base.base_action import BaseAction


class AboutPage(BaseAction):
    # 版本更新按钮
    update_button = By.XPATH, '//*[@text="版本更新"]'

    # 点击版本 更新
    def click_update(self):
        self.click(self.update_button)
