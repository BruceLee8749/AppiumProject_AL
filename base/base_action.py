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
        message_xpath = By.XPATH, '//*[contains(@text,"{}")]'.format(message)
        try:
            self.find_element(message_xpath, 5, 0.1)
            print('找到toast元素了')
            return True
        except:
            print('打印当前错误信息:元素未找到！')
            return False

    # 获取toast的全部文本值
    def get_toast_text(self, message):
        if self.is_toast_exist(message):
            message_xpath = By.XPATH, '//*[contains(@text,"{}}")]'.format(message)
            return self.get_text(message_xpath)
        else:
            # 自定义异常信息 并抛出
            raise Exception('toast未出现，请检查参数是否正确，或toast有没有出现在屏幕上')
