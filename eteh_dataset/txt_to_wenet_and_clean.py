'''
Author: luxun luxun59@126.com
Date: 2024-10-22 09:32:07
LastEditors: luxun59 luxun59@126.com
LastEditTime: 2025-02-09 23:10:12
FilePath: \lxtools\eteh_dataset\txt_to_wenet_and_clean.py
Description: from a ref.txt type: xxxx(xxx/xxx.wav) 
                                  xxxx(xxx/xxx.wav) 

             to                   xxx.wav xxxx                     

Copyright (c) 2024 by luxun59@126.com, All Rights Reserved. 
'''

import argparse
import os
import re
import sys

def read_ref_file_and_write_to_wenet(infilepath,outfilepath):  
    """  
    读取ref.txt文件并返回一个字典，键是文件名，值是该文件名所在行的前面字符串和行号。  
    """  
    file_dict = {}  
    try:  
        with open(infilepath, 'r', encoding='utf-8') as infile, open(
            outfilepath,'w',encoding='utf-8') as outfile:  
            lines = infile.readlines()  
            for line_num, line in enumerate(lines, start=1):  
                # 查找括号内的文件名   
                match = re.search(r'\((.*?)\)', line)  
                # print("line",line)
                if match:  
                    filename = match.group(1)  
                    # filename = os.path.basename(filename)
                    prefix = line[:match.start()].strip()  
                    file_dict[filename.strip()] = prefix
                    outfile.writelines(filename.strip()+' '+prefix+'\n')

    except FileNotFoundError:  
        print(f"文件 {infilepath} 未找到。")
    # print(file_dict)
    return file_dict  

# 定义文件名
if len(sys.argv)<2:
    file_name = r"w2vdateset\english-test\data.tsv"  # 请将此文件名替换为你的实际文件名
    output_name = '/data/home/luxun/dataset/testset/manifest/data_eval.tsv.base'
elif len(sys.argv)==2:
    file_name=sys.argv[1] 
    output_name=file_name+'.we'
else:
    file_name=sys.argv[1]   
    output_name=sys.argv[2]   


read_ref_file_and_write_to_wenet(file_name,output_name)
# read_ref_file_and_write_to_wenet('ref.txt','kor_ref_we.txt')
# read_ref_file_and_write_to_wenet('evltest_8k_split_ref.txt','jpn_ref_we.txt')

