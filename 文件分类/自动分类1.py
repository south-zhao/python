import os
import shutil

src_folder = 'D:\\大一下\\选修课\\'
des_folder = 'D:\\大一下\\选修课\\说课'
files = os.listdir(src_folder)
print(files)
for i in files:
    src_path = src_folder + i
    if os.path.isfile(src_path):
        des_path = des_folder + i.split('.')[-1]
        if not os.path.exists(des_path):
            os.makedirs(des_path)
        shutil.move(src_path, des_path)
