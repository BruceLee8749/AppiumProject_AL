import random
import time

import allure
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
    save_button = By.XPATH, '//*[@text="保存"]'

    # 输入 收件人
    @allure.step(title='新增地址页面 输入收件人')
    def input_name(self, text):
        self.input(self.name_edit_text, text)

    # 输入 手机号
    @allure.step(title='新增地址页面 输入手机号')
    def input_phone(self, text):
        self.input(self.phone_edit_text, text)

    # 输入 详细地址
    @allure.step(title='新增地址页面 输入详细地址')
    def input_info(self, text):
        self.input(self.info_edit_text, text)

    # 输入邮编
    @allure.step(title='新增地址页面 输入邮编')
    def input_post_code(self, text):
        self.input(self.post_code_edit_text, text)

    # 点击设置为默认地址
    @allure.step(title='新增地址页面 点击设置默认地址')
    def click_default(self):
        self.click(self.default_address_button)

    # 点击选择所在地区
    @allure.step(title='新增地址页面 点选城市1')
    def click_region(self):
        self.click(self.region_button)

    # 进入所在地区并选择随机区域
    @allure.step(title='新增地址页面 点选城市2')
    def choose_region(self):
        self.click_region()
        while True:
            # 查看是否 还在城市列表页面上 不等于 就表示点完了
            if self.driver.current_activity != 'com.yunmall.ymctoc.ui.activity.ProvinceActivity':
                return
            # 获取 当前屏幕上 所有城市/直辖市元素
            areas = self.find_elements(self.area_feature)
            areas_count = len(areas)
            area_index = random.randint(0, areas_count - 1)
            # 获取随机城市  通过列表下标 对列表中一组元素的指定某个元素 进行点击
            areas[area_index].click()
            time.sleep(1)

    # 点击保存
    @allure.step(title='新增地址页面 点击保存')
    def click_save(self):
        self.click(self.save_button)

    # 新增地址组合业务方法
    @allure.step(title='新增地址页面 填写地址信息组合业务方法')
    def add_new_address_group(self, name_text, phone_text, info_text, post_code_text,set_default):
        # 输入名字-电话-选择地区-输入详细地址-输入邮编-点击默认-点击保存 Ture-->点击默认按钮
        print('打印组合方法参数(有些是空值测试值)：{},{},{},{},{}'.format(name_text, phone_text, info_text, post_code_text,set_default))
        self.input_name(name_text)
        self.input_phone(phone_text)
        self.choose_region()
        self.input_info(info_text)
        self.input_post_code(post_code_text)
        if set_default is True:
            self.click_default()
        self.click_save()
