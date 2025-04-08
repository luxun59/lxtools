'''
Author: luxun luxun59@126.com
Date: 2025-04-08 15:32:45
LastEditors: luxun luxun59@126.com
LastEditTime: 2025-04-08 15:36:49
FilePath: \lxtools\common_dataset\filter_text.py
Description: 

Copyright (c) 2025 by luxun59@126.com, All Rights Reserved. 
'''
import argparse

def load_filter_ids(filter_file):
    with open(filter_file, 'r', encoding='utf-8') as f:
        return [line.strip().split()[0] for line in f if line.strip()]

def filter_text(text_file, filter_ids, strict=False, preserve_order=False, mode='include'):
    filter_set = set(filter_ids)
    filtered_lines = {}

    with open(text_file, 'r', encoding='utf-8') as fin:
        for line in fin:
            if not line.strip():
                continue
            parts = line.strip().split(maxsplit=1)
            if not parts:
                continue
            id_ = parts[0]
            matched = (id_ in filter_set) if mode == 'include' else (id_ not in filter_set)
            if matched:
                filtered_lines[id_] = line if not strict else f"{id_} {parts[1] if len(parts) > 1 else ''}\n"

    if preserve_order and mode == 'include':
        return [filtered_lines[id_] for id_ in filter_ids if id_ in filtered_lines]
    else:
        return list(filtered_lines.values())

def main():
    parser = argparse.ArgumentParser(description="筛选 text 文件中包含或排除指定 ID 的行")
    parser.add_argument('--text', required=True, help='输入的 text 文件（每行: id text）')
    parser.add_argument('--filter', required=True, help='包含要保留/排除 ID 的文件')
    parser.add_argument('--output', default='filtered_text', help='输出文件路径')
    parser.add_argument('--strict', action='store_true', help='只保留 id + text（丢弃 filter 多余列）')
    parser.add_argument('--preserve_order', action='store_true', help='按 filter 文件中 ID 顺序输出（仅正向匹配下有效）')
    parser.add_argument('--mode', choices=['include', 'exclude'], default='include',
                        help='匹配模式: include (保留在 filter 中的 ID) 或 exclude (排除在 filter 中的 ID)')

    args = parser.parse_args()

    filter_ids = load_filter_ids(args.filter)
    filtered = filter_text(
        args.text,
        filter_ids,
        strict=args.strict,
        preserve_order=args.preserve_order,
        mode=args.mode
    )

    with open(args.output, 'w', encoding='utf-8') as fout:
        fout.writelines(filtered)

    print(f"✅ 筛选完成，输出文件保存为：{args.output}")


if __name__ == '__main__':
    main()

