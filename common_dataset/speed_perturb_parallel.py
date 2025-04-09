import os
import subprocess
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, help='Input wav.scp file')
    parser.add_argument('--input_text', type=str, default=None, help='Input text file')
    parser.add_argument('--output_dir', type=str, help='Output directory for perturbed wavs')
    parser.add_argument('--output_scp', type=str, help='Output wav.scp file path')
    parser.add_argument('--output_text', type=str, default=None, help='Output text file path')
    parser.add_argument('--speed_factors', type=float, default=[1.1], nargs='+', help='Speed factors for perturbation')
    parser.add_argument('--num_workers', type=int, default=4, help='Number of threads to use')
    return parser.parse_args()

def run_sox(wav_id, wav_path, speed, output_dir, text_mapping=None):
    speed_str = f"{speed:.1f}"
    new_id = f"{wav_id}_sp{speed_str.replace('.', '')}"
    output_path = os.path.join(output_dir, f"{new_id}.wav")

    # 自动创建输出目录（递归创建）
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    cmd = ['sox', wav_path, output_path, 'speed', str(speed), 'rate', '8k']

    try:
        print(f"Running: {' '.join(cmd)}")
        subprocess.run(cmd, check=True)
        text = text_mapping.get(wav_id) if text_mapping else None
        return new_id, output_path, text
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Sox failed for {wav_path} at speed {speed}: {e}")
        return None

def main():
    args = parse_args()
    os.makedirs(args.output_dir, exist_ok=True)

    # Load text mapping if provided
    text_mapping = {}
    if args.input_text and args.output_text:
        with open(args.input_text, 'r') as tf:
            for line in tf:
                parts = line.strip().split(maxsplit=1)
                if len(parts) == 2:
                    utt_id, text = parts
                    text_mapping[utt_id] = text

    # Prepare tasks
    tasks = []
    with open(args.input, 'r') as fin:
        for line in fin:
            utt_id, wav_path = line.strip().split(maxsplit=1)
            for speed in args.speed_factors:
                tasks.append((utt_id, wav_path, speed))

    results = []

    # Run in multithreading
    with ThreadPoolExecutor(max_workers=args.num_workers) as executor:
        future_to_task = {
            executor.submit(run_sox, utt_id, wav_path, speed, args.output_dir, text_mapping): (utt_id, speed)
            for utt_id, wav_path, speed in tasks
        }

        for future in as_completed(future_to_task):
            result = future.result()
            if result:
                results.append(result)

    # Write wav.scp and text if needed
    with open(args.output_scp, 'w') as scp_f:
        for new_id, output_path, _ in results:
            scp_f.write(f"{new_id} {output_path}\n")

    if args.output_text:
        with open(args.output_text, 'w') as text_f:
            for new_id, _, text in results:
                if text:
                    text_f.write(f"{new_id} {text}\n")
                else:
                    print(f"Warning: No text found for {new_id}")

    print(f"✅ 完成！共生成 {len(results)} 条增强数据。")

if __name__ == '__main__':
    main()
