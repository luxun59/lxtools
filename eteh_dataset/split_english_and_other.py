import re
import sys


input_name=sys.argv[1]   
output_name=sys.argv[2]  

# def add_underscore_between_langs(text):
#     # 定义正则表达式来匹配英文单词
#     english_word_pattern = r'\b[a-zA-Z]+\b'
    
#     # 定义一个函数，用于替换匹配到的英文单词
#     def replace_with_underscore(match):
#         word = match.group(0)
#         # 在单词前后添加下划线，如果单词前后已经有其他内容则只在单词前添加下划线
#         # 这样可以避免在字符串开头或结尾添加不必要的下划线
#         if match.start() == 0:
#             return word + '▁'
#         elif match.end() == len(text):
#             return '▁' + word
#         else:
#             return '▁' + word + '▁'
    
#     # 使用re.sub()函数进行替换
#     result = re.sub(english_word_pattern, replace_with_underscore, text)
    
#     # 由于替换后可能会在某些位置留下多余的下划线（如两个下划线连在一起），需要进行清理
#     result = result.replace('▁▁', '▁')
#     result = result.replace('▁ ▁', '▁')
#     # 清理开头和结尾可能出现的多余下划线
#     result = result.strip('▁')
    
#     return result
def replace_space_to_underscore(text):
    # Replace multiple spaces with a single space first
    text = re.sub(r'\s+',' ', text)
    return text

# def text_clean_space(text):
#     ispace = [" ","\u00A0","\u0020","\u3000"]
#     for item in ispace:
#         text.replace(item," ")
#     return text

def text_clean_space(input_string):
    # 使用正则表达式将连续的多个空格替换为一个空格
    ispace = [" ","\u00A0","\u0020","\u3000"]
    for item in ispace:
        input_string.replace(item," ")
    import re
    normalized_string = re.sub(r'\s+', ' ', input_string).strip()
    return normalized_string



def replace_space_to_underscore(text):
    # print(text)
    parts = text.strip().split(" ")
    text = '▁'.join(parts)
    return text

# Read input file
with open(input_name, 'r', encoding='utf-8') as fin,open(output_name, 'w', encoding='utf-8') as fout:
    for line in fin:
        line = line.replace("\t"," ")
        parts = line.strip().split(' ')
        key = parts[0]
        if "yodas/ko000/gKde7VSV6R4-00022-00009280-00009480" in key:
            print(line)
            atext = " ".join(parts[1:])
            print(atext)
            for i in atext:
                print(f"'{i}': \\u{ord(i):04x}")

        text = " "
        if len(parts) > 1:
            text = " ".join(parts[1:])
            # Process the text
            # print(text)
            text = text_clean_space(text) 
            # print(text)
            text = replace_space_to_underscore(text)

        print("{} {}".format(key,text),file=fout)


print("Processing complete. Output written to text_processed.txt")