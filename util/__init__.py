import numpy as np
import cv2
from config import *


# 从文本文件读取数据
def read_data(filename):
    vector_list = []
    label_list = []
    img_list = []
    with open(filename, 'r') as f:
        for line in f:
            vector = []
            img_name, binary, label = line.split('\t')
            for i in binary:
                if i == '0':
                    vector.append(-1)
                else:
                    vector.append(1)
            vector_list.append(np.array(vector))
            label_list.append(label[:-1])
            img_list.append(img_name)
        return img_list, vector_list, label_list


# 计算汉明距离
def hamming_distance(data_arr, item):
    dis = np.dot(item, data_arr.T)
    return (K - dis) / 2


# 转化成二进制字符转
def to_binary_string(binary_like_values):
    num, bit_length = binary_like_values.shape
    list_string_binary = []
    for i in range(num):
        bit = ''
        for j in range(bit_length):
            bit += '0' if binary_like_values[i][j] <= 0 else '1'
        list_string_binary.append(bit)
    return list_string_binary


# 文本添加数据
def insert_txt(file, url, code, label):
    f = open(file, 'a')
    f.write(url + '\t' + code + '\t' + label + '\n')
    pass


# 返回文件列表
def get_file_name(path):
    if not os.path.exists(path):
        print('can not find the path')
        return
    return os.listdir(path)


# 显示图片
def show_img(n, m, t=0):
    cv2.imshow(n, m)
    cv2.waitKey(t)
