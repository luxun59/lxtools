


import sys




def read_ref_file_to_lower(filepath):  
    """  
    读取ref.txt文件并返回一个字典，键是文件名，值是该文件名所在行的前面字符串和行号。  
    """  
    file_dict = {}  
    try:  
        with open(filepath, 'r', encoding='utf-8') as file:  
            lines = file.readlines()  
            for line_num, line in enumerate(lines, start=1):  
                transes = line.split(' ')
                file_dict[transes[0]]=transes[1].lower()
    except FileNotFoundError:  
        print(f"文件 {filepath} 未找到。")
    # print(file_dict)
    return file_dict  





# 定义文件名
if len(sys.argv)==0:
    file_name = r"w2vdateset\english-test\data.tsv"  # 请将此文件名替换为你的实际文件名
    dict_files_path = '/data/home/luxun/dataset/testset/manifest/data_eval.tsv.base'
else:
    file_name=sys.argv[1]   
    dict_files_path=sys.argv[2]   


outfile_name = file_name+'.name'


with open(file_name, 'r', encoding='utf-8') as file, open(
    outfile_name,'w',encoding='utf-8' ) as outfile:  
    lines = file.readlines()  
    filedict=read_ref_file_to_lower(dict_files_path)
    for line_num, line in enumerate(lines, start=1):  
        lineNone = line.split(' ')[0]
        if lineNone in filedict:
            print('{} {}'.format(filedict[lineNone],line[1:]),outfile=outfile)








