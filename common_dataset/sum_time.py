'''
Author: luxun luxun59@126.com
Date: 2024-11-07 17:34:41
LastEditors: luxun luxun59@126.com
LastEditTime: 2024-11-07 21:11:29
FilePath: \lxtools\common_dataset\sum_time.py
Description: 

Copyright (c) 2024 by luxun59@126.com, All Rights Reserved. 
'''

import os,sys
import soundfile as sf

def get_wav_duration(file_path):
    """获取WAV文件的时长（秒）"""
    try:
        # 使用soundfile读取音频文件，获取采样率和帧数
        data, samplerate = sf.read(file_path)
        # 计算时长：帧数 / 采样率
        duration = len(data) / samplerate
        return duration
    except Exception as e:
        # 如果读取文件时发生错误（如文件格式不支持、文件损坏等），则打印错误信息并返回0
        print(f"无法读取文件 {file_path}: {e}")
        return 0

def calculate_total_duration(directory,file_endname='.wav'):
    """计算指定目录及其子目录下所有WAV文件的总时长"""
    total_duration = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(file_endname):
                file_path = os.path.join(root, file)
                duration = get_wav_duration(file_path)
                total_duration += duration
    return total_duration

if __name__ == "__main__":
    file_endname='.mp3'
    if len(sys.argv)==2:
        current_directory = sys.argv[1]
        
    elif len(sys.argv)==3:
        current_directory = sys.argv[1]
        file_endname=sys.argv[2]
        print("file endwith:",file_endname)
    else:
        current_directory = os.getcwd()  # 获取当前目录

    total_duration = calculate_total_duration(current_directory,file_endname)
    print(f"当前目录及其子目录下所有{file_endname}文件的总时长为: {total_duration:.2f} 秒")