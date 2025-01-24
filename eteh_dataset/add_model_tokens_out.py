



import torch
import torch.nn as nn

from torch.nn.parameter import Parameter


import sys

args = sys.argv

input_path = sys.argv[1]
output_path = sys.argv[2]

origin_odim = 3146
new_odim = 3147




# 加载模型
loaded_model_state_dict = torch.load(input_path)

print(loaded_model_state_dict.keys())
if 'model' not in loaded_model_state_dict.keys():
    # 将模型包装在字典中
    wrapped_model = {'model': loaded_model_state_dict}
else:
    wrapped_model = loaded_model_state_dict


## ctc_layer
# Get the parameters of ctc_Linear
ctc_weight_old = wrapped_model['model']['model.ctc.1.weight']
ctc_bias_old = wrapped_model['model']['model.ctc.1.bias']

ctc_Linear_new = torch.nn.Linear(320,new_odim)
print(ctc_Linear_new)

ctc_weight_new = ctc_Linear_new.weight.clone()
ctc_bias_new = ctc_Linear_new.bias.clone()

ctc_weight_new[:origin_odim,:] = ctc_weight_old
wrapped_model['model']['model.ctc.1.weight'] = Parameter(ctc_weight_new)

ctc_bias_new[:origin_odim] = ctc_bias_old
wrapped_model['model']['model.ctc.1.bias'] = Parameter(ctc_bias_new)


print("CTC Linear Weight Size:", wrapped_model['model']['model.ctc.1.weight'].size())
print("CTC Linear Bias Size:", wrapped_model['model']['model.ctc.1.bias'].size())


## decoder_output_layer
decoder_output_layer_weight_old = wrapped_model['model']['model.decoder.output_layer.weight']
decoder_output_layer_bias_old = wrapped_model['model']['model.decoder.output_layer.bias']


decoder_output_layer_Linear_new = torch.nn.Linear(320,new_odim)
print(decoder_output_layer_Linear_new)

decoder_output_layer_weight_new = decoder_output_layer_Linear_new.weight.clone()
decoder_output_layer_bias_new = decoder_output_layer_Linear_new.bias.clone()

decoder_output_layer_weight_new[:origin_odim,:] = decoder_output_layer_weight_old
wrapped_model['model']['model.decoder.output_layer.weight'] = Parameter(decoder_output_layer_weight_new)

decoder_output_layer_bias_new[:origin_odim] = decoder_output_layer_bias_old
wrapped_model['model']['model.decoder.output_layer.bias'] = Parameter(decoder_output_layer_bias_new)


print("decoder_output_layer Linear Weight Size:", wrapped_model['model']['model.decoder.output_layer.weight'].size())
print("decoder_output_layer Linear Bias Size:", wrapped_model['model']['model.decoder.output_layer.bias'].size())

## deocder_embed

decoder_embed_layer_weight_old = wrapped_model['model']['model.decoder.embed.0.weight']

# torch.nn.Linear(320,new_odim)
decoder_embed_layer_Linear_new = torch.nn.Embedding(new_odim, 320)
print(decoder_embed_layer_Linear_new)

decoder_embed_layer_weight_new = decoder_embed_layer_Linear_new.weight.clone()
# decoder_embed_layer_bias_new = decoder_embed_layer_Linear_new.bias.clone()

decoder_embed_layer_weight_new[:origin_odim,:] = decoder_embed_layer_weight_old
wrapped_model['model']['model.decoder.embed.0.weight'] = Parameter(decoder_embed_layer_weight_new)

# decoder_embed_layer_bias_new[:origin_odim] = decoder_embed_layer_bias_old
# wrapped_model['model']['model.decoder.embed.0.bias'] = Parameter(decoder_embed_layer_bias_new)




torch.save(wrapped_model, output_path)


