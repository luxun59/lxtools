'''
Author: luxun luxun59@126.com
Date: 2025-01-21 15:16:12
LastEditors: luxun luxun59@126.com
LastEditTime: 2025-01-23 09:41:21
FilePath: \lxtools\multilingual\get_json.py
Description: 

Copyright (c) 2025 by luxun59@126.com, All Rights Reserved. 
'''




import os
import json

# def get_subdirs(root_dir):
#     """
#     Get all subdirectories under the root directory
    
#     Args:
#         root_dir: Root directory path
        
#     Returns:
#         List of subdirectory paths
#     """
#     subdirs = []
#     for dirpath, dirnames, filenames in os.walk(root_dir):
#         for dirname in dirnames:
#             full_path = os.path.join(dirpath, dirname)
#             subdirs.append(full_path)
#     return subdirs

def combine_json_entries(json_data):
    """
    Combine individual JSON entries into a single JSON object with an "annotation" array
    
    Args:
        json_data: List of individual JSON entries
        
    Returns:
        Combined JSON object with annotation array
    """
    combined_json = {
        "annotation": json_data
    }
    return combined_json


# def get_json_from_txt():

def get_json_from_txt(root_dir,txt_name="transcript_1h_train.txt"):
    """
    Extract json data from txt file with key, source path and target text
    
    Args:
        txt_path: Path to input txt file
        
    Returns:
        List of dictionaries containing key, source and target
    """
    json_data = []
    json_data_and_language = []
    txt_path = os.path.join(root_dir,txt_name)
    with open(txt_path, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) < 3:
                continue
                
            key = parts[0]
            text = parts[2]
            # Create json entry
            entry = {
                "key": key,
                "source": root_dir+"/wav/"+key+".wav", # Use key as source path for now
                "target": text
            }
            json_data.append(entry)
            entry_all = {
                "key": key,
                "source": root_dir+"/wav/"+key+".wav", # Use key as source path for now
                "target": text,
                "lauguage":root_dir.split("/")[-1]
            }
            json_data_and_language.append(entry_all)

    return json_data,json_data_and_language



def write_to_json(root_dir,json_path):
    """
    Write json data to file
    
    Args:
        root_dir: Root directory containing txt files
        json_path: Output json file path
    """
    # Get json data
    json_data, json_data_and_language = get_json_from_txt(root_dir,txt_name)
    
    # Write to json file
    with open(json_path, 'w', encoding='utf-8') as f:
        # json.dump(json_data, f, ensure_ascii=False, indent=4)
        for item in json_data:
            print(item,file=f)
        
    # Write json with language info
    lang_json_path = json_path.replace('.json', '_with_lang.json')
    with open(lang_json_path, 'w', encoding='utf-8') as f:
        # json.dump(json_data_and_language, f, ensure_ascii=False, indent=4)
        for item in json_data_and_language:
            print(item,file=f)



def get_subdirs(root_dir):
    """
    Get all second-level subdirectories under root_dir
    
    Args:
        root_dir: Root directory path
        
    Returns:
        List of second-level subdirectory paths
    """
    subdirs = []
    # 遍历第一级目录
    for first_level in os.listdir(root_dir):
        first_level_path = os.path.join(root_dir, first_level)
        if os.path.isdir(first_level_path):
            # 遍历第二级目录
            for second_level in os.listdir(first_level_path):
                second_level_path = os.path.join(first_level_path, second_level)
                if os.path.isdir(second_level_path):
                    subdirs.append(second_level_path)
    return subdirs

def process_all_subdirs(root_dir,json_path,txt_name):
    """
    Process all subdirectories and generate combined json
    """
    # Get all subdirectories
    subdirs = get_subdirs(root_dir)
    
    # Initialize combined json data
    all_json_data = []
    all_json_data_with_lang = []
    
    # Process each subdir
    for subdir in subdirs:
        json_data, json_data_and_language = get_json_from_txt(subdir,txt_name)
        all_json_data.extend(json_data)
        all_json_data_with_lang.extend(json_data_and_language)
       

    # Write to json file
    with open(json_path, 'w', encoding='utf-8') as f:
        # json.dump(json_data, f, ensure_ascii=False, indent=4)
        for item in all_json_data:
            print(item,file=f)
        
    # Write json with language info
    lang_json_path = json_path.replace('.json', '_with_lang.json')
    with open(lang_json_path, 'w', encoding='utf-8') as f:
        # json.dump(json_data_and_language, f, ensure_ascii=False, indent=4)
        for item in all_json_data_with_lang:
            print(item,file=f)






if __name__ == "__main__":
    import sys
    # if len(sys.argv) != 3:
    #     print("Usage: python get_json.py <root_dir> <json_path>")
    #     sys.exit(1)
    if len(sys.argv) == 3:
        root_dir = sys.argv[1]
        json_path = sys.argv[2]
        txt_name = "transcript_1h_train.txt"
    elif len(sys.argv) == 4:
        root_dir = sys.argv[1]
        json_path = sys.argv[2]
        txt_name = sys.argv[3]
    process_all_subdirs(root_dir,json_path,txt_name)
















