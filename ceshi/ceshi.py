import time
from time import sleep

from appium import webdriver

desired_caps = dict()
desired_caps['automationName'] = 'uiautomator2'  # 不指定2版本会出错 使用该框架还能解决中文乱码问题
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0'  # S7为8.0
desired_caps['deviceName'] = 'c5e5d5eb'  # S7真机名 可以随便写
# desired_caps['deviceName'] = '192.168.84.101:5555'  # S6模拟器
desired_caps['appPackage'] = 'com.yunmall.lc'  # 程序名
desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'  # 界面名
desired_caps['noReset'] = True # appium每次起动时，默认每次都会重置程序 此处设置不重置
desired_caps["unicodeKeyboard"] = True  # 设置手机输入法为unicodeKeyboard，并手动把默认输入法改为此输入法  解决中文乱码问题
desired_caps["resetKeyboard"] = False
# desired_caps['newCommandTimeout'] = '600'  # 设置appium自动关闭程序时间 不设置APPIUM大概60s自动退出
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# adb shell dumpsys window windows | findstr mFocusedApp
# sleep(3)
# print(time.time())
# print(time.time())
# print(type(driver.page_source))
# driver.find_element_by_xpath('//*contains[@text,"hello"]')
print(desired_caps)