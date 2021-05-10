import os

import yaml


def analyze_file(file_name, key):
    # os.sep 作用：兼容ios和windows 文件路径的斜杠
    with open(".%sdata%s%s" % (os.sep, os.sep, file_name), "r") as f:
        case_data = yaml.load(f)[key]

        data_list = list()
        for i in case_data.values():
            data_list.append(i)

        return data_list
