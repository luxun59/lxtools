'''
Author: luxun luxun59@126.com
Date: 2024-12-24 16:28:05
LastEditors: luxun luxun59@126.com
LastEditTime: 2024-12-24 16:36:33
FilePath: \lxtools\eteh_dataset\process_clovacall.py
Description: 

Copyright (c) 2024 by luxun59@126.com, All Rights Reserved. 
'''




import os
import json

def remove_punctuation(text):
    return text.replace(".", "").replace("?", "").replace("!", "").replace(",", "").replace(";", "").replace(":", "").replace("(", "").replace(")", "").replace("'", "").replace("\"", "").replace("'", "").replace("\"", "")


def process_clovacall_data(json_path, wav_dir, output_dir):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    wav_scp_dict = {}
    text_dict = {}

    # Read and process the JSON file
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    for item in data:
        wav_name = item['wav']
        text = item['text']
        text=remove_punctuation(text)
        speaker_id = item['speaker_id']
        
        # Create utterance ID from wav name
        # utt_id = os.path.splitext(wav_name)[0]
        utt_id=os.path.basename(wav_name)
        
        # Get full path to wav file
        wav_path = os.path.join(wav_dir, wav_name)
        if not os.path.exists(wav_path):
            print(f"Warning: WAV file not found: {wav_path}")
            continue
            
        wav_scp_dict[utt_id] = wav_path
        text_dict[utt_id] = text

    # Write wav.scp
    with open(os.path.join(output_dir, "wav.scp"), "w", encoding="utf-8") as f:
        for key, value in wav_scp_dict.items():
            f.write(f"{key} {value}\n")
            
    # Write text file
    with open(os.path.join(output_dir, "text"), "w", encoding="utf-8") as f:
        for key, value in text_dict.items():

            f.write(f"{key} {value}\n")
            
    return wav_scp_dict, text_dict

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python process_clovacall.py <json_file> <wav_dir> <output_dir>")
        sys.exit(1)
        
    json_path = sys.argv[1]
    wav_dir = sys.argv[2]
    output_dir = sys.argv[3]
    
    wav_scp_dict, text_dict = process_clovacall_data(json_path, wav_dir, output_dir)















