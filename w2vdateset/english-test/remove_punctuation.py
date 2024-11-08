# import string

# def remove_punctuation(text):
#     # 创建一个没有标点符号的字符串映射
#     translator = str.maketrans('', '', string.punctuation)
#     # 使用translate方法去除标点符号
#     return text.translate(translator)

# # 打开输入文件并读取内容
# with open(r'w2vdateset\english-test\ted3-JamesCameron.txt', 'r', encoding='utf-8') as infile:
#     text = infile.read()

# # 去除标点符号
# cleaned_text = remove_punctuation(text)

# # 将去除标点符号后的文本写入输出文件
# with open('output.txt', 'w', encoding='utf-8') as outfile:
#     outfile.write(cleaned_text)

# print("Punctuation removed and text written to output.txt")


import string

def remove_and_conditionally_space_punctuation(text):
    result = []
    i = 0
    while i < len(text):
        char = text[i]
        if char in ["\""]:
            pass
        elif char in ["—"]:
            i+=1
        elif char in string.punctuation:
            # 如果是标点符号，不添加到结果中
            # 检查下一个字符是否是空格，如果不是则添加空格
            if i + 1 < len(text) and text[i + 1] != ' ' and (text[i + 1] not in string.punctuation ):
                result.append(' ')
            # 不需要设置标记，因为我们直接检查了下一个字符
        else:
            # 如果不是标点符号，直接添加到结果中
            result.append(char)
        i += 1
    
    # 将列表转换为字符串并返回
    return ''.join(result).lower()

# 打开输入文件并读取内容
with open(r'robertgupta.txt', 'r', encoding='utf-8') as infile:
    text = infile.read()

# 去除标点符号并在需要的地方补充空格
cleaned_and_spaced_text = remove_and_conditionally_space_punctuation(text)

# 将处理后的文本写入输出文件
with open('output.txt', 'w', encoding='utf-8') as outfile:
    outfile.write(cleaned_and_spaced_text)

print("Punctuation removed, conditional spaces added, and text written to output.txt")


