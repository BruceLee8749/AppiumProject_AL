from time import sleep

from base.base_driver import init_driver
from page.page import Page


class TestShopCart:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        sleep(10)
        self.driver.quit()

    def test_add_shop_cart(self):
        # 首页，如果没有登录就登录
        self.page.home.login_if_not(self.page)
        # 首页—分类
        self.page.home.click_category()
        # 分类—商品列表页面
        self.page.category_page.click_goods_list()
        # 商品类表页面—商品详情页面
        self.page.goods_list.click_goods()
        # 商品详情页面—购买商品页面
        self.page.goods_detail.click_add_shop_cart()
        
