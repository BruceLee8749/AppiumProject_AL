import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


# 网站主页面
class HomePage(BaseAction):
    # 按钮 “我”
    me_button = By.ID, 'com.yunmall.lc:id/tab_me'
    # 分类元素
    category_button = By.ID, 'com.yunmall.lc:id/tab_category'
    # 主页上的购物车
    shop_cart_button = By.ID, "com.yunmall.lc:id/tab_shopping_cart"

    # 点击 “我” 按钮
    @allure.step(title='主页 点击 我')
    def click_me(self):
        self.click(self.me_button)

    # 点击分类
    @allure.step(title='主页 点击 分类')
    def click_category(self):
        self.click(self.category_button)

    # 判断当前页面是否登录，未登录--> 直接点击登录按钮 已登录--> 结束方法  用到很多页面 需要传page对象
    @allure.step(title='主页 如果没登录 点击登录')
    def login_if_not(self, page):
        # 点击 我
        self.click_me()
        # 查看包名和界面名字：如果未登录
        if self.driver.current_activity == 'com.yunmall.ymctoc.ui.activity.LogonActivity':
            # 点击底部已有账号，去登录
            page.register.click_login()
            # 输入用户名
            page.login.input_username('itheima_test')
            # 输入密码
            page.login.input_password('itheima')
            # 点击登录
            page.login.click_login()
        else:
            # 如果已经登录 直接返回结束
            return  

    @allure.step(title='主页 点击 购物车')
    def click_shop_cart(self):
        self.click(self.shop_cart_button)
