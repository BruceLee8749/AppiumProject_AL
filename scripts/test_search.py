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
        # 判断当前页面是否存在商品
        no_search_goods_flag = self.page.search_page.if_search_goods_exists()
        # 在搜索结果页点击返回 到 搜索页面
        self.page.search_page.press_back()
        # 如果能够搜索到商品 才去判断
        if not no_search_goods_flag:
            # 判断搜索文字是否在 最近搜索中
            assert self.page.search_page.is_keyword_exist("嘿嘿嘿")

    @pytest.mark.skip
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