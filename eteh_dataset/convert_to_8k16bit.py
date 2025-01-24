import os
import subprocess
import sys

args = sys.argv

wav_scp_path = sys.argv[1]
output_dir = sys.argv[2]
# 定义输入和输出目录
# wav_scp_path = 'wav.scp'  # 输入的 wav.scp 文件路径
# output_dir = 'output_wavs'  # 转换后的音频文件保存目录

# 确保输出目录存在
os.makedirs(output_dir, exist_ok=True)

# 读取 wav.scp 文件
with open(wav_scp_path, 'r') as f:
    for line in f:
        # 解析每一行的 id 和 path
        id, path = line.strip().split(maxsplit=1)

        wav_name = os.path.basename(path)
        # 构建输出文件路径
        output_path = os.path.join(output_dir, wav_name)

        if os.path.exists(output_path):
            print(f"Skip {path}")
            continue        

        # 使用 sox 命令进行音频转换
        sox_command = f"sox {path} -r 8000 -b 16 {output_path}"
        
        # 执行 sox 命令
        try:
            subprocess.run(sox_command, shell=True, check=True)
            print(f"Converted {path} to {output_path}")
        except subprocess.CalledProcessError as e:
            print(f"Error converting {path}: {e}")