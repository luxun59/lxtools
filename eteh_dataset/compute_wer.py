'''
Author: luxun59 luxun59@126.com
Date: 2025-02-08 15:26:19
LastEditors: luxun59 luxun59@126.com
LastEditTime: 2025-02-08 15:38:14
FilePath: \lxtools\eteh_dataset\compute_wer.py
Description: 

Copyright (c) 2025 by luxun59@126.com, All Rights Reserved. 
'''





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

# 示例数据
reference = "the quick brown fox jumps over the lazy dog"
hypothesis = "a fast brown foxi leaped over a sleepy canine"
keywords = ["quick", "fox", "jumps"]  # 假设这些是我们的关键词

# 计算KWER
kwer_value = keyword_error_rate(reference, hypothesis, keywords)
print(f"关键词错误率（KWER）: {kwer_value}")





def char_wer(reference, hypothesis):
    """
    计算字符级别的词错率（WER）。
    
    :param reference: 参考字符串
    :param hypothesis: 假设字符串（待评估的字符串）
    :return: WER值
    """
    # 将字符串拆分为字符列表，以便于编辑操作
    ref_chars = list(reference)
    hyp_chars = list(hypothesis)
    
    # 初始化动态规划表
    d = [[0] * (len(hyp_chars) + 1) for _ in range(len(ref_chars) + 1)]
    
    # 填充动态规划表
    for i in range(len(ref_chars) + 1):
        for j in range(len(hyp_chars) + 1):
            if i == 0:
                d[i][j] = j  # 插入操作
            elif j == 0:
                d[i][j] = i  # 删除操作
            elif ref_chars[i - 1] == hyp_chars[j - 1]:
                d[i][j] = d[i - 1][j - 1]  # 匹配
            else:
                d[i][j] = 1 + min(d[i - 1][j],    # 删除
                                  d[i][j - 1],    # 插入
                                  d[i - 1][j - 1])  # 替换
    
    # 总编辑距离（插入+删除+替换）
    total_edits = d[len(ref_chars)][len(hyp_chars)]
    
    # WER计算：总编辑距离 / 参考字符串长度
    wer = total_edits / len(ref_chars) if len(ref_chars) > 0 else float('inf')
    
    return wer

# 示例使用
reference = "hello"
hypothesis = "hxllo"
wer_value = char_wer(reference, hypothesis)
print(f"字符级别的WER: {wer_value}")








