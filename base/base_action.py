from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    # 获取元素方法封装
    def find_element(self, loc, timeout=30, poll=0.5):
        # 使用*表示参数解耦  driver.find_element(*loc) <==>driver.find_element（By.xxx,value)
        return WebDriverWait(self.driver, timeout=timeout,poll_frequency=poll).until(lambda x: x.find_element(*loc))

    def find_elements(self, loc, timeout=10, poll=1):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_elements(*loc))

    def click(self, loc):
        self.find_element(loc).click()

    def input(self, loc, text):
        self.find_element(loc).clear()
        self.find_element(loc).send_keys(text)

    def get_text(self, loc):
        return self.find_element(loc).text
