# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 17:38:09 2025

@author: Ronyt
"""

from transformers import BertForQuestionAnswering
from transformers import BertTokenizer
import torch
model_name = "bert-large-uncased-whole-word-masking-finetuned-squad"
model = BertForQuestionAnswering.from_pretrained(model_name)
tokenizer = BertTokenizer.from_pretrained(model_name)

# example question and text containing the answer
question = "When was the first dvd released?"
answer_document = "The first DVD (Digital Versatile Disc) was released on March 24, 1997. It was a movie titled 'Twister' and was released in Japan. DVDs quickly gained popularity as a replacement for VHS tapes and became a common format for storing and distributing digital video and data."

encoding = tokenizer.encode_plus(text=question, text_pair=answer_document)
print(encoding)

inputs = encoding['input_ids']
sentence_embedding = encoding['token_type_ids']
tokens = tokenizer.convert_ids_to_tokens(inputs)
tokenizer.decode(101)
tokenizer.decode(102)
output = model(input_ids = torch.tensor([inputs]), token_type_ids = torch.tensor([sentence_embedding]))
start_index = torch.argmax(output.start_logits)
end_index = torch.argmax(output.end_logits)

print(start_index)
print(end_index)

answer = ' '.join(tokens[start_index:end_index+1])
print(answer)