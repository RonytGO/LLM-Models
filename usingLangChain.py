# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 23:43:23 2025

@author: Ronyt
"""


from langchain_openai import OpenAI



# Set up the model (Make sure you have an OpenAI API key)
llm = OpenAI(model_name="gpt-3.5-turbo", openai_api_key="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")

# Run a query
response = llm.invoke("In two sentences: What is LangChain?")
print(response)
