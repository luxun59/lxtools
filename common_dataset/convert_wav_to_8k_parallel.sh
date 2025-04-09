#!/bin/bash

# 用法: ./convert_wav_parallel_native.sh wavlist.txt output_folder [num_jobs]
wavlist=$1
output_dir=$2
num_jobs=${3:-4}  # 默认并发数为 4

mkdir -p "$output_dir"

# 定义转换函数
convert_wav() {
  wavfile="$1"
  if [[ -f "$wavfile" ]]; then
    filename=$(basename "$wavfile")
    output_file="$output_dir/$filename"
    echo "转换中: $wavfile -> $output_file"
    sox "$wavfile" -r 8000 -b 16 -c 1 "$output_file"
  else
    echo "文件不存在: $wavfile"
  fi
}

# 控制最大并发数的函数
sem() {
  while (( $(jobs -rp | wc -l) >= num_jobs )); do
    sleep 0.5
  done
}

# 遍历每一行并并发处理
while IFS= read -r wavfile; do
  sem  # 控制并发数量
  convert_wav "$wavfile" &
done < "$wavlist"

wait  # 等待所有任务结束
echo "✅ 全部转换完成"
