from base.base_analyze import analyze_file

data_list = analyze_file('address_data.yaml', 'test_add_address')
print(data_list)
class testA:
    index1 = 1
    def printinfo(self):
        testA.index1 += 1
        print(testA.index1)
a = testA()
a.printinfo()
# 别看他们长得一样其实是两个不一样的东西！一定要注意有特殊字符的情况！！！
assert '收件人姓名21个字符' == '收件人姓名215个字符'
