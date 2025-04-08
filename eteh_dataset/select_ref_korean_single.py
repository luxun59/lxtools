'''
Author: luxun59 luxun59@126.com
Date: 2025-02-23 10:30:34
LastEditors: luxun59 luxun59@126.com
LastEditTime: 2025-02-23 11:24:52
FilePath: \eteh_dataset\select_ref_korean_single.py
Description: 

Copyright (c) 2025 by luxun59@126.com, All Rights Reserved. 
'''
def hanja_reading(num):
    # 汉字词读法规则
    tens = {10: '십', 20: '이십', 30: '삼십', 40: '사십', 50: '오십', 60: '육십', 70: '칠십', 80: '팔십', 90: '구십'}
    units = {1: '일', 2: '이', 3: '삼', 4: '사', 5: '오', 6: '육', 7: '칠', 8: '팔', 9: '구'}
    
    if num < 10:
        return units[num]
    elif num % 10 == 0:
        return tens[num]
    else:
        return tens[num // 10 * 10] + units[num % 10]

def 固有词_reading(num):
    # 固有词读法规则
    tens = ['', '십', '이십', '서른', '마흔', '쉰', '예순', '일곱십', '아흔', '구십']
    units = ['', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    
    return tens[num // 10] + units[num % 10]

def mixed_reading(num):
    # 十位汉字词，个位固有词读法规则
    tens_hanja = {10: '십', 20: '이십', 30: '삼십', 40: '사십', 50: '오십', 60: '육십', 70: '칠십', 80: '팔십', 90: '구십'}
    units_固有词 = ['', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    
    return tens_hanja[num // 10 * 10] + units_固有词[num % 10]

# def get_closest_reading(num, transcript):
#     readings = [
#         hanja_reading(num),
#         固有词_reading(num),
#         mixed_reading(num)
#     ]
    
#     closest_reading = min(readings, key=lambda x: levenshtein_distance(transcript, x))
    
#     return closest_reading

def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

# # 示例用法
# numbers = [12, 23, 34, 45, 56, 67, 78, 89, 90, 10]
# transcriptions = [
#     "십이", "이십삼", "삼십사", "사십오", "육십육", "칠십칠", "팔십팔", "구십구", "구십", "십"
# ]

# for num, transcript in zip(numbers, transcriptions):
#     closest = get_closest_reading(num, transcript)
#     print(f"Number: {num}, Transcript: {transcript}, Closest Reading: {closest}")



def parse_string_to_numbers(s):
    # 解析以四位数字一组后面跟空格的字符串为数字列表
    return [int(num_str) for num_str in s.split()]

def parse_transcriptions(s):
    # 假设transcriptions字符串中每个转录结果之间用某种分隔符（比如逗号）分隔
    # 如果它们之间没有分隔符，而是连续排列的，那么需要根据实际情况调整解析逻辑
    # 这里我们假设使用逗号作为分隔符
    return s.split(',')  # 或者根据实际情况使用其他分隔符或解析逻辑

# 之前的函数定义保持不变（hanja_reading, 固有词_reading, mixed_reading, levenshtein_distance）

def get_closest_readings(numbers_str, transcriptions_str):
    # 解析字符串为数字列表和转录结果列表
    numbers = parse_string_to_numbers(numbers_str)
    transcriptions = parse_transcriptions(transcriptions_str)
    
    # 确保numbers和transcriptions的长度相同，或者根据实际情况处理不匹配的情况
    if len(numbers) != len(transcriptions):
        raise ValueError("The number of numbers and transcriptions do not match.")
    
    closest_readings = []
    for num, transcript in zip(numbers, transcriptions):
        # 为每个数字找到最接近的读法
        readings = [
            hanja_reading(num),
            固有词_reading(num),
            mixed_reading(num)
        ]
        closest_reading = min(readings, key=lambda x: levenshtein_distance(transcript.strip(), x))
        closest_readings.append(closest_reading)
    
    return closest_readings

# 示例用法
numbers_str = "0012 0023 0034 0045 0056 0067 0078 0089 0090 0010"
transcriptions_str = "십이,이십삼,삼십사,사십오,육십육,칠십칠,팔십팔,구십구,구십,십"

closest_readings = get_closest_readings(numbers_str, transcriptions_str)
for num_str, closest_reading in zip(numbers_str.split(), closest_readings):
    print(f"Number: {num_str.strip()}, Closest Reading: {closest_reading}")




