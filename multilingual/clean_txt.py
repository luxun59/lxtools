




import string

import argparse
import os
import re
import sys

def remove_punctuation_except_apostrophe(s):
    # 获取所有标点符号
    all_punctuation = set(string.punctuation)
    # 保留英文省略形式所需的 '
    allowed_punctuation = {"'"}
    # 得到需要移除的标点符号
    punctuation_to_remove = all_punctuation - allowed_punctuation
    result = ""
    for char in s:
        if char in punctuation_to_remove:
            # 如果是需要移除的标点，替换为空格
            result += " "
        else:
            # 否则保留原字符
            result += char
    return result






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
                line = line.strip()
                match = re.search(r'\((.*)\)', line)  
                # print("line",line)
                if match:  
                    filename = match.group(1)  
                    # filename = os.path.basename(filename)
                    prefix = line[:match.start()].strip()  
                    prefix = remove_punctuation_except_apostrophe(prefix)
                    file_dict[filename.strip()] = prefix
                    # outfile.writelines(filename.strip()+' '+prefix+'\n')
                    outfile.writelines("{}({})\n".format(prefix,filename))

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









