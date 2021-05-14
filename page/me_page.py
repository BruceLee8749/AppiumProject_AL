from time import sleep

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


# 个人信息 页面
class MyPage(BaseAction):
    # 昵称
    nick_name_text_view = By.ID, 'com.yunmall.lc:id/tv_user_nikename'
    # 左上角 设置按钮
    setting_button = By.ID, 'com.yunmall.lc:id/ymtitlebar_left_btn_image'
    # 加入超级vip按钮
    be_vip_button = By.XPATH, '//*[@text="加入超级VIP"]'

    # 获取昵称文本
    def get_nick_name_text(self):
        print('是否打印get_text')
        return self.get_text(self.nick_name_text_view)

    # 点击 设置按钮
    def click_setting(self):
        self.click(self.setting_button)

    # 滑动查找 并点击超级vip按钮
    def click_be_vip(self):
        self.find_element_with_scroll(self.be_vip_button).click()