'''
Author: luxun luxun59@126.com
Date: 2025-04-08 19:55:49
LastEditors: luxun luxun59@126.com
LastEditTime: 2025-04-08 20:10:34
FilePath: \lxtools\common_dataset\volume_perturb_sox.py
Description: 

Copyright (c) 2025 by luxun59@126.com, All Rights Reserved. 
'''
import os
import argparse
import random
import subprocess

def apply_volume_perturb(input_path, output_path, volume_gain):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cmd = ["sox", input_path, output_path, "vol", f"{volume_gain}"]
    subprocess.run(cmd, check=True)

def parse_wav_list(wav_file):
    with open(wav_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    entries = []
    for line in lines:
        parts = line.strip().split()
        if len(parts) == 2:
            utt_id, path = parts
        else:
            # fallback: use full path as utt_id
            path = line.strip()
            utt_id = os.path.splitext(os.path.basename(path))[0]
        entries.append((utt_id, path))
    return entries

def main():
    parser = argparse.ArgumentParser(description="基于 SoX 的音量扰动脚本")
    parser.add_argument('--input', required=True, help='输入 wav.scp 或 wavlist 文件')
    parser.add_argument('--input-text', default=None, help='输入文本文件（可选）')
    parser.add_argument('--output-dir', required=True, help='输出目录')
    parser.add_argument('--output-wavscp', default='wav_perturbed.scp', help='输出的 wav.scp 文件')
    parser.add_argument('--output-text', default=None, help='输出文本文件（可选）')
    parser.add_argument('--min-gain', type=float, default=0.8, help='最小音量增益因子（与 volume-factors 互斥）')
    parser.add_argument('--max-gain', type=float, default=1.2, help='最大音量增益因子（与 volume-factors 互斥）')
    parser.add_argument('--volume-factors', type=str, default=None, help='逗号分隔的增益值列表，例如: 0.8,1.0,1.2')
    parser.add_argument('--select-mode', choices=['random', 'round_robin'], default='random',
                        help='当使用 volume-factors 时的选择方式（默认: random）')
    parser.add_argument('--seed', type=int, default=42, help='随机种子（用于 random 模式）')

    args = parser.parse_args()
    random.seed(args.seed)

    entries = parse_wav_list(args.input)

    # 使用 volume_factors 模式
    if args.volume_factors:
        factors = [float(f.strip()) for f in args.volume_factors.split(',')]
        if args.select_mode == 'random':
            gains = [random.choice(factors) for _ in entries]
        else:  # round robin
            gains = [factors[i % len(factors)] for i in range(len(entries))]
    else:
        # 使用 min-max 范围随机扰动
        gains = [round(random.uniform(args.min_gain, args.max_gain), 3) for _ in entries]

    if args.input_text and args.output_text:    
        with open(args.input_text, 'r', encoding='utf-8') as fin:
            
            text_mapping = {}
            for line in fin:
                parts = line.strip().split(maxsplit=1)
                if len(parts) == 2:
                    utt_id, text = parts
                    text_mapping[utt_id] = text
        fout_text = open(args.output_text, 'w', encoding='utf-8')

    with open(args.output_wavscp, 'w', encoding='utf-8') as out_scp:
        for (utt_id, input_path), gain in zip(entries, gains):
            gains_str = f"{gains:.1f}"
            new_utt_id = f"{utt_id}_vol{gains_str.replace('.', '')}"
            output_path = os.path.join(args.output_dir, f"{new_utt_id}.wav")
            print(f"📢 处理 {utt_id} | 增益: {gain}")
            apply_volume_perturb(input_path, output_path, gain)
            out_scp.write(f"{new_utt_id} {output_path}\n")
            if args.input_text and args.output_text: 
                if utt_id in text_mapping:
                    fout_text.write(f"{new_utt_id} {text_mapping[utt_id]}\n")
                else:
                    print(f"⚠️  未找到文本: {utt_id}")
                
    print(f"✅ 处理完成，输出到：{args.output_dir}")
    print(f"📄 新 wav.scp：{args.output_wavscp}")
    if args.input_text and args.output_text:
        print(f"📄 新文本文件：{args.output_text}")
        fout_text.close()

if __name__ == '__main__':
    main()
