from time import sleep

import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


# 搜索页面
class SearchPage(BaseAction):
    # 输入框
    keyword_edit_text = By.ID, "com.yunmall.lc:id/text_search_keyword"
    # 搜索按钮
    search_button = By.ID, "com.yunmall.lc:id/button_search"
    # 删除按钮
    search_del_button = By.ID, 'com.yunmall.lc:id/search_del'

    # 输入关键字
    @allure.step(title="搜索页面 输入 关键字")
    def input_keyword(self, text):
        self.input(self.keyword_edit_text, text)

    # 点击搜索
    @allure.step(title="搜索页面 点击 搜索")
    def click_search(self):
        self.click(self.search_button)

    # 点击返回
    @allure.step(title="搜索页面 点击 返回")
    def press_back(self):
        sleep(1)
        self.driver.press_keycode(4)

    # 判断搜索文字是否在 最近搜索中
    @allure.step(title="搜索页面 判断是否存在指定文字")
    def is_keyword_exist(self, keyword):
        xpath = By.XPATH, "//*[@resource-id='com.yunmall.lc:id/keyayout']/*/*[@text='{}']".format(keyword)
        return self.is_feature_exist(xpath)

    # 点击删除搜索记录
    @allure.step(title="搜索页面 点击 删除搜索记录")
    def click_search_del(self):
        self.click(self.search_del_button)
