from appium.common.exceptions import NoSuchContextException
from selenium import  webdriver
dict = dict()
print(dict)
dict1 = {"height":"165cm","width":"30cm"}
print(dict1['height'])

try:
    driver = webdriver.Firefox()
    driver.find_element_by_id('hello')
    1/0

except NoSuchContextException:
    print('测试是否可以打印出来')
else:
    print('else测试是否可以打印出来')
finally:
    print('finally测试是否可以打印出来')