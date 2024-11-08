
###
 # @Author: luxun luxun59@126.com
 # @Date: 2024-10-26 10:07:55
 # @LastEditors: luxun luxun59@126.com
 # @LastEditTime: 2024-10-26 10:12:14
 # @FilePath: \lxtools\w2vdateset\gigaspeech\untar-shard-list.sh
 # @Description: 
 # 
 # Copyright (c) 2024 by luxun59@126.com, All Rights Reserved. 
### 
#!/bin/bash  
## 输入 xxx_data_raw.list 格式每行为  dev/shards_000000005类似 dev为文件夹，shards_000000005为tar包的无后缀basename
##

# 定义文件名列表文件和解压目标目录  
# filelist="dev_data_raw.list"  
# output_dir="giga_shards_raw"  
# tar_dir='giga_shards'



# 定义文件名列表文件和解压目标目录  
root=/data/home/wangxuyang/datasets/gigaspeech/raw_data_scripts
filelist="dev_data_raw.list"  
output_dir="/data/home/wangxuyang/datasets/gigaspeech/giga_shards_raw"  

tar_dir='/data/home/wangxuyang/datasets/gigaspeech/giga_shards'




# 确保输出目录存在  
mkdir -p "$output_dir"  
  
# 读取文件名列表文件，并逐行处理  
while IFS= read -r filename; do  
  # 检查文件名是否为空（处理空行的情况）  
  if [ -n "$filename" ]; then  
    # 构造压缩文件的完整路径（假设与filelist.txt在同一目录下）  
    compressed_file="$filename"  
    # 检查压缩文件是否存在  
    if [ -f "$tar_dir/$compressed_file.tar" ]; then  
      # 解压文件到目标目录  
      echo "正在解压 $compressed_file 到 $output_dir"  
      mkdir -p "$output_dir/$compressed_file"
      tar -xf ${tar_dir}/$compressed_file.tar -C $output_dir/$compressed_file
    else  
      echo "文件不存在: $compressed_file"  
    fi  
  fi  
done < "$filelist"  
  
echo "所有文件已解压完毕。"












