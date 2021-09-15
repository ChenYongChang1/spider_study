import os
import json

arr = []

def make_dir(path):
    exist = os.path.exists(path)
    if not exist:
        os.mkdir(path)
    else:
        print('“{}”目录已存在'.format(path))

def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        # print(root)  # 当前目录路径
        # print(dirs)  # 当前路径下所有子目录
        # print(files)  # 当前路径下所有非目录子文件
        with open('./jj/all.py', 'a+', encoding='utf-8') as F:
            for i in files:
                with open('./juejinpy/{}'.format(i), 'r+', encoding='utf-8') as f:
                    # print(f.read())
                    arr.append(json.load(f, ensure_ascii=False))
                    # print(i)
                    # strs = f.read() + ',\n'
                    # F.write(strs)
                # fil = f.read()
                # for i in fil:
                #     print(i)
                # if maps.get()
                # arr.append(fil)


file_name('./juejin')
