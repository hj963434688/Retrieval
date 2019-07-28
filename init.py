from util import *
from config import *
from network import NNService

head = 'https://pro-img.and-shoe.com/resource/ai/'


def init_from_image(images_path, db_file, mode=0):
    nn = NNService(k=K)

    if mode == 0:
        f = open(db_file, 'w')
    elif mode == 1:
        f = open(db_file, 'a')
    image_list = get_file_name(images_path)

    for i, img in enumerate(image_list):
        image = cv2.imread(images_path + img)[:, :, ::-1]
        mean = np.mean(image, axis=(0, 1), dtype=int)
        image = cv2.resize(image, (input_size, input_size))
        out_bin = nn.img_bin([image])
        code = to_binary_string(out_bin)[0]
        label = '-'.join([str(m) for m in mean]) + '-' + str(i)
        print(i, label)
        f.write(head + img + '\t' + code + '\t' + label + '\n')


if __name__ == '__main__':
    init_from_image('/home/yxt/img_retr/dataset/material/all_images/', './database/data_vgg16_material.txt')
    # init_from_image('/home/yxt/img_retr/dataset/parts/all_images/', './database/data_vgg16_parts_4096.txt')
    # pass