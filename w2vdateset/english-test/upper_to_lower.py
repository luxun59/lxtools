'''
Author: luxun luxun59@126.com
Date: 2024-12-31 10:30:19
LastEditors: luxun luxun59@126.com
LastEditTime: 2024-12-31 10:30:34
FilePath: \lxtools\w2vdateset\english-test\upper_to_lower.py
Description: 

Copyright (c) 2024 by luxun59@126.com, All Rights Reserved. 
'''



import os,sys
def read_lines(path, encoding="utf-8"):
    with open(path, "r", encoding=encoding) as fd:
        lines = fd.readlines()
    return lines

def write_lines(path, lines, encoding="utf-8"):
    with open(path, "w", encoding=encoding) as fd:
        fd.writelines(lines)

if __name__=="__main__":
    texts=[]
    file=sys.argv[1]
    lines=read_lines(file)
    for line in lines:
        text = line.lower()
        texts.append(text)
    write_lines(file+"-1", texts)







