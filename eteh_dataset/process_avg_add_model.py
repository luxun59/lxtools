'''
Author: luxun luxun59@126.com
Date: 2024-12-31 17:35:10
LastEditors: luxun luxun59@126.com
LastEditTime: 2024-12-31 17:35:22
FilePath: \lxtools\eteh_dataset\process_avg_add_model.py
Description: 

Copyright (c) 2024 by luxun59@126.com, All Rights Reserved. 
'''



import torch
import torch.nn as nn

import sys

args = sys.argv

input_path = sys.argv[1]
output_path = sys.argv[2]


# 加载模型
loaded_model_state_dict = torch.load(input_path)

print(loaded_model_state_dict.keys())

# 将模型包装在字典中
wrapped_model = {'model': loaded_model_state_dict}

print(wrapped_model['model'].keys())

print(wrapped_model.keys())

torch.save(wrapped_model, output_path)


