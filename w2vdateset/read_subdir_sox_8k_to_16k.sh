#!/bin/bash  
###
 # @Author: luxun luxun59@126.com
 # @Date: 2024-10-21 11:30:57
 # @LastEditors: luxun luxun59@126.com
 # @LastEditTime: 2024-10-22 09:49:12
 # @FilePath: \lxtools\w2vdateset\read_subdir_sox_8k_to_16k.sh
 # @Description: 
 # 
 # Copyright (c) 2024 by luxun59@126.com, All Rights Reserved. 
### 
  
# 检查是否提供了顶级目录和新文件夹参数  
if [ "$#" -ne 2 ]; then  
  echo "Usage: $0 <source_directory> <destination_directory>"  
  exit 1  
fi  
  
SOURCE_DIR="$1"  
DEST_DIR="$2"  
  
# 检查顶级目录是否存在  
if [ ! -d "$SOURCE_DIR" ]; then  
  echo "Error: Source directory '$SOURCE_DIR' does not exist."  
  exit 1  
fi  
  
# 创建新文件夹（如果不存在）  
mkdir -p "$DEST_DIR"  
  
# 查找所有 .wav 文件并转换采样率  
find "$SOURCE_DIR" -type f -name "*.wav" | while read -r FILE; do  
  # 获取文件名（不包括路径）  
  BASENAME=$(basename "$FILE")  
    
  # 构建新文件的完整路径  
  NEW_FILE="$DEST_DIR/$BASENAME"  
    
  # 使用 ffmpeg 转换采样率到 16kHz  
  sox "$FILE" -r 16000 "$NEW_FILE"  
    
  # 检查 ffmpeg 是否成功  
  if [ $? -ne 0 ]; then  
    echo "Error converting file: $FILE"  
  else  
    echo "Converted file: $FILE -> $NEW_FILE"  
  fi  
done