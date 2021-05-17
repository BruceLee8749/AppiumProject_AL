import random
import time

import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


# 购买商品页面
class GoodsDetailPage(BaseAction):
    # 加入购物车 按钮
    add_shop_card_button = By.ID, 'com.yunmall.lc:id/btn_add_to_shopping_cart'

    # 确认按钮
    commit_button = By.XPATH, '//*[@text = "确认"]'

    # 商品标题
    goods_title_text_view = By.ID, 'com.yunmall.lc:id/tv_product_title'
    # 购物车图标按钮
    shop_cart_button = By.ID, 'com.yunmall.lc:id/btn_shopping_cart'

    # 点击 加入购物车 按钮
    @allure.step(title='购买商品页面 加入购物车')
    def click_add_shop_cart(self):
        self.click(self.add_shop_card_button)

    # 判断当前页面是否有 确认按钮
    @allure.step(title='购买商品页面 判断是否有确认按钮')
    def if_commit_exists(self):
        return self.is_feature_exist(self.commit_button)

    # 点击 确认
    @allure.step(title='购买商品页面 点击确认按钮')
    def click_commit(self):
        self.click(self.commit_button)

    # 获取分类文本字符串 按 空格 分割组成列表
    def get_choose_spec(self, text):
        # 获取文本中 请选择后面 第一个词
        return text.split(" ")[1]

    # 选择商品属性 并添加购物车
    @allure.step(title='购买商品页面 选择商品规格')
    def click_spec(self):
        if self.if_commit_exists():
            while True:
                # 不断点击确认 查看toast后面内容
                self.click_commit()
                # 如果还有确认按钮 就点击确认按钮 否则直接短路 不用再判断“请选择toast”是否存在
                if self.if_commit_exists() and self.is_toast_exist("请选择"):
                    # 请选择 颜色分类 规格
                    spec_name = self.get_choose_spec(self.get_toast_text("请选择"))
                    # 请选择后第一个属性（例如：驼色）
                    spec_feature = By.XPATH, "//*[@text='{}']/../*[2]/*[1]".format(spec_name)
                    self.click(spec_feature)
                    time.sleep(1)
                else:
                    break

    # 获取商品标题
    def get_goods_title_text(self):
        return self.get_text(self.goods_title_text_view)

    # 点击购物车图标 查看已购买的商品列表
    def click_shop_cart(self):
        self.click(self.shop_cart_button)

    # 通过商品标题 判断商品在不在已购买的购物车列表中
    def is_goods_title_exist(self, title):
        title_xpath = By.XPATH, '//*[@text="{}"]'.format(title)
        return self.is_feature_exist(title_xpath)
