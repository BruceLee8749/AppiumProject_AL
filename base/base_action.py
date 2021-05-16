import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    # 获取元素方法封装  WebDriverWait(driver, timeout, poll_frequency=POLL_FREQUENCY)
    def find_element(self, loc, timeout=30, poll=0.5):
        # 使用*表示参数解耦  driver.find_element(*loc) <==>driver.find_element（By.xxx,value)
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    def find_elements(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))

    def click(self, loc):
        self.find_element(loc).click()

    def input(self, loc, text):
        self.find_element(loc).clear()
        self.find_element(loc).send_keys(text)

    def get_text(self, loc):
        return self.find_element(loc).text

    # 根据提供内容，判断toast能否找到
    def is_toast_exist(self, message):
        """
        根据部分内容，判断toast是否存在
        :param message: 文字部分内容
        :return: 是否存在
        contains（）文字部分包含方法
        """
        message_xpath = By.XPATH, "//*[contains(@text,'{}')]".format(message)
        try:
            self.find_element(message_xpath,6,0.1)
            return True
        except:
            print('打印当前错误信息:元素未找到！')
            return False

    # 获取toast的全部文本值
    def get_toast_text(self, message):
        if self.is_toast_exist(message):
            message_xpath = By.XPATH, '//*[contains(@text,"{}")]'.format(message)
            return self.get_text(message_xpath)
        else:
            # 自定义异常信息 并抛出
            raise Exception('toast未出现，请检查参数是否正确，或toast有没有出现在屏幕上')

    # 定义滑动屏幕一次方法  从1/4屏幕位置 到 3/4屏幕位置
    def scroll_page_one_time(self, direction='up'):
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']

        # center为中心，为坐标位置起始点
        center_x = width / 2
        center_y = height / 2

        # 左右滑动参数
        left_x = width / 4
        left_y = center_y
        right_x = center_x / 4 * 3
        right_y = center_y

        # 上下滑动参数
        top_x = center_x
        top_y = height / 4
        bottom_x = center_x
        bottom_y = height / 4 * 3

        # 从下往上滑动
        if direction == 'up':
            self.driver.swipe(bottom_x,bottom_y,top_x,top_y,1000)
        # 从上往下滑动
        elif direction == 'down':
            self.driver.swipe(top_x,top_y,bottom_x,bottom_y,1000)
        # 从右往左滑动
        elif direction == 'left':
            self.driver.swipe(right_x,right_y,left_x,left_y,1000)
        # 从左往右滑动
        elif direction == 'right':
            self.driver.swipe(left_x,left_y,right_x,right_y,1000)
        else:
            raise Exception('必须使用指定方向参数名称: up/down/left/right')

    # 定义边滑边找方法
    def find_element_with_scroll(self,loc,direction='up'):
        page_source = ''
        while True:
            try:
                # 如果可以找到 就返回元素
                return self.find_element(loc)
            except:
                # 找不到，就循环滑动屏幕进行查找，一直找到为止（退出死循环）
                self.scroll_page_one_time(direction)
                # 判断是否滑到底部
                if self.driver.page_source == page_source:
                    print('到底了')
                    break
                else:
                    # 如果滑动 后整屏元素不等于上次整屏元素 就再次赋值
                    page_source = self.driver.page_source

    # 获取 关键字字符串是否在page_source中 （driver.page_source 返回是一段超长字符串）
    def is_keyword_in_page_source(self,keyword,timeout=5,poll=0.2):
        """
        keyword: 要找的关键字字符串
        timeout: 查找总时间
        poll: 时间间隔
        return  如果在page_source中返回 True，否则返回False
        """
        # 结束时间
        end_time = time.time() + timeout;
        while True:
            # 如果结束时间大于当前时间，那么就认为超时了
            if time.time() > end_time:
                return False
            elif keyword in self.driver.page_source:
                return True
            time.sleep(poll)

    # 判断某个特征是否存在 必须传递时间5s 否则会找30s才会报异常 浪费时间
    def is_feature_exist(self,feature,timeout=5,poll=0.1):
        try:
            self.find_element(feature,timeout,poll)
            return True
        except:
            return False