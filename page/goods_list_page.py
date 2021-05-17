import random

import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


# 商品详情页面
class GoodsListPage(BaseAction):
    # 商品分类下具体某类商品
    goods_button = By.ID, 'com.yunmall.lc:id/iv_element_1'

    # 如果没有就显示抱歉..文本
    goods_null_text = By.XPATH, '//*[contains(@text,"抱歉")]'

    # 判断当前页面上是否有商品
    @allure.step(title='商品详情页面 判断是否含有商品')
    def if_goods_exists(self):
        return self.is_feature_exist(self.goods_null_text)

    # 随机点击 某个商品
    @allure.step(title='商品详情页面 随机点击某个商品')
    def click_goods(self):
        goods = self.find_elements(self.goods_button)
        goods_count = len(goods)
        # 随机选择一个
        goods_index = random.randint(0, goods_count - 1)
        goods[goods_index].click()
