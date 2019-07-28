import nets.vgg as vgg
import tensorflow as tf
import net
from util import *


# 网络服务类的定义
class NNService:

    def __init__(self, model_name='../vgg/vgg_16.ckpt', k=hash_bits[1]):
        with tf.get_default_graph().as_default():
            # 输入图片
            self.images = tf.placeholder(tf.float32, shape=[None, input_size, input_size, 3])
            # 预处理
            self.inputs = net.mean_image_subtraction(self.images)
            # 网络输出
            self.outputs, self.end_points = vgg.vgg_16(self.inputs, is_training=False)
            # 得到特征值
            if k == 1000:
                self.binary = tf.sign(self.outputs)
            else:
                self.out_4096 = tf.squeeze(self.end_points['vgg_16/fc6'], [1, 2])
                self.binary = tf.sign(self.out_4096)
            # 创建会话
            self.sess = tf.InteractiveSession()
            # 模型保存类
            self.saver = tf.train.Saver()

            # 数据文件
            if k == 1000:
                self.db_files = ['./database/data_vgg16_material.txt', './database/data_vgg16_parts.txt']
            else:
                self.db_files = ['./database/data_vgg16_material_4096.txt', './database/data_vgg16_parts_4096.txt']

            # 载入模型
            if os.path.exists(model_name):
                self.checkpoint_path = model_name
                self.saver.restore(self.sess, self.checkpoint_path)
                print('Restore from {}'.format(self.checkpoint_path))
            # 读取数据库
            self.database = []
            for f in self.db_files:
                if os.path.exists(f):
                    print('Read data from {}'.format(f))
                    data_f = read_data(f)
                    self.database.append(data_f)
                else:
                    print('can not find file')

    # 正向传播
    def img_bin(self, images):
        res_sign = self.sess.run(self.binary, feed_dict={self.images: images})
        return res_sign

    # 获取内存数据
    def get_data(self, tag=0):
        return self.database[tag]

    # 更新内存数据
    def update_db(self, url, code, label, tag=0):
        self.database[tag][0].append(url)
        self.database[tag][1].append(code)
        self.database[tag][2].append(label)

    # 删除内存数据
    def delete_data(self, url, tag=0):
        index = self.database[tag][0].index(url)
        del self.database[tag][0][index]
        del self.database[tag][1][index]
        del self.database[tag][2][index]

    # 检查内存数据
    def check_data(self):
        print('check data')
        try:
            for i in range(len(self.db_files)):
                for k in range(3):
                    print(len(self.database[i][k]))

        except():
            print('Reload txt')
            self.database = []
            for f in self.db_files:
                if os.path.exists(f):
                    print('Read data from {}'.format(f))
                    data_f = read_data(f)
                    self.database.append(data_f)
                else:
                    print('can not find file')


if __name__ == '__main__':
    pass
