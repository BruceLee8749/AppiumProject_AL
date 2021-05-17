from time import sleep

import pytest

from base.base_driver import init_driver
from page.page import Page


class TestSearch:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        sleep(5)
        self.driver.quit()
    @pytest.mark.skip
    def test_search(self):
        # 首页，如果没有登录就登录
        self.page.home.login_if_not(self.page)
        # 从个人信息页 跳到 首页
        self.page.home.click_home()
        # 点击放大镜
        self.page.home.click_search()
        # 在搜索页面 输入文字
        self.page.search_page.input_keyword("嘿嘿嘿")
        # 搜索页面点击搜索 到 搜索结果页
        self.page.search_page.click_search()
        # 在搜索结果页点击返回 到 搜索页面
        self.page.search_page.press_back()
        # 判断搜索文字是否在 最近搜索中
        assert self.page.search_page.is_keyword_exist("嘿嘿嘿")

    def test_search_del(self):
        # 添加搜索记录
        # 首页，如果没有登录就登录
        self.page.home.login_if_not(self.page)
        # 从个人信息页 跳到 首页
        self.page.home.click_home()
        # 点击放大镜
        self.page.home.click_search()
        # 在搜索页面 输入文字
        self.page.search_page.input_keyword("阿迪达斯")
        # 搜索页面点击搜索 到 搜索结果页
        self.page.search_page.click_search()
        # 在搜索结果页点击返回 到 搜索页面
        self.page.search_page.press_back()
        # 删除记录
        self.page.search_page.click_search_del()
        # 判断搜索记录是否为空
        self.page.search_page.is_feature_exist("暂无搜索历史")