import time
from time import sleep

from base.base_driver import init_driver  # 按道理说这样导入语法没错。但是但是但是，需要在当前文件夹中建立一个__init__.py文件 或者sys中添加目录
from page.page import Page
import pytest
from base.base_analyze import analyze_file


class TestLogin:
    def setup_class(self):
        # 定义同一个变量 保证后面的若干对象使用同一个driver
        self.driver = init_driver(False)
        self.page = Page(self.driver)
        # 截图文件名字
        now_time = time.strftime('%Y_%m_%d %H_%M_%S')
        try:
            # 进入注册登录页面
            self.page.home.click_me()
            self.page.register.click_login()
        except:
            # 截图文件名字必须符合规范 不能有\ / : * ? # ” < > |
            self.page.driver.get_screenshot_as_file('./data/{}.png'.format(now_time))
            raise Exception('未进注册登录界面，检查是否已登录')

    def teardown_class(self):
        sleep(10)
        self.driver.quit()

    # 虽然单元测试一组方法不太好，但测的是仅仅一个功能 原则可以接受
    data_list = analyze_file('login_data.yaml', 'test_login')

    @pytest.mark.parametrize('args', data_list)
    def test_login(self, args):
        username = args['username']
        password = args['password']
        toast = args['toast']
        # 脚本流程
        sleep(3)
        self.page.login.input_username(username)
        self.page.login.input_password(password)
        self.page.login.click_login()
        if toast is None:
            # assert <condition>,<error message>
            print('打印当前页面source：', self.page.driver.page_source)
            assert self.page.me.get_nick_name_text() == username, '登录后的用户名和输入时的用户名不一致'
            # 如果用户登录成功，但是输入的用户名和界面显示不一样，就提示：登录后的用户名和输入时的用户名不一致
        else:
            # 找toast提示，把预定toast参数传进去看是否可以找到，如果能就通过，否则不通过

            assert self.page.login.is_toast_exist(toast)

