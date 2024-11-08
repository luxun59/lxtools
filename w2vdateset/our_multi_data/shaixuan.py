import argparse
import os
import re


dict_files_path='out/jpn_ref_we.txt'
filepath='evl.txt'
outfile_path='out/jpn_evl_post.txt'

def read_ref_file(filepath):  
    """  
    读取ref.txt文件并返回一个字典，键是文件名，值是该文件名所在行的前面字符串和行号。  
    """  
    file_dict = {}  
    try:  
        with open(filepath, 'r', encoding='utf-8') as file:  
            lines = file.readlines()  
            for line_num, line in enumerate(lines, start=1):  
                transes = line.split(' ')
                file_dict[transes[0]]=transes[1]
    except FileNotFoundError:  
        print(f"文件 {filepath} 未找到。")
    # print(file_dict)
    return file_dict  



with open(filepath, 'r', encoding='utf-8') as file, open(
    outfile_path,'w',encoding='utf-8' ) as outfile:  
    lines = file.readlines()  
    filedict=read_ref_file(dict_files_path)
    for line_num, line in enumerate(lines, start=1):  
        whispertxt = line.split(' ')
        if whispertxt[0] in filedict:
            outfile.writelines(line)




