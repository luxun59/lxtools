import argparse
import os
import re



dict_files_path=r'C:\Users\luxun\Desktop\testdata\ted3_hubert_hypo.word.we.name'
filepath=r'E:\ASR\english\NLP\trans\ted3_mms.txt'
outfile_path='ted3_post_hubert.txt'

def read_ref_file(filepath):  
    """  
    读取ref.txt文件并返回一个字典，键是文件名，值是该文件名所在行的前面字符串和行号。  
    """  
    file_dict = {}  
    try:  
        with open(filepath, 'r', encoding='utf-8') as file:  
            lines = file.readlines()  
            for line_num, line in enumerate(lines, start=1):  
                transes = line.split('\t')
                file_dict[transes[0].strip()]=' '.join(transes[1:])
    except FileNotFoundError:  
        print(f"文件 {filepath} 未找到。")
    # print((file_dict))
    return file_dict  



with open(filepath, 'r', encoding='utf-8') as file, open(
    outfile_path,'w',encoding='utf-8' ) as outfile:  
    lines = file.readlines()  
    filedict=read_ref_file(dict_files_path)
    for line_num, line in enumerate(lines, start=1):  
        whispertxt = line.split(' ')[0]
        whispertxt = line.strip()
        print(whispertxt)
        if whispertxt in filedict:
            # outfile.writelines(whispertxt+' '+filedict[whispertxt])
            print(whispertxt+' '+filedict[whispertxt])
            print(whispertxt+' '+filedict[whispertxt].strip(),file=outfile)




