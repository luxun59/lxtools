'''
Author: luxun luxun59@126.com
Date: 2024-10-25 15:03:30
LastEditors: luxun luxun59@126.com
LastEditTime: 2024-11-07 20:45:38
FilePath: \lxtools\w2vdateset\english-test\get_tsv_to_line.py
Description: 

Copyright (c) 2024 by luxun59@126.com, All Rights Reserved. 
'''

import sys


# 定义文件名
if len(sys.argv)==1:
    file_name = r"w2vdateset\english-test\data.tsv"  # 请将此文件名替换为你的实际文件名
else:
    file_name=sys.argv[1]   


outfile_name = file_name+'.base'


# 打开文件并逐行读取
with open(file_name, 'r', encoding='utf-8') as file ,open(
    outfile_name,'w',encoding='utf-8') as outputfile:
    next(file)
    for line_number, line in enumerate(file, start=0):
        file_name=line.split(" ")[0]
        basename=file_name.split('/')[-1].split('.')[0]
        print(basename+" "+"None-{}".format(line_number),file=outputfile)


