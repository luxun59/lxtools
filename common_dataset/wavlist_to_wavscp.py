import argparse
import os

def generate_utt_id(path, levels=0, sep='/'):
    path = os.path.normpath(path)
    parts = path.split(os.sep)
    filename = os.path.splitext(parts[-1])[0]

    if levels <= 0:
        return filename
    else:
        # 从倒数第 levels 个目录开始加上 filename
        start = max(0, len(parts) - (levels + 1))  # +1 是为了包括 filename
        selected = parts[start:-1] + [filename]
        return sep.join(selected)

def convert_wavlist_to_wavscp(wavlist_path, output_path, levels, sep):
    with open(wavlist_path, 'r', encoding='utf-8') as fin, \
         open(output_path, 'w', encoding='utf-8') as fout:
        for line in fin:
            wav_path = line.strip()
            if not wav_path:
                continue
            utt_id = generate_utt_id(wav_path, levels=levels, sep=sep)
            fout.write(f"{utt_id} {wav_path}\n")
    print(f"✅ 已生成 wav.scp：{output_path}")

def main():
    parser = argparse.ArgumentParser(description="将 wavlist 转为 wav.scp，支持自定义 ID 层级")
    parser.add_argument('--wavlist', required=True, help='包含完整路径的 wavlist 文件')
    parser.add_argument('--output', default='wav.scp', help='输出文件路径')
    parser.add_argument('--levels', type=int, default=0, help='用于构造 ID 的目录层级数(0 表示仅使用文件名)')
    parser.add_argument('--sep', default='/', help='路径片段拼接的分隔符(默认: /)')

    args = parser.parse_args()

    convert_wavlist_to_wavscp(args.wavlist, args.output, args.levels, args.sep)

if __name__ == '__main__':
    main()
