import os
import shutil
import sys


# 将dir目录下的图像按照6:2:2的比例分割训练集、验证集、测试集
def split_image_data(dir_path, save_dir_path):
    if os.path.exists(dir_path):
        for f1 in os.listdir(dir_path):
            second_dir_path = os.path.join(dir_path, f1)
            file_list = os.listdir(second_dir_path)
            train_save_dir = os.path.join(save_dir_path, "train", f1)
            if not os.path.exists(train_save_dir):
                os.makedirs(train_save_dir)
            val_save_dir = os.path.join(save_dir_path, "val", f1)
            if not os.path.exists(val_save_dir):
                os.makedirs(val_save_dir)
            test_save_dir = os.path.join(save_dir_path, "test", f1)
            if not os.path.exists(test_save_dir):
                os.makedirs(test_save_dir)
            for index, file in enumerate(file_list):
                file_path = os.path.join(second_dir_path, file)
                if index <= len(file_list) * 0.6:
                    save_path = os.path.join(train_save_dir, file)
                elif len(file_list) * 0.6 < index <= len(file_list) * 0.8:
                    save_path = os.path.join(val_save_dir, file)
                else:
                    save_path = os.path.join(test_save_dir, file)
                shutil.move(file_path, save_path)




if __name__ == '__main__':
    split_image_data(sys.argv[1], sys.argv[2])
