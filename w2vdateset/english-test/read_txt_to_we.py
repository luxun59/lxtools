'''
Author: luxun luxun59@126.com
Date: 2024-12-31 10:27:58
LastEditors: luxun luxun59@126.com
LastEditTime: 2024-12-31 10:29:40
FilePath: \lxtools\w2vdateset\english-test\read_txt_to_we.py
Description: 

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
                match = re.search(r'\((.*)\)', line)  
                # print("line",line)
                if match:  
                    filename = match.group(1)  
                    filename = os.path.basename(filename)
                    prefix = line[:match.start()].strip()  
                    file_dict[filename.strip()] = prefix
                    outfile.writelines(filename.strip()+' '+prefix+'\n')

    except FileNotFoundError:  
        print(f"文件 {infilepath} 未找到。")
    # print(file_dict)
    return file_dict  


# 定义文件名
if len(sys.argv)==0:
    input_file_name = r"w2vdateset\english-test\data.tsv"  # 请将此文件名替换为你的实际文件名
    output_file_name = input_file_name+'.base'
else:
    input_file_name=sys.argv[1]   
    output_file_name=sys.argv[2]   

read_ref_file_and_write_to_wenet(input_file_name,output_file_name)
# read_ref_file_and_write_to_wenet('ref.txt','kor_ref_we.txt')
# read_ref_file_and_write_to_wenet('evltest_8k_split_ref.txt','jpn_ref_we.txt')


