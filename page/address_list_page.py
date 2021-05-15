from selenium.webdriver.common.by import By

from base.base_action import BaseAction


# 地址管理页面
class AddressListPage(BaseAction):
    # 新增地址按钮
    add_address_button = By.ID, 'com.yunmall.lc:id/address_add_new_btn'
    # 默认的姓名+电话信息
    default_receipt_name_text_view = By.ID, 'com.yunmall.lc:id/receipt_name'

    # 点击新增地址按钮
    def click_add_address(self):
        self.find_element_with_scroll(self.add_address_button).click()

    # 获取页面上默认地址 姓名+电话信息 (如果找的是一组元素，仍用find_element不会报错，系统会默认查找第一个)
    def get_default_receipt_name_text(self):
        return self.get_text(self.default_receipt_name_text_view)
