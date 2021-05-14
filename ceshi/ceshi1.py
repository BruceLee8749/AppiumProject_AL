from appium.common.exceptions import NoSuchContextException

dict = dict()
print(dict)
dict1 = {"height":"165cm","width":"30cm"}
print(dict1['height'])

try:
    1/0
except NoSuchContextException:
    print('测试是否可以打印出来')
else:
    print('else测试是否可以打印出来')
finally:
    print('finally测试是否可以打印出来')