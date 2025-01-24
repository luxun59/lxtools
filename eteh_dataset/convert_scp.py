import os
import subprocess
import sys

args = sys.argv

wav_scp_path = sys.argv[1]
wav_scp_new_path = sys.argv[2]

output_dir = '/home/mydata/dataEnv/dataEnv/XUJI8k'  # 转换后的音频文件保存目录


# 读取 wav.scp 文件
with open(wav_scp_path, 'r') as f:
    with open(wav_scp_new_path, 'w') as fout:
        for line in f:
            # 解析每一行的 id 和 path
            id, path = line.strip().split(maxsplit=1)

            wav_name = os.path.basename(path)
            # 构建输出文件路径
            new_path = os.path.join(output_dir, wav_name)
            fout.write(f"{id} {new_path}\n")