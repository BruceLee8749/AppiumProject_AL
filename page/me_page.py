from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MyPage(BaseAction):
    # 昵称
    nick_name_text_view = 'com.yunmall.lc:id/tv_user_nikename'

    def get_nick_name_text(self):
        self.get_text(self.nick_name_text_view)
