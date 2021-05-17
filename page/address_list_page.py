import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


# 地址管理页面
class AddressListPage(BaseAction):
    # 新增地址按钮
    add_address_button = By.ID, 'com.yunmall.lc:id/address_add_new_btn'
    # 默认的姓名+电话信息
    default_receipt_name_text_view = By.ID, 'com.yunmall.lc:id/receipt_name'
    # 默认标记
    is_default_feature = By.ID, 'com.yunmall.lc:id/address_is_default'
    # 编辑按钮
    edit_button = By.XPATH, '//*[@text="编辑"]'
    # 删除按钮
    delete_button = By.XPATH, '//*[@text="删除"]'
    # 确任按钮
    commit_button = By.XPATH, '//*[@text="确认"]'

    # 点击新增地址按钮
    @allure.step(title='地址管理页面 点击新增地址')
    def click_add_address(self):
        self.find_element_with_scroll(self.add_address_button).click()

    # 获取页面上默认地址 姓名+电话信息 (如果找的是一组元素，仍用find_element不会报错，系统会默认查找第一个)
    @allure.step(title='地址管理页面 获取收件人+电话标题')
    def get_default_receipt_name_text(self):
        return self.get_text(self.default_receipt_name_text_view)

    # 判断当前页面默认地址是否存在
    @allure.step(title='地址管理页面 判断默认标记是否存在')
    def is_default_feature_exist(self):
        return self.is_feature_exist(self.is_default_feature)  # 记得返回方法中返回的布尔值

    # 点击默认地址
    @allure.step(title='地址管理页面 点击默认地址')
    def click_default_address(self):
        self.click(self.is_default_feature)

    # 点击编辑按钮
    @allure.step(title='地址管理页面 点击编辑')
    def click_edit(self):
        self.click(self.edit_button)

    # 点击删除按钮
    @allure.step(title='地址管理页面 点击删除')
    def click_delete(self):
        self.click(self.delete_button)

    # 点击确任按钮
    @allure.step(title='地址管理页面 点击确认')
    def click_commit(self):
        self.click(self.commit_button)

    # 判断删除按钮是否存在
    @allure.step(title='地址管理页面 判断删除按钮是否存在')
    def is_delete_exist(self):
        return self.is_feature_exist(self.delete_button)

