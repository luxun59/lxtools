'''
Author: luxun luxun59@126.com
Date: 2024-11-07 20:20:48
LastEditors: luxun luxun59@126.com
LastEditTime: 2024-11-13 10:05:01
FilePath: \lxtools\w2vdateset\english-test\copy_from_tsv_to_dir.py
Description: 

Copyright (c) 2024 by luxun59@126.com, All Rights Reserved. 
'''
'''
Author: luxun luxun59@126.com
Date: 2024-11-07 20:20:48
LastEditors: luxun luxun59@126.com
LastEditTime: 2024-11-07 20:25:25
FilePath: \lxtools\w2vdateset\english-test\copy_from_tsv_to_dir.py
Description: 

Copyright (c) 2024 by luxun59@126.com, All Rights Reserved. 
'''



import os
import shutil

def copy_files_from_list(filenames_txt, source_dir, target_dir):
    # 确保目标目录存在，如果不存在则创建
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # 读取文件名列表
    with open(filenames_txt, 'r') as file:
        next(file)
        file_list = file.readlines()

    # 去除文件名两侧的空白字符（包括换行符）
    file_list = [line.strip().split("\t")[1] for line in file_list]

    # 遍历文件名列表
    for filename in file_list:
        # 构建源文件的完整路径
        source_file = os.path.join(source_dir, filename)
        # 构建目标文件的完整路径
        target_file = os.path.join(target_dir, filename)

        # 检查源文件是否存在
        if os.path.isfile(source_file):
            # 复制文件到目标目录
            shutil.copy2(source_file, target_file)
            print(f"Copied {source_file} to {target_file}")
        else:
            print(f"Source file not found: {source_file}")

if __name__ == "__main__":
    # 文件名列表的文本文件路径
    filenames_txt_path = "path/to/filenames.txt"
    # 源目录路径
    source_directory = "path/to/source/directory"
    # 目标目录路径
    target_directory = "path/to/target/directory"

    copy_files_from_list(filenames_txt_path, source_directory, target_directory)







