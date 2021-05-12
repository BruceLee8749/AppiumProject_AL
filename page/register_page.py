from selenium.webdriver.common.by import By

from base.base_action import BaseAction


# 登录注册页面1
class RegisterPage(BaseAction):
    # 已有账号 去登录按钮元素
    login_button = By.XPATH, '//*[@text="已有账号，去登录"]'

    # 点击 已有账号，去登录按钮元素
    def click_login(self):
        self.click(self.login_button)
