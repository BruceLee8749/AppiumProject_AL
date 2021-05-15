from time import sleep

import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestAddress:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        sleep(3)
        self.driver.quit()

    data_list = analyze_file('address_data.yaml', 'test_add_address')

    @pytest.mark.parametrize('args', data_list)
    def test_add_address(self, args):
        name = args['name']
        phone = args['phone']
        info = args['info']
        post_code = args['post_code']
        toast = args['toast']
        # 登录
        self.page.home.login_if_not(self.page)
        # 用户信息页面上 点击设置
        self.page.me.click_setting()
        # 设置页面上 点击地址管理
        self.page.setting.click_address_list()
        # 地址管理上  点击新增地址
        self.page.address_list.click_add_address()
        # 新增地址上 输入收件人
        self.page.edit_address.input_name(name)
        # 输入手机号
        self.page.edit_address.input_phone(phone)
        # 输入所在地区
        self.page.edit_address.choose_region()
        # 输入详细地址
        self.page.edit_address.input_info(info)
        # 输入邮编
        self.page.edit_address.input_post_code(post_code)
        # 点击设置默认按钮 有坑：如果此时界面有输入法弹窗会定位不到该元素 前置代码设置：使用Unicode键盘
        self.page.edit_address.click_default()
        # 点击保存
        self.page.edit_address.click_save()
        # 如果yaml文件中的toast为空表示: 信息填写正确情况
        if toast is None:
            # 判断是否和获取的默认地址文本一致 -->一致 则 地址添加成功
            assert self.page.address_list.get_default_receipt_name_text() == "{}  {}".format(name,
                                                                                             phone), '保存不成功，默认姓名+电话与输入信息不符'
        else:
            # 判断弹出的toast能否找到
            """
            一定要注意有特殊字符的情况！用了特殊字符后很容易出现和你输入的不是同一个字符的情况，导致assert比对失败，更坑比的是没有提示。
            解决方法：用contains 然后 输入部分纯中文内容进去 就不会错了
            """
            print(self.page.edit_address.get_toast_text('收件人姓名'))
            assert self.page.edit_address.is_toast_exist(toast), '保存不成功，toast内容和预期不符'
