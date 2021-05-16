from page.about_page import AboutPage
from page.address_list_page import AddressListPage
from page.edit_address_page import EditAddressPage
from page.home_page import HomePage
from page.login_page import LoginPage
from page.me_page import MyPage
from page.register_page import RegisterPage
from page.setting_page import SettingPage
from page.vip_page import VipPage


# 所有page的入口类
class Page:
    def __init__(self, driver):
        # 初始化driver 后面self.driver 都是同一个driver
        self.driver = driver

    # @property将方法变成属性调用方式
    @property
    def home(self):
        return HomePage(self.driver)

    @property
    def login(self):
        return LoginPage(self.driver)

    @property
    def register(self):
        return RegisterPage(self.driver)

    @property
    def me(self):
        return MyPage(self.driver)

    @property
    def register(self):
        return RegisterPage(self.driver)

    @property
    def setting(self):
        return SettingPage(self.driver)

    @property
    def about(self):
        return AboutPage(self.driver)

    @property
    def vip(self):
        return VipPage(self.driver)

    @property
    def address_list(self):
        return AddressListPage(self.driver)

    @property
    def edit_address(self):
        return EditAddressPage(self.driver)

    # 从登录到进入地址管理页面封装
    def enter_address_manager(self,page_obj):
        # 登录
        self.home.login_if_not(page_obj)
        # 用户信息页面上 点击设置
        self.me.click_setting()
        # 设置页面上 点击地址管理
        self.setting.click_address_list()
