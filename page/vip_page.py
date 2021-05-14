from selenium.webdriver.common.by import By

from base.base_action import BaseAction


# 加入超级vip页面 该页面为H5网页（由于apk有问题暂时略过）  如何获取当前页面url暂时不会。后期来解决。
# 真几把坑。apk需要在源码中加入一些语句，开启调试模式，否则driver.contexts 获取不到 webView无法切入
class VipPage(BaseAction):
    # 邀请码 输入框
    invite_edit_text = By.XPATH, "//*[@type='tel']"
    # 立即成为会员 按钮
    be_vip_button = By.XPATH, '//input[@value="立即成为会员"]'

    # 输入邀请码
    def input_invite(self, text):
        self.input(self.invite_edit_text, text)

    # 点击立即成为会员
    def click_be_vip(self):
        self.click(self.be_vip_button)
