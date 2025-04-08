'''
Author: luxun59 luxun59@126.com
Date: 2025-02-08 14:19:17
LastEditors: luxun59 luxun59@126.com
LastEditTime: 2025-02-09 23:07:46
FilePath: \lxtools\eteh_dataset\split_number.py
Description: 

Copyright (c) 2025 by luxun59@126.com, All Rights Reserved. 
'''


import re

def replace_spaces_with_underline(text):
    # 使用正则表达式匹配数字之间的空格，并用粗下划线代替
    text = re.sub(r'(\d)\s+(\d)', r'\1▁\2', text)
    
    # 使用正则表达式匹配数字和其它字符之间的边界，并用粗下划线分割
    text = re.sub(r'(\d)([^▁\d])', r'\1▁\2', text)
    text = re.sub(r'([^▁\d])(\d)', r'\1▁\2', text)
    
    return text

# 示例文本
text = "12shuzi45中文abc 78 def 101 1구십구23 4"
text = text.replace(" ", "")
result = replace_spaces_with_underline(text)
print(result)


result_parts = result.split("▁")
for word in result_parts:
    if word.isdigit():
        print(f"{word} 是纯数字")
    else:
        print(f"{word} 不是纯数字")


