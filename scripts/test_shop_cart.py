from time import sleep

import allure
import pytest

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
            sleep(2)
            allure.attach(self.driver.get_screenshot_as_png(), "当前没有商品截图", allure.attachment_type.PNG)
            print('当前页面没有商品，请重新选择！！！')
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
                
            """
            # 商品详情 - 已买商品列表页面
            self.page.goods_detail.click_shop_cart()
            sleep(2)
            allure.attach(self.driver.get_screenshot_as_png(), "测试商品截图", allure.attachment_type.PNG)
            assert self.page.goods_detail.is_goods_title_exist(goods_title)
            # assert self.page.goods_detail.is_toast_exist('成功加入购物车') 显示出来但是获取不到该toast

    def test_shop_cart_price(self):
        # 首页，如果没有登录就登录
        self.page.home.login_if_not(self.page)
        # 首页，点击购物车
        self.page.home.click_shop_cart()
        # 点击全选
        self.page.shop_cart.click_select_all()
        # 记录总价
        all_price = self.page.shop_cart.get_all_price()
        # 记录单价
        price = self.page.shop_cart.get_price()
        # 点击编辑
        self.page.shop_cart.click_edit()
        # 点击加号
        self.page.shop_cart.click_add()
        # 点击完成
        self.page.shop_cart.click_commit()
        # 计算总价
        compute_result = self.page.shop_cart.get_all_price()
        # 断言 是否 计算总价 == 记录总价 + 记录单价
        print('记录总价：{} 单价：{} 计算总价：{}'.format({all_price}, {price}, {compute_result}))
        assert compute_result == all_price + price, '价格计算错误！'

    def test_del_shop_cart(self):
        # 首页，如果没有登录就登录
        self.page.home.login_if_not(self.page)
        # 首页，点击购物车
        self.page.home.click_shop_cart()
        # 如果没有商品就添加商品
        if self.page.shop_cart.is_shop_cart_empty():
            # 首页—分类
            self.page.home.click_category()
            # 分类—商品列表页面
            self.page.category_page.click_goods_list()
            # 判断当前商品详情页面是否为空
            if self.page.goods_list.if_goods_exists():
                sleep(2)
                allure.attach(self.driver.get_screenshot_as_png(), "当前没有商品截图", allure.attachment_type.PNG)
                raise Exception('当前页面没有商品，无法自动添加。请重新选择非空商品列表 或 手动添加商品到购物车！！！')
            else:
                # 商品类表页面—商品详情页面
                self.page.goods_list.click_goods()
                # 商品详情页面—购买商品页面
                self.page.goods_detail.click_add_shop_cart()
                # 选择商品属性 并添加购物车
                self.page.goods_detail.click_spec()
                # 执行2次返回操作进入首页购物车
                self.page.driver.press_keycode(4)
                sleep(2)
                self.page.driver.press_keycode(4)
        # 如果购物车里有商品就执行下列操作
        # 点击首页购物车
        self.page.home.click_shop_cart()
        # 购物车-点击全选
        self.page.shop_cart.click_select_all()
        # 点击编辑
        self.page.shop_cart.click_edit()
        # 点击删除
        self.page.shop_cart.click_delete()
        # 点击确认
        self.page.shop_cart.click_yes()
        # 断言toast删除成功
        assert self.page.shop_cart.is_toast_exist("删除成功")
        # 断言当前页面是否为空
        assert self.page.shop_cart.is_shop_cart_empty()
