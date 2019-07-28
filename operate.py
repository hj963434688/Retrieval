from config import *
from skimage import io
from util import *
import heapq
import json


def retrieval_ing(url, nn, tag=0, num=10):
    try:
        image = io.imread(url)
    except():
        return b'404'

    try:
        # 判断三通道
        if image.shape[2] > 3:
            image = image[:, :, :3]
        image = cv2.resize(image, (input_size, input_size))
        # 网络正向传播
        out_bin = nn.img_bin([image])[0]
        # # 检查数据
        nn.check_data()
        # 获取要操作的数据库
        db = nn.get_data(tag)
        print(np.array(db[1]).shape)
        print(out_bin.shape)
        # 计算距离
        distances_arr = hamming_distance(np.array(db[1]), out_bin)
        # 计算得分
        scores = 1 - distances_arr / (out_bin.shape[0] - 1)
        # 获取下标
        min_index = heapq.nsmallest(num, range(len(distances_arr)), distances_arr.__getitem__)
        result = []
        item = {}
        print('append')
        for idx in min_index:

            item['url'] = db[0][idx]
            item['score'] = scores[idx]
            item['msg'] = db[2][idx]
            result.append(item)
            item = {}
        print('done')
    except():
        return b'555'
    # 返回数据
    res = json.dumps(result)
    return res


def insert_img(url, nn, id_, tag=0):
    # 检查数据
    nn.check_data()
    # 获取要操作的数据库
    db = nn.get_data(tag)
    if url in db[0]:
        print('111')
        return b'111'
    try:
        # 读取图片
        image = io.imread(url)
    except():
        print('404')
        return b'404'
    try:
        if image.shape[2] > 3:
            image = image[:, :, :3]
        # 计算机三通道平均值
        mean = np.mean(image, axis=(0, 1), dtype=int)
        image = cv2.resize(image, (input_size, input_size))
        # 正向传播
        out_bin = nn.img_bin([image])
        # 转化字符
        code = to_binary_string(out_bin)[0]
        print(mean)
        label = '-'.join([str(m) for m in mean]) + '-' + id_
        # 更新内存数据
        nn.update_db(url, out_bin[0], label, tag)
        # 写入文件
        db_file = open(nn.db_files[tag], 'a')
        db_file.write(url + '\t' + code + '\t' + label + '\n')
        db_file.close()
    except():
        return b'555'
    print('insert ', url)
    return b'insert done'


# 删除文本数据
def del_line(file, index):
    old = open(file, 'r')
    new = open(file, 'r+')
    print(file)
    current_line = 0
    while current_line < (index - 1):
        old.readline()
        current_line += 1

    seek_point = old.tell()
    new.seek(seek_point, 0)
    old.readline()
    next_line = old.readline()

    while next_line:
        new.write(next_line)
        next_line = old.readline()

    new.truncate()


def delete_img(url, nn, tag=0):
    if nn.if_reload():
        nn.load_txt()
    db = nn.get_data(tag)
    if url not in db[0]:
        print('222')
        return b'222'
    else:
        index = db[0].index(url)

    try:
        nn.delete_data(url, tag)
        del_line(nn.db_files[tag], index+1)
    except():
        return b'555'
    print('delete ', url)
    return b'delete done'


if __name__ == '__main__':
    pass
