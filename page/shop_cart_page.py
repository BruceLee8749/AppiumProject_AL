import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


# 购物车页面（从首页进去）
class ShopCartPage(BaseAction):
    # 全选按钮
    select_all_button = By.ID, 'com.yunmall.lc:id/iv_select_all'
    # 编辑按钮
    edit_button = By.XPATH, '//*[@text="编辑"]'
    # 完成
    commit_button = By.XPATH, '//*[@text="完成"]'
    # 加号按钮
    add_button = By.ID, 'com.yunmall.lc:id/iv_add'
    # 单价文本
    price_feature = By.ID, 'com.yunmall.lc:id/tv_price'
    # 总价
    all_price_feature = By.ID, 'com.yunmall.lc:id/tv_count_money'
    # 删除按钮
    delete_button = By.XPATH, '//*[@text="删除"]'
    # 删除后确认
    yes_button = By.XPATH, '//*[@text="确认"]'
    # 提示信息：购物车为空
    shop_cart_null = By.XPATH, '//*[contains(@text,"购物车还是空的")]'

    # 点击编辑
    @allure.step(title='首页购物车页面 点击 编辑')
    def click_edit(self):
        self.click(self.edit_button)

    # 点击全选
    @allure.step(title='首页购物车页面 点击 全选')
    def click_select_all(self):
        self.click(self.select_all_button)

    # 点击完成
    @allure.step(title='首页购物车页面 点击 完成')
    def click_commit(self):
        self.click(self.commit_button)

    # 点击 加号
    @allure.step(title='首页购物车页面 点击 加号')
    def click_add(self):
        self.click(self.add_button)

    # 获取单价
    @allure.step(title='首页购物车页面 获取 单价')
    def get_price(self):
        # 获取单价文本
        price_text = self.get_text(self.price_feature)
        # 获取价格文本中数字
        return self.deal_with_price(price_text)

    # 获取总价
    @allure.step(title='首页购物车页面 获取 总价')
    def get_all_price(self):
        # 获取总价文本
        price_text = self.get_text(self.all_price_feature)
        # 获取价格文本中数字
        return self.deal_with_price(price_text)

    # 获取人民币数字
    @allure.step(title='首页购物车页面 获取人民币数字')
    def deal_with_price(self, price):
        "示例：￥ 25.8"
        # 切片：表示从字符串第3个元素开始（包括第3个）到末尾
        return float(price[2:])

    # 点击删除
    @allure.step(title='首页购物车页面 删除商品')
    def click_delete(self):
        self.click(self.delete_button)

    # 点击确认
    @allure.step(title='首页购物车页面 确认删除')
    def click_yes(self):
        self.click(self.yes_button)

    # 判断购物车是否为空
    @allure.step(title='首页购物车页面 是否购物车为空')
    def is_shop_cart_empty(self):
        return self.is_feature_exist(self.shop_cart_null)
