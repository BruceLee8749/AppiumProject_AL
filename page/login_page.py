from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):
    # 用户名元素
    username_edit_text = By.ID, 'com.yunmall.lc:id/logon_account_textview'
    # 密码元素
    password_edit_text = By.ID, 'com.yunmall.lc:id/logon_password_textview'
    # 登录按钮元素
    login_button = By.ID, 'com.yunmall.lc:id/logon_button'

    # 输入用户名
    def input_username(self, text):
        self.input(self.username_edit_text, text)

    # 输入密码
    def input_password(self, text):
        self.input(self.password_edit_text, text)

    # 点击登录
    def click_login(self):
        self.click(self.login_button)
