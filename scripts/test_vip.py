from time import sleep

import pytest
from appium.common.exceptions import NoSuchContextException
from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestVip:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        sleep(13)
        self.driver.quit()

    data_list = analyze_file('vip_data.yaml', 'test_vip')

    @pytest.mark.parametrize('args', data_list)
    def test_vip(self, args):
        self.keyword = args['keyword']
        self.expect = args['expect']
        # 登录
        self.page.home.login_if_not(self.page)
        # 点击加入超级vip
        self.page.me.click_be_vip()
        sleep(3)
        try:
            print(self.driver.contexts)
            # 切换Webviewer 页面
            self.driver.switch_to.context('WEBVIEW_com.yunmall.lc')
            # 进入WebViewer页面 输入邀请码
            self.page.vip.input_invite(self.keyword)
            # 点击 立即成为会员
            self.page.vip.click_be_vip()
            # 断言，输入后返回结果 是否在page_source中 -->str类型
            assert self.page.vip.is_keyword_in_page_source(self.expect)
            # 切换回原生环境
            self.driver.switch_to.context('NATIVE_APP')
        except NoSuchContextException:
            print('获取不了上下文异常：真机需要root 需要在源码加入webView debug语句 ')
