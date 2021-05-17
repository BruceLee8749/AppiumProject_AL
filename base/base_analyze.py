import yaml


# 此处key为yaml 最外层的key
def analyze_file(file_name, key):
    # 用pytest命令运行路径为：./data/
    # 用框架run in 运行路径为：../data/
    with open("../data/{}".format(file_name), "r", encoding='utf-8') as f:
        case_data = yaml.load(f, Loader=yaml.FullLoader)[key]

        data_list = list()
        for i in case_data.values():
            data_list.append(i)

        return data_list

# data_list = analyze_file('login_data.yaml','test_login')
# print(data_list)
