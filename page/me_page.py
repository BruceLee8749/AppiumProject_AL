from selenium.webdriver.common.by import By

from base.base_action import BaseAction


# 个人信息 页面
class MyPage(BaseAction):
    # 昵称
    nick_name_text_view = By.ID, 'com.yunmall.lc:id/tv_user_nikename'

    def get_nick_name_text(self):
        print('是否打印get_text')
        return self.get_text(self.nick_name_text_view)

    # 左上角 设置按钮
    setting_button = By.ID, 'com.yunmall.lc:id/ymtitlebar_left_btn_image'

    # 点击 设置按钮
    def click_setting(self):
        self.click(self.setting_button)
