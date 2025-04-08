'''
Author: luxun luxun59@126.com
Date: 2025-04-08 15:19:59
LastEditors: luxun luxun59@126.com
LastEditTime: 2025-04-08 15:43:26
FilePath: \lxtools\common_dataset\speed_perturb.py
Description: 

Copyright (c) 2025 by luxun59@126.com, All Rights Reserved. 
'''
import os
import subprocess
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, help='Input wav.scp file')
parser.add_argument('--input_text', type=str,default=None, help='Input text file')
parser.add_argument('--output_dir', type=str, help='Output directory for perturbed wavs')
parser.add_argument('--output_scp', type=str, help='Output wav.scp file path')
parser.add_argument('--output_text', type=str,default=None, help='Output text file path')
parser.add_argument('--speed_factors', type=float, default=[1.1] ,nargs='+', help='Speed factors for perturbation')
args = parser.parse_args()

# Set the values from command line arguments
wav_scp = args.input
output_dir = args.output_dir
output_scp = args.output_scp
speed_factors = args.speed_factors
text_file = args.input_text
output_text = args.output_text
output_text_file = None 

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)
# Read the text file and create a dictionary for text mapping
if text_file and output_text:
    text_mapping = {}
    with open(text_file, 'r') as fin:
        for line in fin:
            parts = line.strip().split(maxsplit=1)
            if len(parts) == 2:
                utt_id, text = parts
                text_mapping[utt_id] = text
    output_text_file= open(output_text, 'w')

with open(wav_scp, 'r') as fin, open(output_scp, 'w') as fout:
    for line in fin:
        utt_id, wav_path = line.strip().split(maxsplit=1)
        
        for speed in speed_factors:
            speed_str = f"{speed:.1f}"
            new_utt_id = f"{utt_id}_sp{speed_str.replace('.', '')}"
            output_path = os.path.join(output_dir, f"{new_utt_id}.wav")
            
            # Construct sox command
            cmd = [
                'sox', wav_path, output_path,
                'speed', str(speed),
                'rate', '8k'  # Ensure sample rate remains the same (change to your desired rate)
            ]

            print(f"Running: {' '.join(cmd)}")
            subprocess.run(cmd, check=True)

            # Write new wav.scp entry
            fout.write(f"{new_utt_id} {output_path}\n")
            if output_text_file is not None:
                # Write new text entry
                if utt_id in text_mapping:
                    new_text = text_mapping[utt_id]
                    output_text_file.write(f"{new_utt_id} {new_text}\n")
                else:
                    print(f"Warning: No text found for {utt_id}, skipping text entry.")
