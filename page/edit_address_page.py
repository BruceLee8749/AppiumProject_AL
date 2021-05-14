from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class EditAddressPage(BaseAction):
    # 收件人输入框
    name_edit_text = By.ID, 'com.yunmall.lc:id/address_receipt_name'
    # 手机号输入框
    phone_edit_text = By.ID, 'com.yunmall.lc:id/address_add_phone'
    # 详细地址输入框
    info_edit_text = By.ID, 'com.yunmall.lc:id/address_detail_addr_info'
    # 邮编输入框
    post_code_edit_text = By.ID, 'com.yunmall.lc:id/address_post_code'
    # 设为默认地址 单选框
    default_address_button = By.ID, 'com.yunmall.lc:id/address_default'

    # 输入 收件人
    def input_name(self,text):
        self.input(self.name_edit_text,text)

    # 输入 手机号
    def input_phone(self,text):
        self.input(self.phone_edit_text,text)

    # 输入 详细地址
    def input_info(self,text):
        self.input(self.info_edit_text,text)

    # 输入邮编
    def input_post_code(self,text):
        self.input(self.post_code_edit_text,text)

    # 点击设置为默认地址
    def click_default(self):
        self.find_element(self.default_address_button).click()
    # 点击 保存
