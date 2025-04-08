#!/bin/bash

# 用法: ./convert_wav.sh wavlist.txt output_folder

wavlist=$1
output_dir=$2

# 创建输出目录（如果不存在）
mkdir -p "$output_dir"

# 遍历 wavlist 文件中的每一行
while IFS= read -r wavfile; do
  if [[ -f "$wavfile" ]]; then
    filename=$(basename "$wavfile")
    output_file="$output_dir/$filename"

    echo "正在转换: $wavfile -> $output_file"

    # 转换为 8kHz, 16-bit, mono 的 PCM WAV 格式
    sox "$wavfile" -r 8000 -b 16 -c 1 "$output_file"
  else
    echo "文件不存在: $wavfile"
  fi
done < "$wavlist"





