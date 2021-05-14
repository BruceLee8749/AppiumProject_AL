from time import sleep

import pytest
from appium.common.exceptions import NoSuchContextException
from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page
class TestAddress:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        pass

    def test_add_address(self):
        # 登录
        self.page.home.login_if_not(self.page)
        # 用户信息页面上 点击设置
        self.page.me.click_setting()
        # 设置页面上 点击地址管理
        self.page.setting.click_address_list()
        # 地址管理上  点击新增地址
        self.page.address_list.click_add_address()
        # 新增地址上 输入收件人
        self.page.edit_address.input_name('zhangsan')
        # 输入手机号
        self.page.edit_address.input_phone('18888888888')
        # 输入所在地区

        # 输入详细地址
        self.page.edit_address.input_info('江苏省苏州市松泽家园八区36栋')
        # 输入邮编
        self.page.edit_address.input_post_code('210000')
        # 点击设置默认按钮 有坑：如果此时界面有输入法弹窗会定位不到该元素
        self.page.edit_address.click_default()
        # 点击保存