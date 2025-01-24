import sys


input_path = sys.argv[1]
output_path = sys.argv[2]




with open(input_path, 'r', encoding='utf-8') as fin,open(
            output_path, 'w', encoding='utf-8') as fout:
    for line in fin:
        line = line.replace("\t"," ")
        fout.write(line)



        