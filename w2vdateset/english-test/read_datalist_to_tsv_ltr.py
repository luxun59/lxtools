'''
Author: luxun luxun59@126.com
Date: 2024-10-25 15:03:30
LastEditors: luxun luxun59@126.com
LastEditTime: 2024-10-28 11:27:32
FilePath: \lxtools\w2vdateset\english-test\read_datalist_to_tsv_ltr.py
Description: 

Copyright (c) 2024 by luxun59@126.com, All Rights Reserved. 
'''
import argparse
import os
import re


filepath=r"C:\Users\luxun\OneDrive\document\learn\lxtools\w2vdateset\english-test\data.list"

tsvfile=filepath.split(".")[0]+".tsv"
wrdfile=filepath.split(".")[0]+".wrd"
ltrfile=filepath.split(".")[0]+".ltr"

try:  
    with open(filepath, 'r', encoding='utf-8') as file,open(
        tsvfile,"w",encoding='utf-8') as tsv,open(
        ltrfile,"w",encoding='utf-8') as ltr,open(
        wrdfile,"w",encoding='utf-8') as wrd:  
        lines = file.readlines()  
        for line_num, line in enumerate(lines, start=1):  
            dict_line=eval(line) 
            print("dict_line",dict_line)
            print("dict_line",type(dict_line))
            wavpath=dict_line["wav"]
            txt=dict_line["txt"]
            print("wavpath",type(wavpath))
            print(wavpath,file=tsv)
            print(txt,file=wrd)
            print(
                " ".join(list(txt.replace(" ", "|"))) + " |",
                file=ltr,
            )


except FileNotFoundError:  
    print(f"文件 {filepath} 未找到。")






