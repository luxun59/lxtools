'''
Author: luxun59 luxun59@126.com
Date: 2025-02-09 22:38:17
LastEditors: luxun59 luxun59@126.com
LastEditTime: 2025-02-09 23:06:27
FilePath: \lxtools\eteh_dataset\make_korean_ref.py
Description: 

Copyright (c) 2025 by luxun59@126.com, All Rights Reserved. 
'''
import argparse

# def load_dictionary(dict_file):
#     with open(dict_file, 'r', encoding='utf-8') as f:
#         dictionary = {}
#         for line in f:
#             key, value = line.strip().split()
#             dictionary[key] = value
#     return dictionary

def keyword_error_rate(reference, hypothesis, keywords):
    """
    计算两句之间的关键词错误率（KWER）。
    
    :param reference: 参考句子（正确句子）
    :param hypothesis: 假设句子（可能包含错误的句子）
    :param keywords: 关键词列表
    :return: KWER值
    """
    # 将句子转换为小写并分割成单词列表
    ref_words = reference.lower().split()
    hyp_words = hypothesis.lower().split()
    
    # 转换为集合以便于快速查找
    ref_set = set(ref_words)
    hyp_set = set(hyp_words)
    
    # 找出参考句子中的关键词
    ref_keywords = [word for word in ref_words if word in keywords]
    
    # 计算错误：插入、删除和替换
    # 注意：这里我们简化处理，只考虑关键词是否在句子中出现，不考虑词序和位置
    # 插入错误：假设句子中有而参考句子中没有的关键词（但这不是标准的KWER计算方式，因为KWER通常不考虑非关键词的插入）
    # 实际上，对于KWER，我们更关心的是关键词是否被错误地删除或替换
    # 因此，这里我们主要计算删除和替换错误
    deletion_errors = sum(1 for keyword in ref_keywords if keyword not in hyp_set)
    substitution_errors = sum(1 for hyp_word in hyp_set if hyp_word in keywords and hyp_word not in ref_set)
    # 注意：这里的替换计算是简化的，因为它只考虑了假设句子中的关键词是否在参考句子中不存在
    # 在更复杂的场景中，你可能需要更精确地匹配和计算替换，比如使用词对齐算法
    
    # 总关键词错误数
    total_errors = deletion_errors + substitution_errors
    
    # KWER计算：总关键词错误数 / 参考句子中的关键词总数
    kwer = total_errors / max(len(ref_keywords), 1)
    
    return kwer

def load_korean_numbers(file_path):
    """
    从文件中加载数字和韩语的对照表，返回一个字典
    """
    korean_numbers = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # 去除空白字符并分割数字和韩语
            number, korean = line.strip().split()
            korean_numbers[int(number)] = korean
    return korean_numbers

def translate_numbers_to_korean(numbers, korean_numbers):
    """
    将一组数字翻译成韩语,输入是一个列表
    """
    result = []
    for number in numbers:
        if number.isdigit():
            if number in korean_numbers:
                result.append(korean_numbers[number])
            else:
                result.append(f"({number}未找到翻译)")  # 如果数字没有对应的翻译
    return " ".join(result)

def read_file_to_dict(filepath):  
    """  
    读取ref.txt文件并返回一个字典，键是文件名，值是该文件名所在行的前面字符串和行号。  
    """  
    file_dict = {}  
    try:  
        with open(filepath, 'r', encoding='utf-8') as file:  
            lines = file.readlines()  
            for line_num, line in enumerate(lines, start=1):  
                transes = line.split(' ')
                file_dict[transes[0].strip()]=' '.join(transes[1:])
    except FileNotFoundError:  
        print(f"文件 {filepath} 未找到。")
    return file_dict  


def process_file(hyp_file,input_file,dict_origin,dict_hanzi, output_file):
    dictionary_origin = load_korean_numbers(dict_origin)
    dictionary_hanzi = load_korean_numbers(dict_hanzi)
    dictionary_hyp = read_file_to_dict(hyp_file)
    with open(input_file, 'r', encoding='utf-8') as f_in, open(
              output_file, 'w', encoding='utf-8') as f_out:
        for line in f_in:
            parts = line.strip().split()
            key = parts[0]
            hyp = dictionary_hyp.get(key, '')
            processed_line = ' '.join(parts[1:])
            # processed_line = processed_line.replace("▁", " ")
            words = processed_line.split("▁")
            ref_origin = translate_numbers_to_korean(words, dictionary_origin)
            ref_hanzi = translate_numbers_to_korean(words, dictionary_hanzi)
            # 计算关键词错误率
            kwer_origin = keyword_error_rate(ref_origin, hyp, dictionary_origin.values())
            kwer_hanzi = keyword_error_rate(ref_hanzi, hyp, dictionary_hanzi.values())
            if kwer_origin < kwer_hanzi:
                processed_line = ref_origin
            else:
                processed_line = ref_hanzi
            # processed_line = ' '.join([dictionary.get(word, word) for word in words])
            f_out.write(key+" "+processed_line + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process a file using a dictionary.')
    parser.add_argument('dict_origin_file', type=str, help='Path to the dictionary file')
    parser.add_argument('dict_hanzi_file', type=str, help='Path to the dictionary file')
    parser.add_argument('input_file', type=str, help='Path to the input file')
    parser.add_argument('hyp_file', type=str, help='Path to the input file')
    parser.add_argument('output_file', type=str, help='Path to the output file')

    args = parser.parse_args()

    # dictionary = load_dictionary(args.dict_file)
    process_file(args.hyp_file,args.input_file,args.dict_origin_file,args.dict_hanzi_file ,args.output_file)