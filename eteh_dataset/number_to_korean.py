'''
Author: luxun59 luxun59@126.com
Date: 2025-02-08 15:15:07
LastEditors: luxun59 luxun59@126.com
LastEditTime: 2025-02-09 21:31:21
FilePath: \lxtools\eteh_dataset\number_to_korean.py
Description: 

Copyright (c) 2025 by luxun59@126.com, All Rights Reserved. 
'''

def is_pure_number(word):
    """
    判断一个单词是否是纯数字
    """
    return word.isdigit()

# # 测试用例
# test_words = ["123", "45.67", "7890", "abc123", "٠١٢٣"]  # ٠١٢٣ 是阿拉伯数字

# for word in test_words:
#     result = is_pure_number(word)
#     print(f"'{word}' 是纯数字吗？ {result}")


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
    将一组数字翻译成韩语
    """
    result = []
    for number in numbers:
        if number in korean_numbers:
            result.append(korean_numbers[number])
        else:
            result.append(f"({number}未找到翻译)")  # 如果数字没有对应的翻译
    return " ".join(result)

# 文件路径
# file_path = "eteh_dataset/korean_hanzi_number.txt"
file_path = "eteh_dataset/korean_origin_number.txt"

# 加载数字和韩语的对照表
korean_numbers = load_korean_numbers(file_path)

# 输入一组数字
input_numbers = [11, 2, 3, 4, 5, 10]

# 翻译成韩语
translated_text = translate_numbers_to_korean(input_numbers, korean_numbers)

# 输出结果
print("输入的数字:", input_numbers)
print("翻译成韩语:", translated_text)








