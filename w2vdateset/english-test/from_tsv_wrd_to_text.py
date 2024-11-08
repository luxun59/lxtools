




tsv_name=r"C:\Users\luxun\Desktop\testdata\manifest\data_eval.tsv"
wrd_name=r"C:\Users\luxun\Desktop\testdata\manifest\data_eval.wrd"

outfile_name="data_eval.txt"


# 打开文件并逐行读取
with open(tsv_name, 'r', encoding='utf-8') as tsv ,open(
    wrd_name, 'r', encoding='utf-8') as wrd,open(
    outfile_name,'w',encoding='utf-8') as outputfile:
    next(tsv)
    tsv_dict={}
    for line_number, line in enumerate(tsv, start=0):
        file_name=line.split("\t")[0]
        file_name=file_name.split("/")[-1].split(".")[0]
        tsv_dict[line_number]=file_name
    print(len(tsv_dict))
    for line_number1, wrdline in enumerate(wrd, start=0):
        print(tsv_dict[line_number1]+"\t"+wrdline[:-1],file=outputfile)






