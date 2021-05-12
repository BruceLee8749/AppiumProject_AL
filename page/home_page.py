from selenium.webdriver.common.by import By

from base.base_action import BaseAction


# 网站主页面
class HomePage(BaseAction):
    # 元素 “我”
    me_button = By.ID, 'com.yunmall.lc:id/tab_me'

    # 点击 “我”
    def click_me(self):
        self.click(self.me_button)

    # 判断当前页面是否登录，未登录--> 直接点击登录按钮 已登录--> 结束方法  用到很多页面 需要传page对象
    def login_if_not(self, page):
        # 点击 我
        self.click_me()
        # 查看包名和界面名字：如果未登录
        if self.driver.current_activity == 'com.yunmall.ymctoc.ui.activity.LogonActivity':
            # 点击底部已有账号，去登录
            page.register.click_login()
            # 输入用户名
            page.login.input_username('itheima_test')
            # 输入密码
            page.login.input_password('itheima')
            # 点击登录
            page.login.click_login()
        else:
            # 如果已经登录 直接返回结束
            return
