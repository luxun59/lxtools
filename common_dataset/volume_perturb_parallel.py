import os
import argparse
import random
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed

def apply_volume_perturb(input_path, output_path, volume_gain):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cmd = ["sox", input_path, output_path, "vol", f"{volume_gain}"]
    try:
        subprocess.run(cmd, check=True)
        return True
    except subprocess.CalledProcessError:
        print(f"❌ sox 处理失败: {input_path}")
        return False

def parse_wav_list(wav_file):
    with open(wav_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    entries = []
    for line in lines:
        parts = line.strip().split()
        if len(parts) == 2:
            utt_id, path = parts
        else:
            path = line.strip()
            utt_id = os.path.splitext(os.path.basename(path))[0]
        entries.append((utt_id, path))
    return entries

def main():
    parser = argparse.ArgumentParser(description="基于 SoX 的音量扰动脚本（多线程版）")
    parser.add_argument('--input', required=True, help='输入 wav.scp 或 wavlist 文件')
    parser.add_argument('--input-text', default=None, help='输入文本文件（可选）')
    parser.add_argument('--output-dir', required=True, help='输出目录')
    parser.add_argument('--output-wavscp', default='wav_perturbed.scp', help='输出的 wav.scp 文件')
    parser.add_argument('--output-text', default=None, help='输出文本文件（可选）')
    parser.add_argument('--min-gain', type=float, default=0.8, help='最小音量增益因子（与 volume-factors 互斥）')
    parser.add_argument('--max-gain', type=float, default=1.2, help='最大音量增益因子（与 volume-factors 互斥）')
    parser.add_argument('--volume-factors', type=str, default=None, help='逗号分隔的增益值列表，例如: 0.8,1.0,1.2')
    parser.add_argument('--select-mode', choices=['random', 'round_robin'], default='random', help='volume-factors 模式下的选择方式')
    parser.add_argument('--seed', type=int, default=42, help='随机种子')
    parser.add_argument('--num-workers', type=int, default=4, help='线程数')

    args = parser.parse_args()
    random.seed(args.seed)

    entries = parse_wav_list(args.input)

    # 确定增益因子
    if args.volume_factors:
        factors = [float(f.strip()) for f in args.volume_factors.split(',')]
        if args.select_mode == 'random':
            gains = [random.choice(factors) for _ in entries]
        else:
            gains = [factors[i % len(factors)] for i in range(len(entries))]
    else:
        gains = [round(random.uniform(args.min_gain, args.max_gain), 3) for _ in entries]

    # 加载文本映射（可选）
    text_mapping = {}
    if args.input_text and args.output_text:
        with open(args.input_text, 'r', encoding='utf-8') as fin:
            for line in fin:
                parts = line.strip().split(maxsplit=1)
                if len(parts) == 2:
                    utt_id, text = parts
                    text_mapping[utt_id] = text

    os.makedirs(args.output_dir, exist_ok=True)

    results = []

    def process_entry(entry, gain):
        utt_id, input_path = entry
        gain_str = f"{gain:.1f}"
        new_utt_id = f"{utt_id}_vol{gain_str.replace('.', '')}"
        output_path = os.path.join(args.output_dir, f"{new_utt_id}.wav")
        print(f"🎧 处理 {utt_id} | 增益: {gain}")
        success = apply_volume_perturb(input_path, output_path, gain)
        if success:
            text = text_mapping.get(utt_id) if text_mapping else None
            return new_utt_id, output_path, text
        return None

    # 多线程处理
    with ThreadPoolExecutor(max_workers=args.num_workers) as executor:
        futures = [
            executor.submit(process_entry, entry, gain)
            for entry, gain in zip(entries, gains)
        ]
        for future in as_completed(futures):
            result = future.result()
            if result:
                results.append(result)

    # 写输出文件
    with open(args.output_wavscp, 'w', encoding='utf-8') as fscp:
        for new_id, path, _ in results:
            fscp.write(f"{new_id} {path}\n")

    if args.output_text and text_mapping:
        with open(args.output_text, 'w', encoding='utf-8') as ftxt:
            for new_id, _, text in results:
                if text:
                    ftxt.write(f"{new_id} {text}\n")
                else:
                    print(f"⚠️ 文本缺失: {new_id}")

    print(f"✅ 完成，共处理 {len(results)} 条音频。")
    print(f"📄 输出 wav.scp: {args.output_wavscp}")
    if args.output_text:
        print(f"📄 输出 text: {args.output_text}")

if __name__ == '__main__':
    main()
