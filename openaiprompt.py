# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 11:03:37 2025

@author: Ronyt
"""

from openai import OpenAI

client = OpenAI(api_key= "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")

# response = client.chat.completions.create(
#   model="gpt-4o-mini",
#   messages=[
#     {
#       "role": "user",
#       "content": "Complete the following: Once upon a time"
#     }
#   ],
#   temperature=0.8,
#   max_tokens=100,
#   top_p=1
# )

# print(response.choices[0].message.content)

def generate_text(prompt, max_tokens):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
                }
            ],
        temperature = 0.8,
        max_tokens = max_tokens,
        top_p=1
        )
    return response.choices[0].message.content

prompt = "Complete the following: Once upon a time"

generated_text = generate_text(prompt,50)
print(generated_text)