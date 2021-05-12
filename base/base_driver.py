from appium import webdriver
# 此处返回一个driver
# 务必保证后面的对象使用同一个driver  对于登录模块 需要先重置应用
def init_driver(no_reset=True):
    desired_caps = dict()
    desired_caps['automationName'] = 'uiautomator2'  # 不指定2版本会出错
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8.0'
    desired_caps['deviceName'] = 'c5e5d5eb'  # 真机名 可以随便写
    desired_caps['appPackage'] = 'com.yunmall.lc'  # 程序名
    desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'  # 界面名
    desired_caps['noReset'] = no_reset  # appium每次起动时，默认每次都会重置程序 此处设置不重置
    desired_caps["unicodeKeyboard"] = True  # 设置手机输入法为unicodeKeyboard，并手动把默认输入法改为此输入法  解决中文乱码问题
    desired_caps["resetKeyboard"] = False
    # desired_caps['newCommandTimeout'] = '600'  # 设置appium自动关闭程序时间 不设置APPIUM大概60s自动退出
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver
# adb shell dumpsys window windows | findstr mFocusedApp 查找包名 界面名
