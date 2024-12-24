





import sys

def process_log_file(input_file, output_file,error_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(
        output_file, 'w', encoding='utf-8') as outfile, open(
        error_file,'w',encoding='utf-8') as errorfile:
        lines = infile.readlines()
        buffer = []
        
        for line in lines:
            stripped_line = line.strip()
            
            if stripped_line == 'seg#':
                # Start of a new segment, reset the buffer
                buffer = []
            elif stripped_line == '### closed ###':
                # End of the current segment, write it to the output 
                datatext=' '.join(buffer).replace("\n",'') + '\n'
                if "请求错误：" in datatext:
                    errorfile.writelines(datatext)
                else:    
                    outfile.writelines(datatext)
            else:
                # Append the line to the buffer
                buffer.append(stripped_line)

# 定义文件名
if len(sys.argv)<2:
    input_file_path = r'w2vdateset\our_multi_data\rus.log'  # 替换为你的日志文件路径
    output_file_path=input_file_path+'.we'
    error_file=input_file_path+'.we.error'
elif len(sys.argv)==2:
    input_file_path=sys.argv[1] 
    output_file_path=input_file_path+'.we'
    error_file=input_file_path+'.we.error'
else:
    input_file_path=sys.argv[1]   
    output_file_path=sys.argv[2] 
    error_file=  sys.argv[3] 

# 使用示例

process_log_file(input_file_path, output_file_path,error_file)

















