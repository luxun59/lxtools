#!/bin/bash

# 用法: ./split_random_ratio.sh input.txt part1.txt part2.txt 0.8

input_file=$1
part1=$2
part2=$3
ratio=$4  # 示例：0.8 表示前 80%

total_lines=$(wc -l < "$input_file")
split_lines=$(awk -v total="$total_lines" -v r="$ratio" 'BEGIN { printf("%d", total * r) }')

# shuf "$input_file" | tee >(head -n "$split_lines" > "$part1") | tail -n +"$((split_lines + 1))" > "$part2"

# 打乱并保存到临时文件
tmpfile=$(mktemp)
shuf "$input_file" > "$tmpfile"

# 分割
head -n "$split_lines" "$tmpfile" > "$part1"
tail -n +"$((split_lines + 1))" "$tmpfile" > "$part2"


echo "total_lines:$total_lines"


echo "✅ $input_file ($total_lines) 已按比例 $ratio 分为两份：$part1 ($split_lines 行), $part2"
