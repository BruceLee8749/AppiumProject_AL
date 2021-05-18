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
    """新增地址测试"""
    @pytest.mark.parametrize('args', data_list)
    def test_add_address(self, args):
        name = args['name']
        phone = args['phone']
        info = args['info']
        post_code = args['post_code']
        toast = args['toast']
        # 进入 地址管理页面
        self.page.enter_address_manager(self.page)
        # 地址管理上  点击新增地址
        self.page.address_list.click_add_address()
        # 输入 地址信息
        self.page.edit_address.add_new_address_group(name, phone, info, post_code, True)
        # 如果yaml文件中的toast为空表示: 信息填写正确情况
        if toast is None:
            # 判断是否和获取的默认地址文本一致 -->一致 则 地址添加成功
            assert self.page.address_list.get_default_receipt_name_text() == "{}  {}".format(name,
                                                                                             phone), '保存不成功，默认姓名+电话与输入信息不符'
        else:
            # 判断弹出的toast能否找到
            """
            一定要注意有特殊字符的情况！用了特殊字符后很容易出现和你输入的不是同一个字符的情况，导致assert比对失败，更坑比的是没有提示。
            解决方法：用contains 然后 只输入部分纯中文内容进去
            """
            assert self.page.edit_address.is_toast_exist(toast), '保存不成功，toast内容和预期不符'

    """编辑地址测试"""
    def test_edit_address(self):
        # 进入 地址管理页面
        self.page.enter_address_manager(self.page)
        # 如果默认地址存在(页面第一个地址始终为默认地址)
        if not self.page.address_list.is_default_feature_exist():
            print('不存在默认地址，添加默认地址')
            # 地址管理上  点击新增地址
            self.page.address_list.click_add_address()
            # 输入正确的一组地址
            self.page.edit_address.add_new_address_group("itheima", "13836668889", "二单元33幢25层205室", 210000, True)
        else:
            # 点击默认地址开始修改默认地址中的值
            self.page.address_list.click_default_address()
            # 重新输入地址信息
            self.page.edit_address.add_new_address_group("传智播客", "18836668889", "五单元33幢25层205室", 214000, False)
            # 断言是否页面出现 保存成功
            assert self.page.address_list.is_toast_exist("保存成功")

    """删除地址测试"""
    def test_delete_address(self):
        # 从首页 进入 地址管理页面
        self.page.enter_address_manager(self.page)
        # 判断 是否有地址可以删除 没有就自动添加一个
        if not self.page.address_list.is_default_feature_exist():
            # 地址管理上  点击新增地址
            self.page.address_list.click_add_address()
            self.page.edit_address.add_new_address_group("博学谷", "16636668889", "一单元33幢25层205室", 213000, True)
        # 判断是否有地址
        assert self.page.address_list.is_default_feature_exist(), '地址列表为空，没有添加成功，请检查是否有地址'
        # 假定删除 10次（页面最多添加10个地址）
        for i in range(10):
            # 点击编辑
            self.page.address_list.click_edit()
            # 判断删除按钮是否存在 没有就break 存在再去删除
            if not self.page.address_list.is_delete_exist():
                break
            # 点击删除
            self.page.address_list.click_delete()
            # 点击确认
            self.page.address_list.click_commit()
        # 断言是否删除完了
        print("默认元素是否存在",self.page.address_list.is_default_feature_exist())
        assert not self.page.address_list.is_default_feature_exist(),'还没删除完，删除有问题'
