import random
import time

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


# 新增地址页面
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
    # 所在地区
    region_button = By.ID, 'com.yunmall.lc:id/address_province'
    # 省市区
    area_feature = By.ID, 'com.yunmall.lc:id/area_title'
    # 保存
    save_button = By.ID, 'com.yunmall.lc:id/button_send'

    # 输入 收件人
    def input_name(self, text):
        self.input(self.name_edit_text, text)

    # 输入 手机号
    def input_phone(self, text):
        self.input(self.phone_edit_text, text)

    # 输入 详细地址
    def input_info(self, text):
        self.input(self.info_edit_text, text)

    # 输入邮编
    def input_post_code(self, text):
        self.input(self.post_code_edit_text, text)

    # 点击设置为默认地址
    def click_default(self):
        self.click(self.default_address_button)

    # 点击选择所在地区
    def click_region(self):
        self.click(self.region_button)

    # 进入所在地区并选择随机区域
    def choose_region(self):
        self.click_region()
        while True:
            # 查看是否 还在城市列表页面上 不等于 就表示点完了
            if self.driver.current_activity != 'com.yunmall.ymctoc.ui.activity.ProvinceActivity':
                return
            # 获取 当前屏幕上 所有城市/直辖市元素
            areas = self.find_elements(self.area_feature)
            areas_count = len(areas)
            print('城市列表中有多少个城市:',areas_count)
            area_index = random.randint(0, areas_count - 1)
            # 获取随机城市  通过列表下标 对列表中一组元素的指定某个元素 进行点击
            areas[area_index].click()
            time.sleep(1)

    # 点击保存
    def click_save(self):
        self.click(self.save_button)
