

import os
import re
import wave
from pydub import AudioSegment
import glob

def process_kcsc_data(txt_path, wav_dir, output_dir):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    wav_scp_dict={}
    text_dict={}

    # Read and process the text file
    with open(txt_path, 'r', encoding='utf-8') as f:
        for i,line in enumerate(f):
            line = line.strip()
            if not line:
                continue
                
            # Extract time stamps and utterance ID using regex
            match = re.match(r'\[([\d.]+),([\d.]+)\]\s+(\w+)', line)
            if not match:
                continue
                
            start_time = float(match.group(1))
            end_time = float(match.group(2))
            utt_id = match.group(3)
            key=f"{wav_base_name}_{i}"

            # Find corresponding wav file
            wav_base_name=os.path.basename(txt_path).split(".")[0]
            wav_path = os.path.join(wav_dir, f"{wav_base_name}.wav")
            if not os.path.exists(wav_path):
                print(f"Warning: WAV file not found for {utt_id}")
                continue
                
            # Load audio file
            audio = AudioSegment.from_wav(wav_path)
            
            # Convert time to milliseconds
            start_ms = int(start_time * 1000)
            end_ms = int(end_time * 1000)
            
            # Extract segment
            segment = audio[start_ms:end_ms]
            
            # Save segment
            output_path = os.path.join(output_dir, f"{wav_base_name}_{i}.wav")
            segment.export(output_path, format="wav")

            wav_scp_dict[key]=output_path
            text_dict[key]=line.split("\t")[-1]
            
    return wav_scp_dict,text_dict


            
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python process_KCSC.py <txt_file> <wav_dir> <output_dir>")
        sys.exit(1)
        
    txt_dir = sys.argv[1]
    wav_dir = sys.argv[2] 
    output_dir = sys.argv[3]
    
    for txt_path in glob.glob(os.path.join(txt_dir,"*.txt")):
        wav_scp_dict,text_dict=process_kcsc_data(txt_path, wav_dir, output_dir)


    with open(os.path.join(output_dir,"wav.scp"),"w",encoding="utf-8") as f:
        for key,value in wav_scp_dict.items():
            f.write(f"{key} {value}\n")
            
    with open(os.path.join(output_dir,"text"),"w",encoding="utf-8") as f:
        for key,value in text_dict.items():
            f.write(f"{key} {value}\n")









