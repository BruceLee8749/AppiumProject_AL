from appium import webdriver


# 务必保证后面的对象使用同一个driver 此处仅返回driver
def init_driver():
    desired_caps = dict()
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8.0'
    desired_caps['deviceName'] = 'c5e5d5eb'  # 真机名 可以随便写
    desired_caps['appPackage'] = ' com.yunmall.lc'  # 程序名
    desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'  # 界面名
    desired_caps['noReset'] = True  # appium每次起动时，默认每次都会重置程序 此处设置不重置
    desired_caps["unicodeKeyboard"] = 'True'  # 设置手机输入法为unicodeKeyboard，并手动把默认输入法改为此输入法  解决中文乱码问题
    desired_caps["resetKeyboard"] = 'True'
    desired_caps['newCommandTimeout'] = '600'  # 设置appium自动关闭程序时间
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver
