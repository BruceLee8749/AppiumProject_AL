import time
from time import sleep

import allure

from base.base_driver import init_driver
from page.page import Page


class TestShopCart:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        sleep(5)
        self.driver.quit()

    def test_add_shop_cart(self):
        # 首页，如果没有登录就登录
        self.page.home.login_if_not(self.page)
        # 首页—分类
        self.page.home.click_category()
        # 分类—商品列表页面
        self.page.category_page.click_goods_list()
        # 判断当前商品详情页面是否为空
        if self.page.goods_list.if_goods_exists():
            allure.attach("没有商品截图",self.driver.get_screenshot_as_png(),allure.attachment_type.PNG)
            print('当前页面没有商品！！！')
        else:
            # 商品类表页面—商品详情页面
            self.page.goods_list.click_goods()
            # 记录当前商品标题
            goods_title = self.page.goods_detail.get_goods_title_text()
            # 商品详情页面—购买商品页面
            self.page.goods_detail.click_add_shop_cart()
            # 选择商品属性 并添加购物车
            self.page.goods_detail.click_spec()

            """
                灵异事件：买完商品后明明有：“成功加入购物车”toast但是始终获取不到
                通过断言 成功加入购物车toast提示 来判断 购物车流程成功算是行不通
                不知道是什么鬼
                以后再来探究
                assert self.page.goods_detail.is_toast_exist('成功加入购物车')
            """
            # 商品详情 - 已买商品列表页面
            self.page.goods_detail.click_shop_cart()
            time.sleep(2)
            assert self.page.goods_detail.is_goods_title_exist(goods_title)

