import sys
import os
import random


source_name=sys.argv[1] #源域文件名
target_name=sys.argv[2] #目标域文件名
output_name=sys.argv[3] #输出文件名
target_percent=float(sys.argv[4])  #目标域数据比例



# source_wavscp = os.path.join(source_name,".wav.scp")
# source_text = os.path.join(source_name,".text")

# target_wavscp = os.path.join(target_name,".wav.scp")
# target_text = os.path.join(target_name,".text")

# output_wavscp = os.path.join(output_name,".wav.scp")
# output_text = os.path.join(output_name,".text")

source_wavscp = source_name+".wav.scp"
source_text = source_name+".text"

target_wavscp = target_name+".wav.scp"
target_text = target_name+".text"

output_wavscp = output_name+".wav.scp"
output_text = output_name+".text"


source_num=0

rand = random.Random(42)

dict_source_wavscp={}
dict_target_wavscp={}

with open(target_wavscp,"r",encoding="utf-8") as f:
    target_wavscp_lines = f.readlines()
    target_num=len(target_wavscp_lines)
    for line in target_wavscp_lines:
        line=line.strip()
        parts=line.split(" ")
        if len(parts)<2:
            continue
        dict_target_wavscp[parts[0]]=parts[1]

source_output_num=int(target_num*(1-target_percent)/target_percent)

with open(source_wavscp,"r",encoding="utf-8") as f:
    source_wavscp_lines = f.readlines()
    source_num = len(source_wavscp_lines)
    split_percent = source_output_num/source_num
    if split_percent>1:
        print("source num is too small, all data will be used!")
        split_percent=1
    for line in source_wavscp_lines:
        line=line.strip()
        parts=line.split(" ")
        if len(parts)<2:
            continue
        if rand.random() > split_percent:
            continue
        dict_source_wavscp[parts[0]]=parts[1]



# merged_dict = {**dict_source_wavscp, **dict_target_wavscp}


with open(output_wavscp,"w",encoding="utf-8") as fout:
    for key in dict_source_wavscp:
        fout.write(key+" "+dict_source_wavscp[key]+"\n")
    for key in dict_target_wavscp:
        fout.write(key+" "+dict_target_wavscp[key]+"\n")



with open(output_text,"w",encoding="utf-8") as fout:
    with open(target_text,"r",encoding="utf-8") as f:
        target_text_lines = f.readlines()
        for line in target_text_lines:
            line=line.strip()
            parts=line.split(" ")
            if parts[0] in dict_target_wavscp:
                fout.write(line+"\n")
    with open(source_text,"r",encoding="utf-8") as f:
        source_text_lines = f.readlines()
        for line in source_text_lines:
            line=line.strip()
            parts=line.split(" ")
            if parts[0] in dict_source_wavscp:
                fout.write(line+"\n")














