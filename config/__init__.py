import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'

# 输入尺寸
input_size = 224

# 特征编码数目
hash_bits = (1000, 4096)
K = hash_bits[0]
# hash_bits = 4096

if __name__ == '__main__':
    pass
