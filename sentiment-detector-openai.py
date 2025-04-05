# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 22:07:39 2025

@author: Ronyt
"""

from openai import OpenAI

client = OpenAI(api_key= "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")


response = client.moderations.create(
    model="omni-moderation-latest",
    input="test that ",
)

print(response)