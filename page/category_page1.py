import random

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


# 首页 分类页面（家纺）
class CategoryPage(BaseAction):
    # 商品列表 按钮 (默认在家纺中寻找)
    goods_list_button = By.ID, 'com.yunmall.lc:id/iv_img'

    # 随机点击首页家纺中某个元素
    def click_goods_list(self):
        goods_lists = self.find_elements(self.goods_list_button)
        goods_list_count = len(goods_lists)
        # 随机选择一个
        goods_lists_index = random.randint(0, goods_list_count - 1)
        goods_lists[goods_lists_index].click()
        # goods_lists[11].click()
        print("当前家纺栏中共有{}个商品元素".format(goods_list_count))
        print('现在点击的是第{}个商品元素'.format(goods_lists_index))
        # print('现在点击的是第{}个商品元素'.format(11))