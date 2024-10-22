#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""
Helper script to pre-compute embeddings for a flashlight (previously called wav2letter++) dataset
"""

import argparse
import os
import re

def read_ref_file(filepath):  
    """  
    读取ref.txt文件并返回一个字典，键是文件名，值是该文件名所在行的前面字符串和行号。  
    """  
    file_dict = {}  
    try:  
        with open(filepath, 'r', encoding='utf-8') as file:  
            lines = file.readlines()  
            for line_num, line in enumerate(lines, start=1):  
                # 查找括号内的文件名   
                match = re.search(r'\((.*?\.wav)\)', line)  
                # print("line",line)
                if match:  
                    filename = match.group(1)  
                    filename = os.path.basename(filename)
                    # print("file_name",filename)
                    # print("file_name— size:",len(filename))
                    prefix = line[:match.start()].strip()  
                    file_dict[filename.strip()] = prefix 
    except FileNotFoundError:  
        print(f"文件 {filepath} 未找到。")
    # print(file_dict)
    return file_dict  

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--read-ref-file",required=True)
    parser.add_argument("tsv")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--output-name", required=True)
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    transcriptions = {}
    #读取参考文件，创建字典
    file_dict = read_ref_file(args.read_ref_file)

    with open(args.tsv, "r") as tsv, open(
        os.path.join(args.output_dir, args.output_name + ".ltr"), "w"
    ) as ltr_out, open(
        os.path.join(args.output_dir, args.output_name + ".wrd"), "w"
    ) as wrd_out,open(
        os.path.join(args.output_dir, args.output_name + "_new.tsv"), "w"
    ) as tsv_out:
        root = next(tsv).strip()
        for line in tsv:
            line_origin = line
            line = line.split('\t')[0]
            dir = os.path.basename(line)
            if dir not in transcriptions:
                # parts = dir.split(os.path.sep)
                # trans_path = f"{parts[-2]}-{parts[-1]}.trans.txt"
                # path = os.path.join(root, dir, trans_path)
                # assert os.path.exists(path)
                # texts = {}
                # with open(path, "r") as trans_f:
                #     for tline in trans_f:
                #         items = tline.strip().split()
                #         texts[items[0]] = " ".join(items[1:])
                # print("dir:",dir)
                # print(file_dict[dir])
                if dir not in file_dict:
                    # print("{}not in ref".format(dir))
                    continue

                transcriptions[dir] = file_dict[dir]
            part = os.path.basename(line).split(".")[0]
            # assert part in transcriptions[dir]
            print(transcriptions[dir], file=wrd_out)
            print(
                " ".join(list(transcriptions[dir].replace(" ", "|"))) + " |",
                file=ltr_out,
            )
            print(line_origin[:-1],file=tsv_out)



if __name__ == "__main__":
    main()






